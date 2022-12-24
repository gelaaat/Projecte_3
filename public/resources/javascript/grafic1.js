const ctx1 = document.getElementById('canvasTemp1').getContext('2d');
const ctx2 = document.getElementById('canvasTemp2').getContext('2d');
const ctx3 = document.getElementById('canvasHum1').getContext('2d');

const mainTemperatura1 = () => {
    let firstURL = 'http://localhost:8000/temperatura/1/1h' 
    render(firstURL, ctx1);

    const select1 = document.querySelector('.temperaturaSelection1');
    
    select1.onchange = (event) => { 
        const interval = event.target.selectedOptions[0].value;
        let URL = `http://localhost:8000/temperatura/1/${interval || '1h'}`;
        updateChart('canvasTemp1');
        render(URL, ctx1);
    };

    
};

const mainTemperatura2 = () => {
    let firstURL = 'http://localhost:8000/temperatura/2/1h';
    
    render(firstURL, ctx2);

    const select2 = document.querySelector('.temperaturaSelection2');
    
    select2.onchange = (event) => { 
        const interval = event.target.selectedOptions[0].value;
        let URL = `http://localhost:8000/temperatura/2/${interval || '1h'}`;
        updateChart('canvasTemp2');
        render(URL, ctx2);
    };
}

const mainHumitat1 = () => {
    let firstURL = 'http://localhost:8000/humitat/1/1h' 
    render(firstURL, ctx3);
    const select3 = document.querySelector('.humitatSelection1');
    
    select3.onchange = (event) => { 
        const interval = event.target.selectedOptions[0].value;
        let URL = `http://localhost:8000/humitat/1/${interval || '1h'}`;
        updateChart('canvasHum1');
        render(URL, ctx3);
    };
};


const getData = async (URL) => {
    let data = [];
    await fetch(URL).then(success => {
        data = success.json();
    }).catch(err => {
        console.log('Algo va malament');
    });
    
    return data;
};

const render = async (URL, ctx) => {
    
    const data = await getData(URL);

    const intervalTemps = data.map( conjunt => {
        return Object.values(conjunt)[0];
    });

    const dades = data.map (conjunt => {
        return Object.values(conjunt)[1];
    });

    Chart.defaults.borderColor = '#FFFFFF80';
    Chart.defaults.color = 'white';
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: intervalTemps,
            datasets: [{
                data: dades,
                tension: 0.5,
                borderColor: 'rgb(148, 157, 224)',
                backgroundColor: 'rgb(148, 157, 224, 0.4)',
                fill: true
            }]
        },
        options:{
            plugins:{
                legend: {display: false}
            },
            responsive: true,
            scales:{
                y:{
                    min: 0
                }
            }
        }
    })
}

const updateChart = (chartId) => {
    const chart = Chart.getChart(chartId);
    chart.destroy();
};

mainTemperatura1();
mainTemperatura2();
mainHumitat1();