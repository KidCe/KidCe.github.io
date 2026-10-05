const {chromium}=require('playwright'),assert=require('assert'),fs=require('fs'),path=require('path');
const url=process.env.CELL_SELECTOR_URL||'http://127.0.0.1:8765/site/tools/cell-selector/';
const snapshot=JSON.parse(fs.readFileSync(path.resolve(__dirname,'../dist/data/cells.json')));
const output=path.resolve(__dirname,'../test-results');fs.mkdirSync(output,{recursive:true});
const loaded=page=>page.waitForFunction(()=>document.querySelector('#cells')?.children.length===72);
async function overflow(page,label){const dims=await page.evaluate(()=>({viewport:innerWidth,body:document.body.scrollWidth,doc:document.documentElement.scrollWidth}));assert(dims.doc<=dims.viewport&&dims.body<=dims.viewport,`${label}: page overflow ${JSON.stringify(dims)}`);}
async function filters(page,width,action){if(width<=760)await page.locator('#filterToggle').click();await action();if(width<=760)await page.locator('#closeFilters').click();}
async function chartVisible(page){const dims=await page.locator('#filterPreview').evaluate(e=>{const r=e.getBoundingClientRect();return {top:r.top,bottom:r.bottom,height:r.height,viewport:innerHeight}});assert(dims.top>=0&&dims.bottom<dims.viewport&&dims.height>=180,JSON.stringify(dims));assert(await page.locator('#filterPreview #radar').isVisible());}
(async()=>{
const browser=await chromium.launch({channel:'chrome',headless:true});let errors=[],oldSiteCalls=[];
try{
for(const width of [320,360,390,1440]){
 const context=await browser.newContext({viewport:{width,height:850}}),page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(r.url().includes('nkon-cell-selector.kidce.chatgpt.site'))oldSiteCalls.push(r.url())});
 await page.goto(url);await loaded(page);await overflow(page,`${width} initial`);assert.equal(await page.locator('.pricing,#priceChart,#tierList').count(),0);assert.equal(await page.locator('#axisBtn').isVisible(),false);assert.equal(await page.locator('#scaleReference').inputValue(),'70');
 await page.locator('#scaleReference').fill('100');await page.locator('#scaleReference').dispatchEvent('input');await page.waitForTimeout(750);const databaseMax=await page.locator('#radar [data-domain="capacity"]').getAttribute('data-max');
 await filters(page,width,async()=>{await page.locator('#search').fill('50ME');if(width<=760){await chartVisible(page);await overflow(page,`${width} split filters`);}});
 assert.equal(await page.locator('#cells .offer-card').count(),3);await page.waitForTimeout(750);assert.equal(await page.locator('#radar [data-domain="capacity"]').getAttribute('data-max'),databaseMax);await page.locator('#scaleReference').fill('70');await page.locator('#scaleReference').dispatchEvent('input');const text=await page.locator('#cells').innerText();for(const variant of ['New / regular','Mixed Batch','Reclaimed'])assert(text.includes(variant));
 await page.locator('#cells [data-favorite="cell-029"]').click();await page.locator('#cells [data-emphasize="cell-029"]').click();
 await filters(page,width,()=>page.locator('#search').fill('no-match-xyz'));assert.equal(await page.locator('#cells .offer-card').count(),0);assert.equal(await page.locator('#legend .legend-item').count(),1);assert.equal(await page.locator('#radar [data-radar-cell="cell-029"] [data-shape]').getAttribute('stroke-width'),'3.3');
 await page.locator('.chart-legend>summary').click();await page.locator('#legend [data-detail="cell-029"]').click();assert((await page.locator('#detailsContent').innerText()).includes('6097335778791'));const evidence=page.locator('#detailsContent a[href*="visual-evidence"]');assert.equal((await page.request.get(await evidence.getAttribute('href'))).status(),200);await overflow(page,`${width} details`);await page.locator('#details .close').click();
 await filters(page,width,()=>page.locator('#search').fill('50ME'));
 await page.locator('.display-settings>summary').click();await page.locator('#axisBtn').click();await page.locator('[data-curve="capacity"]').selectOption('high');
 if(width<=760){await chartVisible(page);assert(await page.locator('#mobileCurveNotice').isVisible());await page.locator('#filterBody').evaluate(e=>e.scrollTop=e.scrollHeight);await chartVisible(page);await overflow(page,`${width} axes`);await page.locator('#closeFilters').click();}else assert(await page.locator('#curveNotice').isVisible());
 await page.locator('#cells .extra-specs').first().locator('summary').click();await overflow(page,`${width} specs`);
 await page.screenshot({path:path.join(output,`wiki-${width}.png`)});
 await page.reload();await page.waitForFunction(()=>document.querySelector('#cells')?.children.length===3);assert.equal(await page.locator('[data-curve="capacity"]').inputValue(),'high');
 await filters(page,width,()=>page.locator('#reset').click());await loaded(page);
 if(width<=760){
  await page.locator('#filterToggle').click();const graphBefore=await page.locator('#radar [data-domain="capacity"]').getAttribute('data-min');
  const slider=page.locator('.range-filter[data-key="capacity"] input[type="range"][data-edge="0"]');await slider.scrollIntoViewIfNeeded();const box=await slider.boundingBox();await page.mouse.move(box.x+14,box.y+box.height/2);await page.mouse.down();await page.mouse.move(box.x+box.width*.7,box.y+box.height/2,{steps:8});await page.mouse.up();await page.waitForTimeout(750);assert(Number(await slider.inputValue())>0,'Slider can be dragged');assert.notEqual(await page.locator('#radar [data-domain="capacity"]').getAttribute('data-min'),graphBefore);
  await chartVisible(page);const previewTop=await page.locator('#filterPreview').evaluate(e=>e.getBoundingClientRect().top);await page.locator('.advanced>summary').click();await page.locator('#filterBody').evaluate(e=>e.scrollTop=e.scrollHeight);assert.equal(await page.locator('#filterPreview').evaluate(e=>e.getBoundingClientRect().top),previewTop);await chartVisible(page);
  await page.keyboard.press('Escape');assert.equal(await page.locator('#filterDialog').evaluate(d=>d.open),false);assert.equal(await page.locator('.compare #radar').count(),1);
  await page.locator('#filterToggle').click();await page.locator('#filterQuantity').fill('10');assert.equal(await page.locator('#purchaseQuantity').inputValue(),'10');await page.locator('#reset').click();await page.locator('#closeFilters').click();await loaded(page);
 }else{
  const offer=snapshot.cells.find(c=>c.id==='cell-047');await page.locator('#search').fill('P50B');
  for(const tier of offer.priceTiers)for(const n of [tier.minPacks-1,tier.minPacks]){await page.locator('#purchaseQuantity').fill(String(n));const expected=[{minPacks:1,pricePack:offer.pricePack},...offer.priceTiers].filter(t=>t.minPacks<=n).at(-1).pricePack;const row=page.locator('[data-offer="cell-047"]');assert((await row.locator('[data-spec="price"] .num').innerText()).includes(new Intl.NumberFormat('en-GB',{style:'currency',currency:'EUR'}).format(expected)));await page.locator('.range-filter[data-key="price"] input.number[data-edge="1"]').fill(String(expected));assert.equal(await row.count(),1);await page.locator('.range-filter[data-key="price"] input.number[data-edge="1"]').fill('20');}
  await page.locator('#reset').click();await page.locator('#dataBtn').click();for(const link of await page.locator('#dataDialog a[download]').all())assert.equal((await page.request.get(new URL(await link.getAttribute('href'),page.url()).href)).status(),200);await page.locator('#dataDialog .close').click();
  await page.goto(new URL('../../Web%20Tools/',url).href);await page.locator('.md-content a[href*="tools/cell-selector"]').first().click();await loaded(page);await page.goBack();await page.goForward();await loaded(page);
 }
 await context.close();console.log(`PASS browser ${width}px: compact UI, variants, modal controls, live visible chart, prices and persistence`);
}
if(process.env.CELL_SELECTOR_INSTANT_URL){
 const page=await browser.newPage({viewport:{width:390,height:850}});let requests=0;page.on('request',r=>{if(r.url().endsWith('/cell-selector/data/cells.json'))requests++});page.on('pageerror',e=>errors.push(e.message));await page.goto(process.env.CELL_SELECTOR_INSTANT_URL);await loaded(page);await page.evaluate(()=>window.instantSentinel=true);
 await filters(page,390,()=>page.locator('#search').fill('50ME'));await page.locator('#cells [data-favorite="cell-029"]').click();await page.locator('.display-settings>summary').click();await page.locator('#axisBtn').click();await page.locator('[data-curve="price"]').selectOption('low');await page.locator('#closeFilters').click();
 for(let i=0;i<2;i++){await page.locator('.md-footer__link--prev').click();await page.waitForFunction(()=>!document.querySelector('#fpv-nkon-tool'));assert(await page.evaluate(()=>window.instantSentinel));await page.locator('.md-content a[href*="tools/cell-selector"]').first().click();await page.waitForFunction(()=>document.querySelector('#cells')?.children.length===3);assert.equal(await page.locator('[data-curve="price"]').inputValue(),'low');assert.equal(await page.locator('#cells [data-favorite="cell-029"]').getAttribute('aria-pressed'),'true');}
 assert.equal(requests,3);await page.close();console.log('PASS: real Material Instant Navigation, two round trips and one data fetch per mount.');
}
assert.deepEqual(errors,[]);assert.deepEqual(oldSiteCalls,[]);console.log('PASS: no old Site calls or JavaScript errors.');
}finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
