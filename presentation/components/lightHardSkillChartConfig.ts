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
      backgroundColor: 'rgba(54, 162, 235, 0.2)', // Light blue with low opacity
      borderColor: 'rgb(54, 162, 235)', // Solid blue outline
      pointBackgroundColor: 'rgb(54, 162, 235)', // Blue for points
      pointBorderColor: '#000', // Black for point borders
      pointHoverBackgroundColor: '#fff', // White for hover
      pointHoverBorderColor: 'rgb(54, 162, 235)', // Blue for hover borders
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
        color: 'rgba(0, 0, 0, 0.1)', // Dark grid lines for contrast
      },
      angleLines: {
        color: 'rgba(0, 0, 0, 0.2)' // Darker lines for angle lines
      },
      pointLabels: {
        font: {
          size: 14
        },
        color: 'rgba(0, 0, 0, 0.7)' // Dark grey for labels
      },
      ticks: {
        backdropColor: 'rgba(255, 255, 255, 0.8)', // Light background for ticks
        color: 'black', // Black text for ticks
        beginAtZero: true,
        stepSize: 10 // Set step size for scale marks
      },
      suggestedMin: 0,
      suggestedMax: 100
    }
  },
  plugins: {
    tooltip: {
      titleColor: 'black', // Tooltip title in black
      bodyColor: 'black', // Tooltip body text in black
      backgroundColor: 'rgba(255, 255, 255, 0.9)' // Light background for tooltips
    },
    legend: {
      labels: {
        color: 'black' // Black text for legend
      }
    }
  }
};
