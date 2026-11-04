#!/usr/bin/env bash
# Builds the GateLink simulator from the latest public sources and puts it into the site:
#   KidCe/GateLink main (sim/) + kidce/tinywhoop-led-gate main (gate meshes) -> docs/assets/tinywhoopgate/gatelink-sim/
# Used by .github/workflows/deploy.yml, so the wiki always shows GateLink main. Needs git, node >= 20, npm.
set -euo pipefail
site="$(cd "$(dirname "$0")/.." && pwd)"
work="${GATELINK_WORK:-$(mktemp -d)}"
out="$site/docs/assets/tinywhoopgate/gatelink-sim"

git clone -q --depth 1 https://github.com/KidCe/GateLink "$work/GateLink"
git clone -q --depth 1 --filter=blob:none --sparse https://github.com/kidce/tinywhoop-led-gate "$work/TinywhoopGate"
git -C "$work/TinywhoopGate" sparse-checkout set --no-cone /sources/assembly_viewer/scene.json /outputs/assembly-guide/v01_2026-10-25/data/
mods="$work/TinywhoopGate/tools/assembly_viewer"
mkdir -p "$mods"
(cd "$mods" && npm init -y >/dev/null && npm install --silent --no-audit --no-fund esbuild@0.24.0 three@0.169.0)

node "$work/GateLink/sim/tools/build.mjs" --tinywhoop "$work/TinywhoopGate"
mkdir -p "$out"
cp "$work/GateLink/sim/dist/gatelink-sim.html" "$out/index.html"
sha="$(git -C "$work/GateLink" rev-parse HEAD)"
printf '%s\n' "$sha" > "$out/VERSION"
echo "GateLink simulator $sha -> $out"
