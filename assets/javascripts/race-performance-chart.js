(() => {
  const squadRaceSeries = {};

  const trailingAverage = (values, windowSize = 5) =>
    values.map((_, index) => {
      if (index < windowSize - 1) {
        return null;
      }

      const window = values.slice(index - windowSize + 1, index + 1);
      return Math.round((window.reduce((sum, value) => sum + value, 0) / windowSize) * 10) / 10;
    });

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
            data: [38.9, 57, 63.2],
            samples: [3, 10, 9],
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
      { date: "29 Mar 2026", label: "Mar '26", event: "Open Belgian Championship · Heat 1", position: 15, field: 39 },
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

    squadRaceSeries.kidce = races;

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
        labels: races.map((race) => race.label),
        datasets: [
          {
            id: "race-result",
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
          },
          {
            id: "moving-average",
            label: "5-race moving average",
            data: trailingAverage(races.map((race) => race.score)),
            borderColor: color("--fpv-chart-qualifying", "#6f747d"),
            backgroundColor: color("--fpv-chart-qualifying", "#6f747d"),
            pointRadius: 0,
            pointHoverRadius: 4,
            borderWidth: 3,
            borderDash: [7, 5],
            tension: 0.3,
            spanGaps: false
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
            display: true,
            position: "bottom",
            labels: {
              color: color("--md-default-fg-color", "#111317"),
              usePointStyle: true,
              padding: 18
            }
          },
          tooltip: {
            callbacks: {
              title: (items) => races[items[0].dataIndex].event,
              label: (context) => {
                const race = races[context.dataIndex];

                if (context.dataset.id === "moving-average") {
                  return `5-race moving average: ${context.parsed.y}%`;
                }

                return `Final: #${race.position} of ${race.field} · ${race.score}% field beaten`;
              },
              footer: (items) => races[items[0].dataIndex].date
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

  const renderSquadPilotChart = (canvasId, sourceRaces, pilotKey) => {
    const canvas = document.getElementById(canvasId);

    const races = sourceRaces.map((race) => ({
      ...race,
      score: Math.round(((race.field - race.position) / (race.field - 1)) * 1000) / 10
    }));

    squadRaceSeries[pilotKey] = races;

    if (!canvas || canvas.dataset.chartReady === "true" || !window.Chart) {
      return;
    }

    const scores = races.map((race) => race.score);

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
            id: "race-result",
            label: "Final performance",
            data: scores,
            borderColor: color("--fpv-orange", "#ff5a1f"),
            backgroundColor: color("--fpv-orange", "#ff5a1f"),
            pointBackgroundColor: color("--fpv-orange", "#ff5a1f"),
            pointBorderColor: color("--md-default-bg-color", "#ffffff"),
            pointBorderWidth: 1.5,
            pointRadius: 4.5,
            pointHoverRadius: 7,
            borderWidth: 2,
            tension: 0.18
          },
          {
            id: "moving-average",
            label: "5-race moving average",
            data: trailingAverage(scores),
            borderColor: color("--fpv-chart-qualifying", "#6f747d"),
            backgroundColor: color("--fpv-chart-qualifying", "#6f747d"),
            pointRadius: 0,
            pointHoverRadius: 4,
            borderWidth: 3,
            borderDash: [7, 5],
            tension: 0.3,
            spanGaps: false
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
              title: (items) => races[items[0].dataIndex].event,
              label: (context) => {
                const race = races[context.dataIndex];

                if (context.dataset.id === "moving-average") {
                  return `5-race moving average: ${context.parsed.y}%`;
                }

                return `Final: #${race.position} of ${race.field} · ${race.score}% field beaten`;
              },
              footer: (items) => races[items[0].dataIndex].date
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

  const renderSquadRacePerformanceCharts = () => {
    renderSquadPilotChart(
      "kidce-squad-race-performance-chart",
      squadRaceSeries.kidce || [],
      "kidce"
    );

    renderSquadPilotChart("maxdax-race-performance-chart", [
      { date: "14 Jul 2024", label: "Jul '24", event: "BMR Adelsried · DCS overall", position: 35, field: 37 },
      { date: "2 Nov 2024", label: "Nov '24", event: "Friedrichshafen · DCS overall", position: 19, field: 51 },
      { date: "13 Apr 2025", label: "Apr '25", event: "Intermodellbau Dortmund · DCS overall", position: 13, field: 48 },
      { date: "30 May 2025", label: "May '25", event: "Street League Aichtal 1", position: 9, field: 28 },
      { date: "30 May 2025", label: "May '25", event: "Street League Aichtal 2", position: 10, field: 29 },
      { date: "31 May 2025", label: "May '25", event: "Aircrasher Aichtal · DCS overall", position: 36, field: 93 },
      { date: "31 May 2025", label: "May '25", event: "Aircrasher Aichtal · FAI", position: 53, field: 67 },
      { date: "20 Jul 2025", label: "Jul '25", event: "BMR Adelsried · DCS overall", position: 7, field: 45 },
      { date: "13 Sep 2025", label: "Sep '25", event: "MultiGP European Championship", position: 39, field: 86 },
      { date: "2 Nov 2025", label: "Nov '25", event: "Friedrichshafen · DCS overall", position: 8, field: 54 },
      { date: "29 Mar 2026", label: "Mar '26", event: "Open Belgian Championship · Heat 1", position: 6, field: 39 },
      { date: "11 Apr 2026", label: "Apr '26", event: "Aircrasher Aichtal · DCS overall", position: 14, field: 40 },
      { date: "15 May 2026", label: "May '26", event: "Aircrasher Aichtal · Street League", position: 6, field: 22 },
      { date: "16 May 2026", label: "May '26", event: "Aircrasher Aichtal · FAI", position: 20, field: 77 },
      { date: "16 May 2026", label: "May '26", event: "Aircrasher Aichtal · DCS overall", position: 28, field: 96 },
      { date: "14 Jun 2026", label: "Jun '26", event: "TSV Feldkirchen · Central Europe RQ", position: 4, field: 15 },
      { date: "20 Jun 2026", label: "Jun '26", event: "BMR Adelsried · DCS overall", position: 4, field: 33 },
      { date: "28 Jun 2026", label: "Jun '26", event: "FAI World Drone Cup Belgium", position: 21, field: 53 },
      { date: "12 Jul 2026", label: "Jul '26", event: "FAI World Drone Cup Italy · provisional", position: 12, field: 37 }
    ], "maxdax");

    renderSquadPilotChart("bajo-race-performance-chart", [
      { date: "10 May 2024", label: "May '24", event: "Aircrasher Aichtal · FAI", position: 85, field: 90 },
      { date: "11 May 2024", label: "May '24", event: "Aircrasher Aichtal · DCS overall", position: 82, field: 90 },
      { date: "14 Jul 2024", label: "Jul '24", event: "BMR Adelsried · DCS overall", position: 30, field: 37 },
      { date: "2 Nov 2024", label: "Nov '24", event: "Friedrichshafen · DCS overall", position: 12, field: 51 },
      { date: "13 Apr 2025", label: "Apr '25", event: "Intermodellbau Dortmund · DCS overall", position: 17, field: 48 },
      { date: "1 Jun 2025", label: "Jun '25", event: "Aircrasher Aichtal · FAI", position: 32, field: 67 },
      { date: "1 Jun 2025", label: "Jun '25", event: "Aircrasher Aichtal · DCS overall", position: 50, field: 93 },
      { date: "20 Jul 2025", label: "Jul '25", event: "BMR Adelsried · DCS overall", position: 3, field: 45 },
      { date: "13 Sep 2025", label: "Sep '25", event: "MultiGP European Championship", position: 21, field: 86 },
      { date: "2 Nov 2025", label: "Nov '25", event: "Friedrichshafen · DCS overall", position: 2, field: 54 },
      { date: "11 Apr 2026", label: "Apr '26", event: "Aircrasher Aichtal · DCS overall", position: 7, field: 40 },
      { date: "17 May 2026", label: "May '26", event: "Aircrasher Aichtal · FAI", position: 22, field: 77 },
      { date: "17 May 2026", label: "May '26", event: "Aircrasher Aichtal · DCS overall", position: 9, field: 96 },
      { date: "20 Jun 2026", label: "Jun '26", event: "BMR Adelsried · DCS overall", position: 3, field: 33 },
      { date: "28 Jun 2026", label: "Jun '26", event: "FAI World Drone Cup Belgium", position: 10, field: 53 },
      { date: "12 Jul 2026", label: "Jul '26", event: "FAI World Drone Cup Italy · provisional", position: 2, field: 37 }
    ], "bajo");

    renderSquadPilotChart("zelaus-race-performance-chart", [
      { date: "11 Feb 2024", label: "Feb '24", event: "Modell Leben Erfurt · DCS overall", position: 30, field: 34 },
      { date: "21 Apr 2024", label: "Apr '24", event: "Intermodellbau Dortmund · DCS overall", position: 30, field: 32 },
      { date: "10 May 2024", label: "May '24", event: "Aircrasher Aichtal · FAI", position: 69, field: 90 },
      { date: "11 May 2024", label: "May '24", event: "Aircrasher Aichtal · DCS overall", position: 70, field: 90 },
      { date: "14 Jul 2024", label: "Jul '24", event: "BMR Adelsried · DCS overall", position: 33, field: 37 },
      { date: "2 Nov 2024", label: "Nov '24", event: "Friedrichshafen · DCS overall", position: 40, field: 51 },
      { date: "13 Apr 2025", label: "Apr '25", event: "Intermodellbau Dortmund · DCS overall", position: 45, field: 48 },
      { date: "30 May 2025", label: "May '25", event: "Street League Aichtal 1", position: 21, field: 28 },
      { date: "30 May 2025", label: "May '25", event: "Street League Aichtal 2", position: 24, field: 29 },
      { date: "31 May 2025", label: "May '25", event: "Aircrasher Aichtal · FAI", position: 59, field: 67 },
      { date: "31 May 2025", label: "May '25", event: "Aircrasher Aichtal · DCS overall", position: 86, field: 93 },
      { date: "20 Jul 2025", label: "Jul '25", event: "BMR Adelsried · DCS overall", position: 40, field: 45 },
      { date: "12 Sep 2025", label: "Sep '25", event: "MultiGP European Championship", position: 81, field: 86 },
      { date: "2 Nov 2025", label: "Nov '25", event: "Friedrichshafen · DCS overall", position: 40, field: 54 },
      { date: "29 Mar 2026", label: "Mar '26", event: "Open Belgian Championship · Heat 1", position: 31, field: 39 },
      { date: "11 Apr 2026", label: "Apr '26", event: "Aircrasher Aichtal · DCS overall", position: 35, field: 40 },
      { date: "15 May 2026", label: "May '26", event: "Aircrasher Aichtal · Street League", position: 17, field: 22 },
      { date: "16 May 2026", label: "May '26", event: "Aircrasher Aichtal · FAI", position: 69, field: 77 },
      { date: "16 May 2026", label: "May '26", event: "Aircrasher Aichtal · DCS overall", position: 79, field: 96 },
      { date: "14 Jun 2026", label: "Jun '26", event: "TSV Feldkirchen · Central Europe RQ", position: 12, field: 15 },
      { date: "20 Jun 2026", label: "Jun '26", event: "BMR Adelsried · DCS overall", position: 30, field: 33 },
      { date: "28 Jun 2026", label: "Jun '26", event: "FAI World Drone Cup Belgium", position: 48, field: 53 },
      { date: "12 Jul 2026", label: "Jul '26", event: "FAI World Drone Cup Italy · provisional", position: 25, field: 37 }
    ], "zelaus");
  };

  const dateToTimestamp = (date) => {
    const months = {
      Jan: 0,
      Feb: 1,
      Mar: 2,
      Apr: 3,
      May: 4,
      Jun: 5,
      Jul: 6,
      Aug: 7,
      Sep: 8,
      Oct: 9,
      Nov: 10,
      Dec: 11
    };
    const match = date.match(/^(\d{1,2}) ([A-Z][a-z]{2}) (\d{4})$/);

    if (!match || months[match[2]] === undefined) {
      return null;
    }

    return Date.UTC(Number(match[3]), months[match[2]], Number(match[1]));
  };

  const renderSquadComparisonChart = () => {
    const canvas = document.getElementById("squad-trend-comparison-chart");

    if (!canvas || canvas.dataset.chartReady === "true" || !window.Chart) {
      return;
    }

    canvas.dataset.chartReady = "true";
    const styles = getComputedStyle(document.body);
    const color = (name, fallback) =>
      styles.getPropertyValue(name).trim() || fallback;
    const dateFormatter = new Intl.DateTimeFormat("en", {
      month: "short",
      year: "2-digit",
      timeZone: "UTC"
    });
    const pilots = [
      { key: "kidce", label: "KidCe", color: "--fpv-chart-kidce", fallback: "#ff5a1f", pointStyle: "circle" },
      { key: "maxdax", label: "MaxDax", color: "--fpv-chart-maxdax", fallback: "#1976c9", pointStyle: "rectRot" },
      { key: "bajo", label: "bajo", color: "--fpv-chart-bajo", fallback: "#238a62", pointStyle: "triangle" },
      { key: "zelaus", label: "ZeLaus", color: "--fpv-chart-zelaus", fallback: "#8e57b5", pointStyle: "rect" }
    ];
    const datasets = pilots.map((pilot) => {
      const races = squadRaceSeries[pilot.key] || [];
      const averages = trailingAverage(races.map((race) => race.score));
      const seriesColor = color(pilot.color, pilot.fallback);

      return {
        label: pilot.label,
        data: races
          .map((race, index) => ({
            x: dateToTimestamp(race.date),
            y: averages[index],
            race
          }))
          .filter((point) => point.x !== null && point.y !== null),
        parsing: false,
        borderColor: seriesColor,
        backgroundColor: seriesColor,
        pointStyle: pilot.pointStyle,
        pointRadius: 4,
        pointHoverRadius: 7,
        borderWidth: 2.5,
        tension: 0.25
      };
    });

    new window.Chart(canvas, {
      type: "line",
      data: { datasets },
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
            position: "bottom",
            labels: {
              color: color("--md-default-fg-color", "#111317"),
              usePointStyle: true,
              padding: 18
            }
          },
          tooltip: {
            callbacks: {
              title: (items) => items[0].raw.race.date,
              label: (context) =>
                `${context.dataset.label}: ${context.parsed.y}% five-race average`,
              afterLabel: (context) => context.raw.race.event
            }
          }
        },
        scales: {
          x: {
            type: "linear",
            grid: {
              display: false
            },
            ticks: {
              color: color("--md-default-fg-color--light", "#6f747d"),
              maxRotation: 0,
              maxTicksLimit: 9,
              callback: (value) => dateFormatter.format(new Date(value))
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
              text: "Field beaten · 5-race average",
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
    renderSquadRacePerformanceCharts();
    renderSquadComparisonChart();
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
