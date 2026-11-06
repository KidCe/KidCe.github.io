(function () {
  function init() {
    var bar = document.querySelector(".article-filter");
    if (!bar) return;
    var rows = document.querySelectorAll(".article-row[data-section]");
    bar.addEventListener("click", function (event) {
      var chip = event.target.closest(".article-filter__chip");
      if (!chip) return;
      var wanted = chip.getAttribute("data-filter");
      bar.querySelectorAll(".article-filter__chip").forEach(function (c) {
        c.classList.toggle("is-active", c === chip);
      });
      rows.forEach(function (row) {
        row.hidden = wanted !== "" && row.getAttribute("data-section") !== wanted;
      });
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
