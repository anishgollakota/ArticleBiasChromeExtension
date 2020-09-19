

//check if article
var curr_webpage = window.location.href

//send request to api to get article content
var api_key = "db0e7e9f0f30420fa4473eed886e32d3";
var scrapinghub_endpoint = "https://autoextract.scrapinghub.com/v1/extract";

fetch("https://www.vox.com/2020/9/18/20917757/justice-ginsburg-ruth-bader-ginsburg-dies", {
  method: "GET",
  mode: 'no-cors'
}).then(function(response){
  console.log("Vox: " + response);
});


let h = new Headers();
  h.set('Content-Type', 'application/json');
  h.set('Authorization', 'Basic ' + btoa(api_key) + ':');

  console.log('Basic ' + btoa(api_key + ':'))
  
  fetch(scrapinghub_endpoint, {
    method: 'POST',
    headers: h,
    body: 
      [
        {
          "url": curr_webpage,
          "pageType": "article"
        }
      ]
  }).then(function(response){
    console.log(response);
  }).catch((err)=>{
    console.log("error: " + err);
  });

// //send article body to ML backend


// //send message to popup to display bias score


// var isArticle = (url) => {



// }
