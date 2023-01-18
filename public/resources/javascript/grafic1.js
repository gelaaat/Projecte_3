const ctx1 = document.getElementById('canvasTemp1').getContext('2d');
const ctx2 = document.getElementById('canvasTemp2').getContext('2d');
const ctx3 = document.getElementById('canvasHum1').getContext('2d');
const ctx4 = document.getElementById('canvasHum2').getContext('2d');
const ctx5 = document.getElementById('canvasPress2').getContext('2d');
const IP='192.168.0.27'


const mainTemperatura1 = () => {
    let firstURL = `http://${IP}:8000/temperatura/1/1min`;
    //updateChart('canvasTemp1');
    render(firstURL, ctx1);

    const select1 = document.querySelector('.temperaturaSelection1');
    
    select1.onchange = (event) => { 
        const interval = event.target.selectedOptions[0].value;
        let URL = `http://${IP}:8000/temperatura/1/${interval || '1min'}`;
        updateChart('canvasTemp1');
        render(URL, ctx1);
    };

    
};

const mainTemperatura2 = () => {
    let firstURL = `http://${IP}:8000/temperatura/2/1min`;
    //updateChart('canvasTemp2');
    render(firstURL, ctx2);

    const select2 = document.querySelector('.temperaturaSelection2');
    
    select2.onchange = (event) => { 
        const interval = event.target.selectedOptions[0].value;
        let URL = `http://${IP}:8000/temperatura/2/${interval || '1min'}`;
        updateChart('canvasTemp2');
        render(URL, ctx2);
    };
}

const mainHumitat1 = () => {
    let firstURL = `http://${IP}:8000/humitat/1/1min`;
    //updateChart('canvasHum1'); 
    render(firstURL, ctx3);
    const select3 = document.querySelector('.humitatSelection1');
    
    select3.onchange = (event) => { 
        const interval = event.target.selectedOptions[0].value;
        let URL = `http://${IP}:8000/humitat/1/${interval || '1min'}`;
        updateChart('canvasHum1');
        render(URL, ctx3);
    };
};

const mainHumitat2 = () => {
    let firstURL = `http://${IP}:8000/humitat/2/1min`; 
    //updateChart('canvasHum2');
    render(firstURL, ctx4);
    const select4 = document.querySelector('.humitatSelection2');
    
    select4.onchange = (event) => { 
        const interval = event.target.selectedOptions[0].value;
        let URL = `http://${IP}:8000/humitat/2/${interval || '1min'}`;
        updateChart('canvasHum2');
        render(URL, ctx4);
    };
};

const mainPressio2 = () => {
    let firstURL = `http://${IP}:8000/pressio/2/1min`;
    //updateChart('canvasPress2'); 
    render(firstURL, ctx5, 950);
    const select5 = document.querySelector('.pressioSelection2');
    
    select5.onchange = (event) => { 
        const interval = event.target.selectedOptions[0].value;
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
            
            /*responsive: true,
            scales:{
                y:{
                    min: valor_min
                }
            }*/
        }
    })
}

const updateChart = (chartId) => {
    const chart = Chart.getChart(chartId);
    chart.destroy();
};


/*
setInterval(() => {
    mainTemperatura1();
    mainTemperatura2();
    mainHumitat1();
    mainHumitat2();
    mainPressio2();
}, 5000);
*/


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
    console.log('he refrescat')
}, 60000);