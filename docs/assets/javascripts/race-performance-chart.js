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

  const renderIndividualRacePerformanceChart = () => {
    const canvas = document.getElementById("individual-race-performance-chart");

    if (!canvas || canvas.dataset.chartReady === "true" || !window.Chart) {
      return;
    }

    const races = [
      { date: "11 May 2024", label: "May '24", event: "Aircrasher Aichtal · DCS overall", position: 75, field: 90 },
      { date: "14 Jul 2024", label: "Jul '24", event: "BMR Adelsried · DCS overall", position: 23, field: 37 },
      { date: "2 Nov 2024", label: "Nov '24", event: "Friedrichshafen · DCS overall", position: 13, field: 51 },
      { date: "19 Jan 2025", label: "Jan '25", event: "Galaxy Cup · Whoop", position: 3, field: 24 },
      { date: "13 Apr 2025", label: "Apr '25", event: "Intermodellbau Dortmund · DCS overall", position: 22, field: 48 },
      { date: "30 May 2025", label: "May '25", event: "Aircrasher Aichtal · Street League 1", position: 25, field: 28 },
      { date: "30 May 2025", label: "May '25", event: "Aircrasher Aichtal · Street League 2", position: 16, field: 29 },
      { date: "1 Jun 2025", label: "Jun '25", event: "Aircrasher Aichtal · DCS overall", position: 39, field: 93 },
      { date: "1 Jun 2025", label: "Jun '25", event: "Aircrasher Aichtal · FAI", position: 49, field: 67 },
      { date: "20 Jul 2025", label: "Jul '25", event: "BMR Adelsried · DCS overall", position: 13, field: 45 },
      { date: "12 Sep 2025", label: "Sep '25", event: "MultiGP European Championship", position: 46, field: 86 },
      { date: "27 Sep 2025", label: "Sep '25", event: "LVB Modellflugtage Oberschleißheim", position: 3, field: 10 },
      { date: "2 Nov 2025", label: "Nov '25", event: "Friedrichshafen · DCS overall", position: 17, field: 54 },
      { date: "21 Feb 2026", label: "Feb '26", event: "Spring Whooprace · Whoop", position: 1, field: 6 },
      { date: "29 Mar 2026", label: "Mar '26", event: "Open Belgian Championship · Heat 1", position: 15, field: 39 },
      { date: "5 Apr 2026", label: "Apr '26", event: "Rotormaniacs · Central Europe RQ · Whoop", position: 2, field: 8 },
      { date: "11 Apr 2026", label: "Apr '26", event: "Aircrasher Aichtal · DCS overall", position: 13, field: 40 },
      { date: "15 May 2026", label: "May '26", event: "Aircrasher Aichtal · Street League", position: 20, field: 22 },
      { date: "17 May 2026", label: "May '26", event: "Aircrasher Aichtal · FAI", position: 49, field: 77 },
      { date: "17 May 2026", label: "May '26", event: "Aircrasher Aichtal · DCS overall", position: 41, field: 96 },
      { date: "14 Jun 2026", label: "Jun '26", event: "TSV Feldkirchen · Central Europe RQ", position: 3, field: 15 },
      { date: "20 Jun 2026", label: "Jun '26", event: "BMR Adelsried · DCS overall", position: 9, field: 33 },
      { date: "28 Jun 2026", label: "Jun '26", event: "FAI World Drone Cup Belgium", position: 23, field: 53 },
      { date: "12 Jul 2026", label: "Jul '26", event: "FAI World Drone Cup Italy · provisional", position: 13, field: 37 }
    ].map((race) => ({
      ...race,
      score: Math.round(((race.field - race.position) / (race.field - 1)) * 1000) / 10
    }));

    canvas.dataset.chartReady = "true";
    const styles = getComputedStyle(document.body);
    const color = (name, fallback) =>
      styles.getPropertyValue(name).trim() || fallback;

    new window.Chart(canvas, {
      type: "line",
      data: {
        labels: races.map((race) => race.label),
        datasets: [
          {
            label: "Final performance",
            data: races.map((race) => race.score),
            races,
            borderColor: color("--fpv-orange", "#ff5a1f"),
            backgroundColor: color("--fpv-orange", "#ff5a1f"),
            pointBackgroundColor: color("--fpv-orange", "#ff5a1f"),
            pointBorderColor: color("--md-default-bg-color", "#ffffff"),
            pointBorderWidth: 1.5,
            pointRadius: 4.5,
            pointHoverRadius: 7,
            borderWidth: 2,
            tension: 0.18
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: false,
        interaction: {
          mode: "nearest",
          intersect: false
        },
        plugins: {
          legend: {
            display: false
          },
          tooltip: {
            callbacks: {
              title: (items) => races[items[0].dataIndex].event,
              label: (context) => {
                const race = races[context.dataIndex];
                return `Final: #${race.position} of ${race.field} · ${race.score}% field beaten`;
              },
              afterLabel: (context) => races[context.dataIndex].date
            }
          }
        },
        scales: {
          x: {
            grid: {
              display: false
            },
            ticks: {
              autoSkip: true,
              maxTicksLimit: 9,
              maxRotation: 0,
              color: color("--md-default-fg-color--light", "#6f747d")
            }
          },
          y: {
            min: 0,
            max: 100,
            ticks: {
              stepSize: 25,
              color: color("--md-default-fg-color--light", "#6f747d"),
              callback: (value) => `${value}%`
            },
            title: {
              display: true,
              text: "Field beaten",
              color: color("--md-default-fg-color--light", "#6f747d")
            },
            grid: {
              color: (context) =>
                context.tick.value === 50
                  ? color("--fpv-chart-midfield", "rgba(127, 127, 127, 0.5)")
                  : color("--fpv-chart-grid", "rgba(127, 127, 127, 0.18)")
            }
          }
        }
      }
    });
  };

  const renderCharts = () => {
    renderRacePerformanceChart();
    renderIndividualRacePerformanceChart();
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderCharts);
  } else {
    renderCharts();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(renderCharts);
  }
})();
