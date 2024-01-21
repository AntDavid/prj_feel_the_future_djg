
src="https://cdn.jsdelivr.net/npm/chart.js"


    const ctx = document.getElementById('grafico1');

    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Acertos', 'Erros'],
        datasets: [{
          label: 'Qtd',
          data: [10, 5],
          borderWidth: 1
        }]
      },

    });




    const ctx2 = document.getElementById('grafico2');

    new Chart(ctx2, {
      type: 'radar',
      data: {
        labels: ['Matemática', 'Português', 'Programação', 'História'],
        datasets: [{
          label: 'Qtd',
          data: [2, 4, 8, 10],
          borderWidth: 1,
          fill: true,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgb(255, 99, 132)',
          pointBackgroundColor: 'rgb(255, 99, 132)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgb(255, 99, 132)'
        }]
      },

    });


