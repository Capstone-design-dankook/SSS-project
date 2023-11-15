const ctx = document.getElementById('myChart');
    const population = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['00~06', '06~11', '11~14', '14~17', '17~21', '21~24'],
            datasets: [{
                label: '시간대별 유동인구',
                data: [{{ data_00_06 }}, {{ data_06_11 }}, {{ data_11_14 }}, {{ data_14_17 }}, {{ data_17_21 }}, {{ data_21_24 }}],
                backgroundColor: 'skyblue',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                     beginAtZero: true
                }
            }
        }
    });