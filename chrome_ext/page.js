

//check if article
var curr_webpage = window.location.href

//send request to api to get article content
var api_key = "db0e7e9f0f30420fa4473eed886e32d3";
var scrapinghub_endpoint = "https://autoextract.scrapinghub.com/v1/extract";


fetch("http://localhost:3000/getArticleInfo", {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "webpage": curr_webpage
  })
}).then(function(response){

  return response.json().then(function(data){
    
    var article_body = data[0]['article']['articleBody'];
    var headline = data[0]['article']['headline'];
    console.log(article_body);
    console.log(headline);

    // send article body to flask backend
    if(article_body != undefined){
      /*
      fetch("http://localhost:3000/getScore", {
        method: 'POST',
        headers:
        {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          'article': article_body
        })
      }).then(function(data){
        
        console.log(data);

        //display
      })
      */

      fetch("http://localhost:5000/getScore", {
        method: 'POST',
        headers:
        {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          'article': article_body
        })
      }).then(function(response){

        return response.json().then(function(data){
          console.log(data);
        //display
      })
    });
  }

    /*
    fetch("http://localhost:5000/getScore", {method: 'GET' })
      .then(function(data){
        console.log(data)
    })

    fetch("http://localhost:5000/isFakeNews", {method: 'GET' }).then(function(data){
      console.log(data)
    })
    */

    //storing data
    chrome.storage.local.get(['url_list'], function(list){
      console.log("list");
      console.log(list.url_list);

      var new_list = list.url_list == undefined ? [] : list.url_list;
      new_list.push(curr_webpage)
      chrome.storage.local.set({'url_list': new_list}, function(){})
    })
    
    var score = 0;
    chrome.storage.local.set({ curr_webpage: {"body": article_body, "headline": headline, "pb": score} }, function(){});


    


    //send message to popup to display bias score


  })




})


chrome.runtime.onMessage.addListener(function(message, sender, sendResponse){

  if(message.request == "selection"){
      console.log(window.getSelection().toString());
      sendResponse({response: window.getSelection().toString()});
  }
  else if(message.request == "get_list"){
    chrome.storage.local.get(['url_list'], function(result) {
      var dict = [];
      for (url of result.url_list){
        chrome.storage.local.get([url], function(url_result) {
          dict.append(url_result.url);
        });
      }
      sendResponse({response: dict});
    });
  }
  else{
      console.log("bruh");
  }
})

