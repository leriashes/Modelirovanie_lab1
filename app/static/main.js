if (window.jQuery) {
    var vJq = jQuery.fn.jquery;
    console.log(vJq);
}
else {
    console.log(123);
}

values = [];

$(document).ready(function(){
    $('#drawGraph').click(function(e)
    {
        e.preventDefault();

        values = [];
        let cells = document.querySelectorAll('.form-control')

        for(let i = 0; i < cells.length; i++)
        {
            values.push({val : cells[i].value});
        }

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_text: $(this).text(),
                cells_values: JSON.stringify(values),
            },
            success: function(response){
                //$('#drawGraph').text(response.secs + 123);
                
                
                /*let cells = document.querySelectorAll('.form-control')
                //$('#drawGraph').text(cells.length + 1);
                let k = 0;
                for(let i = 0; i < cells.length; i++)
                {
                    let count = 0;

                    for(let j = 0; j < cells[i].value.length; j++)
                    {
                        if (cells[i].value[j] >= '0' && cells[i].value[j] <= '9')
                        {
                            count++;
                        }
                        else
                        {
                            break;
                        }
                    }

                    //$('#findDecision').text(count);

                    if (count < cells[i].value.length || cells[i].value.length == 0 || cells[i].value.length == 1 && cells[i].value[0] == '0')
                    {
                        cells[i].style.backgroundColor = "#ea9999";
                    }
                    else
                    {
                        cells[i].style.backgroundColor = "#ffffff";
                        k++;
                    }

                }

                //$('#drawGraph').text(k);
                */
                
                if (response.bad.length != 0)
                {
                    bad_val = response.bad.split(' ');
                    
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

                    let a = document.querySelector('#cardChart1');
                    a.style.display = 'block';
                }
                /*if (k < cells.length)
                {
                    //$('#drawGraph').text('Всё плохо');
                }
                else
                {
                    //$('#drawGraph').text(k);
                    /*if (cells[0].value == '1')
                    {
                        $('#findDecision').text(45);
                    }
                    else
                    {
                        $('#findDecision').text(cells[0].value);
                    }
                    //$('#drawGraph').text(k);*/

                   /* let a = document.querySelector('#cardChart1');
                    a.style.display = 'block';
                }*/
                


            }
            
        })
    })

    $('#findDecision').click(function()
    {
        $.ajax({
            url: '',
            type: 'get',
            contenType: 'application/json',
            data: {
                button_text: $(this).text(),
            },
            success: function(response){
                let a = document.querySelector('#cardChart2');
                a.style.display = 'block';

                let b = document.querySelector('#cardChart2');
                b.style.display = 'block';
            }
        })
    })
}
)