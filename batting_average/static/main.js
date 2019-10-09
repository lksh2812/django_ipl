function PlotFirst() {
    let host = window.location.host
    fetch(`http://${host}/ipl/api/first/`)
        .then(response => response.json())
        .then((result) => {
            seasons = result['seasons'];
            matches = result['matches'];

            var chart = Highcharts.chart("container", {
                title: {
                    text: "Matches per Season"
                },
                subtitle: {
                    text: "IPL Data"
                },
                xAxis: {
                    title: {
                        text: "Seasons"
                    },
                    categories: seasons
                },
                yAxis: {
                    title: {
                        text: "Match played"
                    }
                },
                series: [
                    {
                        type: "column",
                        name: "Matches",
                        colorByPoint: true,
                        data: matches,
                        showInLegend: false
                    }
                ]
            });
        })
}

function PlotSecond() {
    let host = window.location.host
    fetch(`http://${host}/ipl/api/second/`)
        .then(response => response.json())
        .then((result) => {
            seasons = result['season'];
            team_data = result['team_data'];

            var chart = Highcharts.chart("container", {
                chart: {
                    type: 'bar'
                },
                title: {
                    text: "Matches per Season"
                },
                subtitle: {
                    text: "IPL Data"
                },
                xAxis: {
                    title: {
                        text: "Seasons"
                    },
                    categories: seasons
                },
                yAxis: {
                    title: {
                        text: "Match Win"
                    }
                },
                legend: {
                    reversed: true
                },
                plotOptions: {
                    series: {
                        stacking: 'normal'
                    }
                },
                series:team_data
            });
        })
}