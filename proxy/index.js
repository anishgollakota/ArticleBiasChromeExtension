const express = require('express');
const request = require('request');
const https = require('https');
const fetch = require('node-fetch');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

const api_key = "db0e7e9f0f30420fa4473eed886e32d3";
const scrapinghub_endpoint = "https://autoextract.scrapinghub.com/v1/extract";

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    next();
});

app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/getArticleInfo', async (req, res) => {
    console.log(req.body["webpage"]);
    
    const options = {
        hostname: "autoextract.scrapinghub.com",
        path: '/v1/extract',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Basic ZGIwZTdlOWYwZjMwNDIwZmE0NDczZWVkODg2ZTMyZDM6'
        }
    };

    const articleInfo = https.request(options, r => {
        console.log(`statusCode: ${r.statusCode}`)


            var body = '';
            r.on('data', function (chunk) {
                console.log('CHUNK: ' + chunk);
              body += chunk;
            });
            r.on('end', function () {
              console.log('BODY: ' + body);

              res.json(JSON.parse(body));
            });

    });


    articleInfo.on('error', error=>{
        console.log(error);
    })

    
    var body =  JSON.stringify([
        {"url": req.body["webpage"],
        "pageType": "article"
        }
    ])
    
    articleInfo.write(body);
    articleInfo.end();

})

app.get('/hi', (req, res)=>{
    console.log("hi");
    res.json({'hi': 'hi'})
})


app.listen(3000,  () => console.log(`listening on 3000`))