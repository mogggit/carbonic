function drawPieChart(aryChartData, aryColors) {
    // 圓餅圖
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        // 新增欄位
        aryChartData.unshift(['公司', '佔比']);
        var data = google.visualization.arrayToDataTable(aryChartData);
        var options = {
            // title: '資產總覽',
            colors: aryColors,
            legend: {position: 'top', textStyle: {color: 'black', fontSize: 14}},
            tooltip: {textStyle: {color: 'gray', fontSize: 16}, showColorCode: true}
        };
        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(data, options);
        // 移除欄位，否則影響長條圖
        aryChartData.shift();
    }
}