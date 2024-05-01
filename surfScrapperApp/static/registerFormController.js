
async function init() {
    let data = await callForBeachNames();
    selectBox = $('#Selector')
    if (data.length > 0) {
        var output = [];
        $.each(data, function (i, dat) {
            output.push(`<option value=${dat}> ${dat} </option>`);
        });
        selectBox.html(output.join(""));
        selectBox.selectpicker("refresh");
        return true
    }
    return false
}

async function callForBeachNames() {
    let apiCallResponse = await fetch("http://127.0.0.1:8000/api/get_available_beaches", {
            method: "GET",
            credentials: "same-origin",
            headers: {
              "X-CSRFToken": getCookie("csrftoken"),
              "Accept": "application/json",
              'Content-Type': 'application/json'
            },
        })
    if(apiCallResponse.status == 200) {
        let apiCallParsedResponse = await apiCallResponse.json();
        return apiCallParsedResponse.beach_names
    }
    return []
}

async function submitForm(event) {

    debugger
    let trackedBeaches = ''
    $('.selectpicker').val().forEach( (element, index) => {
    debugger
        if(index == 0) {
            trackedBeaches = element
        } else {
            trackedBeaches = `${trackedBeaches},${element}`
        }
    })
    trackedBeaches
    let apiCallResponse = await fetch("http://127.0.0.1:8000/api/submit_subscriber_form", {
          method: "POST",
          body: JSON.stringify({
            userEmail: $('#emailInput').val(),
            trackedBeaches: trackedBeaches,
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

let alreadyInited = false;
if(!alreadyInited) {
    alreadyInited = init();
}