
console.log("in popup");

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, {request: 'selection'}, function(data) {
        console.log(data.response);
        //send to backend



    });
  });

chrome.storage.local.get(['score', 'fake_news_score'], function(data){
    if(data.score != undefined){
        console.log("in storage thing");
        var rating = "";
        var color = "";
        if(data.score > 0.7){
            rating = "Strongly Conservative";
            color = '#ff0000';
        }
        else if(data.score > 0.5){
            rating = "Mildly Conservative";
            color = '#FFCCCB';
        }
        else if(data.score > 0.3){
            rating = "Mildly Liberal";
            color = '#87CEEB';
        }else{
            rating = "Strongly Liberal";
            color = '#0000ff';
        }
  
        document.getElementById('resultsRequest').innerHTML = '<p style ="fontcolor:' + color + '">' + rating + '</p>';
        document.getElementById('resultsRequest').style.color = color
    }
    if(data.fake_news_score != undefined){
        document.getElementById('resultsConnect').innerHTML = data.fake_news_score;
    }
})

chrome.storage.local.get(['url_list'], function(data){
    console.log(data.url_list);
    var scores = [];
    if(data.url_list != undefined){
        for( url of data.url_list){
            chrome.storage.local.get([url], function(data){
                scores.push(data.url.score);
            })
        }
    }

    console.log(scores);

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
  