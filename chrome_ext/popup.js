

console.log("in popup");

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, {request: 'selection'}, function(data) {
        console.log(data.response);
        //send to backend



    });
  });

chrome.storage.local.get(['score'], function(data){
    if(data.score != undefined){
        document.getElementById('resultsRequest').innerHTML = data.score;
    }
    
})

chrome.storage.local.get(['url_list'], function(data){
    var scores = [];
    if(data.url_list != undefined){
        for( url of data.url_list){
            chrome.storage.local.get([urlData], function(data){
                scores.push(data.urlData.score);
            })
        }
    }

    fetch("http://localhost:5000/plotHistory", 
        {
            method: 'POST',
            headers:
            {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              'hist': scores
            })
    }).then(function(data){
        //img
        console.log(data);
    });
})

document.getElementById('dashboard-button').addEventListener('click', function(){
    var createProperties = {
        url: 'dashboard.html'
    }
    chrome.tabs.create(createProperties, function(tab){});
});
  