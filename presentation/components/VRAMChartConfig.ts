export const data = {
  labels: [
    '2GB',
    '3GB',
    '4GB',
    '6GB',
    '8GB',
    '12GB',
    '16GB',
    '24GB+'
  ],
  datasets: [
    {
      label: 'Steam Users (%)',
      backgroundColor: [
        'rgba(255, 99, 132, 0.7)',
        'rgba(54, 162, 235, 0.7)',
        'rgba(255, 205, 86, 0.7)',
        'rgba(75, 192, 192, 0.7)',
        'rgba(153, 102, 255, 0.7)',
        'rgba(255, 159, 64, 0.7)',
        'rgba(199, 199, 199, 0.7)',
        'rgba(83, 102, 255, 0.7)'
      ],
      borderColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)',
        'rgb(75, 192, 192)',
        'rgb(153, 102, 255)',
        'rgb(255, 159, 64)',
        'rgb(199, 199, 199)',
        'rgb(83, 102, 255)'
      ],
      borderWidth: 2,
      data: [8.2, 5.1, 18.4, 12.8, 33.7, 19.2, 2.1, 0.5]
    }
  ]
};

export const options = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    title: {
      display: true,
      text: 'VRAM Distribution Among Steam Users (2025)',
      font: {
        size: 20,
        weight: 'bold'
      },
      color: 'rgba(0, 0, 0, 0.8)'
    },
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: function(context: any) {
          return `${context.label}: ${context.parsed.y}% of users`;
        }
      }
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      max: 40,
      ticks: {
        callback: function(value: any) {
          return value + '%';
        },
        font: {
          size: 12
        },
        color: 'rgba(0, 0, 0, 0.7)'
      },
      title: {
        display: true,
        text: 'Percentage of Users',
        font: {
          size: 14,
          weight: 'bold'
        },
        color: 'rgba(0, 0, 0, 0.8)'
      },
      grid: {
        color: 'rgba(0, 0, 0, 0.1)'
      }
    },
    x: {
      ticks: {
        font: {
          size: 12
        },
        color: 'rgba(0, 0, 0, 0.7)'
      },
      title: {
        display: true,
        text: 'VRAM Amount',
        font: {
          size: 14,
          weight: 'bold'
        },
        color: 'rgba(0, 0, 0, 0.8)'
      },
      grid: {
        display: false
      }
    }
  }
};
