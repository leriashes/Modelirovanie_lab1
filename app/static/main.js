if (window.jQuery) {
    var vJq = jQuery.fn.jquery;
    console.log(vJq);
}
else {
    console.log(123);
}

$(document).ready(function(){
    $('#drawGraph').click(function(e)
    {
        e.preventDefault();
        $.ajax({
            url: '',
            type: 'get',
            contenType: 'application/json',
            data: {
                button_text: $(this).text(),
            },
            /*success: function(){ // если запрос успешен вызываем функцию
                $('#drawGraph').style.visible(); // добавляем текст в элемент с классом .myClass
            },*/
            success: function(response){
               // $('#drawGraph').text(response.secs + 123);
                let a = document.querySelector('#cardChart1');
                a.style.display = 'block';


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