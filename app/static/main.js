function get_values()
{
    values = [];
    let cells = document.querySelectorAll('.form-control')

    for(let i = 0; i < cells.length; i++)
    {
        values.push({val : cells[i].value});
    }

    return values;
}

function bad_values(bad)
{
    result = (bad.length != 0);
    let cells = document.querySelectorAll('.form-control');

    if (result)
    {
        bad_val = bad.split(' ');

        j = 0;
        for (i = 0; i < cells.length; i++)
        {
            k = parseInt(bad_val[j]);

            if (k == i)
            {
                cells[i].style.backgroundColor = "#ea9999";
                j++;
            }
            else
            {
                cells[i].style.backgroundColor = "#ffffff";
            }
            
        }
    }
    else
    {
        for (i = 0; i < cells.length; i++)
        {
            cells[i].style.backgroundColor = "#ffffff";
        }
    }
    
    return result;
}

function draw_graph(s, xs, ys, T, values, table_number)
{
    var data = [];
    var colors = ['rgba(237, 178, 81, 0.6)', 'rgba(187, 247, 116, 0.6)', 'rgba(103, 224, 224, 0.6)', 'rgba(152, 101, 247, 0.6)', 'rgba(239, 141, 131, 0.6)', 'rgba(23, 53, 110, 0.4)', 'rgba(13, 43, 100, 0.4)'];
    var numbers = '₁₂₃₄₅';

    len = values.length;
    step = 2;

    if (ys != null)
    {
        step = 3;
    }

    /*if (table_number == 2)
    {
        len -= 5;
    }*/
   //$('#findDecision').text(values);

    for (i = 0; i < len; i += step)
    {
        xz = [parseInt(values[i + 1]), parseInt(values[i])];
        yz = ['B', 'A'];

        if (step == 3)
        {
            data.push({
                x: [parseInt(ys[i / step])],
                y: ['C'],
                name: 'y' + numbers[i / step],
                orientation: 'h',
                width: 0.5,
                marker: {
                    color: colors[6],
                    width: 1
                },
                type: 'bar',
                showlegend: false,
            });

            xz = [parseInt(values[i + 2])].concat(xz)
            yz = ['C'].concat(yz)
        }


        data.push({
            x: [parseInt(xs[i / step])],
            y: ['B'],
            name: 'x' + numbers[i / step],
            orientation: 'h',
            width: 0.5,
            marker: {
                color: colors[5],
                width: 1
            },
            type: 'bar',
            showlegend: false,
        });

        name_str = (i / (step) + 1).toString();

        

        if (table_number == 2)
        {
            name_str += '(' + s[i / (step)].toString() + ')';
        }

        data.push({
            x: xz,
            y: yz,
            name: name_str,
            orientation: 'h',
            width: 0.5,
            marker: {
                color: colors[s[i / step] - 1],
                width: 1
            },
            type: 'bar'
        });

    }

    
    data.push({
        x: [0],
        y: ['B'],
        name: 'xᵢ',
        orientation: 'h',
        width: 0.5,
        marker: {
          color: 'rgba(23, 53, 110, 0.8)',
          width: 1
        },
        type: 'bar',
        visible: 'legendonly'
    }); 

    
    if (step == 3)
    {
        data.push({
            x: [0],
            y: ['C'],
            name: 'yᵢ',
            orientation: 'h',
            width: 0.5,
            marker: {
                color: 'rgba(13, 43, 100, 0.8)',
                width: 1
            },
            type: 'bar',
            visible: 'legendonly'
        });
    }

       

    t = parseInt(T / 45) + 1
    
    var layout = {
    title: 'График Ганта',
    barmode: 'stack',
    legend:
    {
        traceorder: 'normal'
    },
    xaxis: {
        dtick: t,
        showline: true
    },
    /*annotations: [{
        text: 't',
        x: 45,
        y: -1,
        textposition: 'bottom left',
        width: 0.5,
        ax: -4000,
        ay: 0,
        showarrow: true
    }]*/
    };
    
    Plotly.newPlot("chart" + table_number.toString(), data, layout);

}

