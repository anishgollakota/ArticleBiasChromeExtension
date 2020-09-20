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

    // send article body to ML backend


    //send message to popup to display bias score


  })




})





