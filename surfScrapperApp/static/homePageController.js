
async function init() {
    let data = await callForBestSpots();
    dataForHtml = ''
    data.forEach((beach, index) => {
        let beachName = beach.fields.name
        let beachNameToReplace = `Beach: ${beachName} <br/>`
        dataForHtml = `${dataForHtml} ${buildBootstrapCard(beachName, beach.fields.textForHtml.replaceAll(beachNameToReplace,''), index+1)}`
    })
    const element = document.getElementById('forecastData')
        element.innerHTML = dataForHtml;
        element.outerHtml = dataForHtml;
        element.html = dataForHtml;

}

async function callForBestSpots() {
    let apiCallResponse = await fetch("/api/get_best_spots_for_today", {
            method: "GET",
            credentials: "same-origin",
            headers: {
              "X-CSRFToken": getCookie("csrftoken"),
              "Accept": "application/json",
              'Content-Type': 'application/json'
            },
        })
    let apiCallParsedResponse = await apiCallResponse.json();
    if(apiCallResponse.status == 200) {
        return JSON.parse(apiCallParsedResponse.beach_data_from_db)
    }
    return []
}

function buildBootstrapCard(beachName, ratingData, position) {

    return `<div class="card" style="width: 20rem; margin:10px">
        <div class="card-body">
            <h5 class="card-title" style="text-align: center">Beach ${beachName}</h5>
            <h6 class="card-subtitle mb-2 text-muted" style="text-align: center">Postion in ranking: ${position}</h6>
            <p class="card-text" style="text-align: center">${ratingData}</p>
        </div>
    </div>`
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