

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

document.getElementById('dashboard-button').addEventListener('click', function(){
    var createProperties = {
        url: 'dashboard.html'
    }
    chrome.tabs.create(createProperties, function(tab){});
});
  