//make request for graph
fetch('', { method: 'GET' }).then(function(graph){
    document.getElementById('graph').innerHTML = 'hi'
});


//generate table
chrome.storage.local.get(['get_list'], function(data){
    var list = data.get_list == undefined ? [] : data.get_list;
    console.log(list);
    var tableHTML = "<p>"
    for (item of list){
        tableHTML += `item`;
    }
    tableHTML += '</p>';
    console.log(tableHTML);
})
