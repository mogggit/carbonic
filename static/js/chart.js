$(window).resize(function(){
    drawChart();
});

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Type', 'kg of carbon'],
        ['Bus', 11],
        ['Car', 20],        
    ]);

    var options = {
        legend: {position: 'top', textStyle: {color: 'black', fontSize: 14}},
        tooltip: {textStyle: {color: 'gray', fontSize: 16}, showColorCode: true}
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));

    chart.draw(data, options);
}