$(document).ready(function(){
    $('#drawGraph').click(function(e)
    {
        e.preventDefault();

        table_values = get_values();

        let cells = document.querySelectorAll('.form-control')

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                action: 'draw',
                cells_values: JSON.stringify(table_values),
            },

            success: function(response){

                if (!bad_values(response.bad))
                {
                    //var graph1 = response.graphikJSON;
                    //Plotly.plot("chart1", graph1, {});
                    values = []
                    
                    for(i = 0; i < cells.length; i++)
                    {
                        values.push(cells[i].value)
                    }

                    if (response.mas_y == null)
                    {
                        draw_graph([1, 2, 3, 4, 5], response.mas_x.split(' '), null, response.T, values, 1);
                    }
                    else
                    {
                        draw_graph([1, 2, 3, 4, 5], response.mas_x.split(' '), response.mas_y.split(' '), response.T, values, 1);
                    }

                    /*var data = [];
                    var colors = ['rgba(237, 178, 81, 0.6)', 'rgba(187, 247, 116, 0.6)', 'rgba(103, 224, 224, 0.6)', 'rgba(152, 101, 247, 0.6)', 'rgba(239, 141, 131, 0.6)', 'rgba(23, 53, 110, 0.4)'];
                    var numbers = '₁₂₃₄₅';
                    
                    var xs = response.x_start.split(' ');

                    

                    for (i = 0; i < cells.length; i += 2)
                    {
                        data.push({
                            x: [parseInt(xs[i / 2])],
                            y: ['B'],
                            name: 'x' + numbers[i / 2],
                            orientation: 'h',
                            width: 0.5,
                            marker: {
                              color: colors[5],
                              width: 1
                            },
                            type: 'bar',
                            showlegend: false,
                        });

                        data.push({
                            x: [parseInt(cells[i + 1].value), parseInt(cells[i].value)],
                            y: ['B', 'A'],
                            name: (i /2 + 1).toString(),
                            orientation: 'h',
                            width: 0.5,
                            marker: {
                              color: colors[i / 2],
                              width: 1
                            },
                            type: 'bar'
                        });

                    }
                      
                    data.push({
                        x: [0],
                        y: ['B'],
                        name: 'xᵢ',
                        orientation: 'h',
                        width: 0.5,
                        marker: {
                          color: 'rgba(23, 53, 110, 0.8)',
                          width: 1
                        },
                        type: 'bar',
                        visible: 'legendonly'
                    });


                      t = parseInt(response.T / 45) + 1
                      
                      var layout = {
                        title: 'График Ганта',
                        barmode: 'stack',
                        legend:
                        {
                            traceorder: 'normal'
                        },
                        xaxis: {
                            dtick: t,
                            showline: true
                        },
                        /*annotations: [{
                            text: 't',
                            x: 45,
                            y: -1,
                            textposition: 'bottom left',
                            width: 0.5,
                            ax: -4000,
                            ay: 0,
                            showarrow: true
                        }]*/
                      /*};
                      
                      Plotly.newPlot("chart1", data, layout);*/

                    let a = document.querySelector('#cardChart1');
                    a.style.display = 'block';
                }


            }
            
        })
    })

    $('#findDecision').click(function(e)
    {
        e.preventDefault();
        
        table_values = get_values();
        
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                action: 'find',
                cells_values: JSON.stringify(table_values)
            },
            success: function(response){
                
                if (!bad_values(response.bad))
                {
                    let cells = document.querySelectorAll('.res-cell1');
                    var res = response.res.split(' ');
                    let s = [];

                    let n = res.length / 5;
                    values = []

                    for(i = 0; i < cells.length; i++)
                    {
                        if (i % n == 0)
                        {
                            s.push(parseInt(res[i]));
                        }
                        else
                        {
                            values.push(res[i])
                        }

                        cells[i].innerHTML = res[i];
                    }


                    //$('#findDecision').text(response.mas_y.split(' '));


                    if (response.mas_y == null)
                    {
                        draw_graph(s, response.mas_x.split(' '), null, response.T, values, 2);
                    }
                    else
                    {
                        draw_graph(s, response.mas_x.split(' '), response.mas_y.split(' '), response.T, values, 2);
                    }

                    let a = document.querySelector('#cardChart2');
                    a.style.display = 'block';
                }
            }
        })
    })
}
)