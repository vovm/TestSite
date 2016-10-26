$(document).ready(function() {
    $("select").change(function () {
        var region_id;
        region_id = $("select option:selected").val();
        ShowMap(region_id)
    }).trigger("change");

    function ShowMap(region_id){
        $.ajax({
                type : "GET",
                url:"select_region",
                dataType:"json",
                data: {
                    region_pk: region_id
                },
                success:function(data){

                    var processed_json = new Array();

                    for (var i = 0; i < data.length; i++){
                        processed_json.push([data[i].district_name, data[i].district_value]);
                    }

                    $('#chart_container').highcharts({
                        chart: {
                            type: "column"
                        },
                        title: {
                            text: $("select option:selected").text()
                        },
                        xAxis: {
                            type: 'category',
                            allowDecimals: false,
                            title: {
                                text: ""
                            }
                        },
                        yAxis: {
                            title: {
                                text: "Values"
                            }
                        },
                        series: [{
                            name: 'Districts (Cities)',
                            data: processed_json
                        }]

                    });

                }
            });
    }
});