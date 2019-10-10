function MatchesPerSeason() {
    let host = window.location.host
    fetch(`http://${host}/api/matches_per_season`)
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

function MatchesWon() {
    let host = window.location.host
    fetch(`http://${host}/api/matches_won`)
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

function ExtraRuns() {
    let host = window.location.host
    fetch(`http://${host}/api/extra_runs_conceded`)
        .then(response => response.json())
        .then((result) => {
            teams = result['teams'];
            extra_runs = result['extra_runs'];

            var chart = Highcharts.chart("container", {
                title: {
                    text: "Extra Runs per Team in 2016"
                },
                xAxis: {
                    title: {
                        text: "Teams"
                    },
                    categories: teams
                },
                yAxis: {
                    title: {
                        text: "Extra Runs"
                    }
                },
                series: [
                    {
                        type: "column",
                        name: "Runs",
                        colorByPoint: true,
                        data: extra_runs,
                        showInLegend: false
                    }
                ]
            });
        })
}


function BowlersEconomy() {
    let host = window.location.host
    fetch(`http://${host}/api/bowlers_economy`)
        .then(response => response.json())
        .then((result) => {
            bowlers = result['bowlers'];
            economies = result['economies'];

            var chart = Highcharts.chart("container", {
                title: {
                    text: "Top Economical Bowlers in 2015"
                },
                xAxis: {
                    title: {
                        text: "Bowlers"
                    },
                    categories: bowlers
                },
                yAxis: {
                    title: {
                        text: "Economy"
                    }
                },
                series: [
                    {
                        type: "column",
                        name: "Runs",
                        colorByPoint: true,
                        data: economies,
                        showInLegend: false
                    }
                ]
            });
        })
}