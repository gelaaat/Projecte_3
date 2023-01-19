const ctx1 = document.getElementById('canvasTemp1').getContext('2d');
const ctx2 = document.getElementById('canvasTemp2').getContext('2d');
const ctx3 = document.getElementById('canvasHum1').getContext('2d');
const ctx4 = document.getElementById('canvasHum2').getContext('2d');
const ctx5 = document.getElementById('canvasPress2').getContext('2d');

const IP='192.168.0.27'


const mainTemperatura1 = () => {
    const select1 = document.querySelector('.temperaturaSelection1');
    let interval = select1.selectedOptions[0].value;
    
    let firstURL = `http://${IP}:8000/temperatura/1/${interval}`;
    render(firstURL, ctx1);

    select1.onchange = (event) => { 
        interval = event.target.selectedOptions[0].value;
        let URL = `http://${IP}:8000/temperatura/1/${interval || '1min'}`;
        updateChart('canvasTemp1');
        render(URL, ctx1);
    };

    

    
};

const mainTemperatura2 = () => {
    const select2 = document.querySelector('.temperaturaSelection2');
    let interval = select2.selectedOptions[0].value;
    
    let firstURL = `http://${IP}:8000/temperatura/2/${interval}`;
    render(firstURL, ctx2);
    
    select2.onchange = (event) => { 
        interval = event.target.selectedOptions[0].value;
        let URL = `http://${IP}:8000/temperatura/2/${interval || '1min'}`;
        updateChart('canvasTemp2');
        render(URL, ctx2);
    };
}

const mainHumitat1 = () => {
    const select3 = document.querySelector('.humitatSelection1');
    let interval = select3.selectedOptions[0].value;

    let firstURL = `http://${IP}:8000/humitat/1/${interval}`;
    render(firstURL, ctx3);
    
    
    select3.onchange = (event) => { 
        interval = event.target.selectedOptions[0].value;
        let URL = `http://${IP}:8000/humitat/1/${interval || '1min'}`;
        updateChart('canvasHum1');
        render(URL, ctx3);
    };
};

const mainHumitat2 = () => {
    const select4 = document.querySelector('.humitatSelection2');
    let interval = select4.selectedOptions[0].value;

    let firstURL = `http://${IP}:8000/humitat/2/${interval}`; 
    render(firstURL, ctx4);
    
    
    select4.onchange = (event) => { 
        interval = event.target.selectedOptions[0].value;
        let URL = `http://${IP}:8000/humitat/2/${interval || '1min'}`;
        updateChart('canvasHum2');
        render(URL, ctx4);
    };
};

const mainPressio2 = () => {
    const select5 = document.querySelector('.pressioSelection2');
    let interval = select5.selectedOptions[0].value;

    let firstURL = `http://${IP}:8000/pressio/2/${interval}`;
    render(firstURL, ctx5, 950);
    
    
    select5.onchange = (event) => { 
        interval = event.target.selectedOptions[0].value;
        let URL = `http://${IP}:8000/pressio/2/${interval || '1min'}`;
        updateChart('canvasPress2');
        render(URL, ctx5, 950);
    };
};

const mainGaratge = async () => {
    let URL = `http://${IP}:8000/portagaratge/3`;
    let divEstatGaratge = document.getElementById('estat-porta');
    let estatActual = await getData(URL);
    divEstatGaratge.innerText = estatActual[0].estat;
};

const getData = async (URL) => {
    let data;
    await fetch(URL).then(success => {
        data = success.json();
    }).catch(err => {
        console.log('Algo va malament');
    });
    
    return data;
};

const render = async (URL, ctx, valor_min = 0) => {
    
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
            
        }
    })
}

const updateChart = (chartId) => {
    const chart = Chart.getChart(chartId);
    chart.destroy();
};


setInterval(() => {
    mainGaratge();
}, 5000);

mainTemperatura1();
mainTemperatura2();
mainHumitat1();
mainHumitat2();
mainPressio2();

setInterval(() => {
    updateChart('canvasTemp1');
    mainTemperatura1();
    updateChart('canvasTemp2');
    mainTemperatura2();
    updateChart('canvasHum1');
    mainHumitat1();
    updateChart('canvasHum2');
    mainHumitat2();
    updateChart('canvasPress2');
    mainPressio2();
}, 60000);