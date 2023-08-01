const ctx = document.getElementById('weather_chart');

const LABLES = document.querySelector('#js_labels').textContent
const DATA = document.querySelector('#js_data').textContent
const CITY = document.querySelector('td').textContent

new Chart(ctx, {
  type: 'line',
  data: {
    labels: JSON.parse(LABLES),
    datasets: [{
      label: `Температура в ${CITY}`,
      data: JSON.parse(DATA),
      borderWidth: 2,
      borderColor: 'rgb(82, 227, 227)'
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      }
    }
  }
});