export const data = {
  labels: [
    'Linux',
    'Networking',
    'Docker',
    'Programming',
    'Kubernetes',
    'CI/CD'
  ],
  datasets: [
    {
      label: 'Hard-Skills',
      backgroundColor: 'rgba(0, 255, 255, 0.2)', // Cyan with low opacity for the area fill
      borderColor: 'rgb(0, 255, 255)', // Bright cyan for the outline
      pointBackgroundColor: 'rgb(0, 255, 255)', // Cyan for points
      pointBorderColor: '#fff', // White for point borders
      pointHoverBackgroundColor: '#fff', // White for hover
      pointHoverBorderColor: 'rgb(0, 255, 255)', // Cyan for hover borders
      data: [70, 50, 80, 80, 60, 85]
    }
  ]
};

export const options = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    r: {
      grid: {
        color: 'rgba(255, 255, 255, 0.2)', // Light grey grid lines for contrast
      },
      angleLines: {
        color: 'rgba(255, 255, 255, 0.5)' // Lighter grey for angle lines
      },
      pointLabels: {
        font: {
          size: 14
        },
        color: 'rgba(255, 255, 255, 0.7)' // Light white for labels
      },
      ticks: {
        backdropColor: 'rgba(0, 0, 0, 0.4)', // Dark background for ticks
        color: 'white', // White text for ticks
        beginAtZero: true,
        stepSize: 10 // Set step size for scale marks
      },
      suggestedMin: 0,
      suggestedMax: 100
    }
  },
  plugins: {
    tooltip: {
      titleColor: 'white', // Tooltip title in white
      bodyColor: 'white', // Tooltip body text in white
      backgroundColor: 'rgba(0, 0, 0, 0.8)' // Dark background for tooltips
    },
    legend: {
      labels: {
        color: 'white' // White text for legend
      }
    }
  }
};
