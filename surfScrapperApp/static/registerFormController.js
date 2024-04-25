
function init() {

    selectBox = $('#Selector')
    let data = [{'display':'dupa', 'value':'dupa'}, {'display':'dupa1', 'value':'dupa1'}, {'display':'dupa2', 'value':'dupa2'}]
    if (data.length > 0) {
        var output = [];
        $.each(data, function (i, dat) {
            debugger
            output.push(`<option value=${dat.value}> ${dat.display} </option>`);
        });
        selectBox.html(output.join("")); // ... on the original element
        selectBox.selectpicker("refresh"); // refresh the options
    }
}

async function myFunction(event) {
    let apiCallResponse = await fetch("http://127.0.0.1:8000/api/submit_subscriber_form", {
          method: "POST",
          body: JSON.stringify({
            userEmail: 'test@test',
            trackedBeaches: JSON.stringify($('.selectpicker').val()),
          }),
            credentials: "same-origin",
            headers: {
              "X-CSRFToken": getCookie("csrftoken"),
              "Accept": "application/json",
              'Content-Type': 'application/json'
            },
        })

    if(apiCallResponse.status == 201) {
        let apiCallParsedResponse = await apiCallResponse.json();
        var toastElList = [].slice.call(document.querySelectorAll('.toast'))
          var toastList = toastElList.map(function(toastEl) {
            return new bootstrap.Toast(toastEl)
          })
          toastList.forEach(toast => toast.show())
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

init();