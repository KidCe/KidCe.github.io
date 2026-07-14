(() => {
  const renderRacePerformanceChart = () => {
    const canvas = document.getElementById("race-performance-chart");

    if (!canvas || canvas.dataset.chartReady === "true" || !window.Chart) {
      return;
    }

    canvas.dataset.chartReady = "true";
    const styles = getComputedStyle(document.body);
    const color = (name, fallback) =>
      styles.getPropertyValue(name).trim() || fallback;

    new window.Chart(canvas, {
      type: "line",
      data: {
        labels: ["2024", "2025", "2026 YTD"],
        datasets: [
          {
            label: "Qualifying median",
            data: [44.4, 59, 61.5],
            samples: [11, 23, 15],
            borderColor: color("--fpv-chart-qualifying", "#6f747d"),
            backgroundColor: color("--fpv-chart-qualifying", "#6f747d"),
            pointStyle: "circle",
            pointRadius: 5,
            pointHoverRadius: 7,
            borderWidth: 2,
            tension: 0.25
          },
          {
            label: "Final median",
            data: [38.9, 57, 66.7],
            samples: [3, 10, 11],
            borderColor: color("--fpv-orange", "#ff5a1f"),
            backgroundColor: color("--fpv-orange", "#ff5a1f"),
            pointStyle: "triangle",
            pointRadius: 6,
            pointHoverRadius: 8,
            borderWidth: 3,
            tension: 0.25
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: false,
        interaction: {
          mode: "index",
          intersect: false
        },
        plugins: {
          legend: {
            position: "bottom",
            labels: {
              color: color("--md-default-fg-color", "#111317"),
              usePointStyle: true,
              padding: 18
            }
          },
          tooltip: {
            callbacks: {
              label: (context) =>
                `${context.dataset.label}: ${Math.round(context.parsed.y)}%`,
              afterLabel: (context) =>
                `Results included: ${context.dataset.samples[context.dataIndex]}`
            }
          }
        },
        scales: {
          x: {
            grid: {
              display: false
            },
            ticks: {
              color: color("--md-default-fg-color--light", "#6f747d")
            }
          },
          y: {
            min: 0,
            max: 100,
            ticks: {
              color: color("--md-default-fg-color--light", "#6f747d"),
              callback: (value) => `${value}%`
            },
            title: {
              display: true,
              text: "Field beaten",
              color: color("--md-default-fg-color--light", "#6f747d")
            },
            grid: {
              color: color("--fpv-chart-grid", "rgba(127, 127, 127, 0.18)")
            }
          }
        }
      }
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderRacePerformanceChart);
  } else {
    renderRacePerformanceChart();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(renderRacePerformanceChart);
  }
})();
