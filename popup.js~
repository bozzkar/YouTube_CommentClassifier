// Post the data to server

function postVideoID(videoID)
{

	/*var postURL = 'ycc';
	var xhr = new XMLHttpRequest();
	xhr.open('GET','http://localhost:8080/ycc/plugin.jsp',true);
	xhr.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
	xhr.send('?videoID='+ videoID);
	document.write(xhr.responseText);*/
	 $(document).ready(function(){
       
       $.get("http://localhost:8080/ycc/plugin.jsp?videoID="+videoID,function(data,status){
           $('#pluginContent').html(data);
         });
});
}

function testURL(tabs)
{
	var videoURL = tabs[0].url;
	var isYouTube = videoURL.search('youtube.com');
	if(isYouTube == -1){document.write("Not an YouTube url");}
	else{
	 var videoID = videoURL.split('v=')[1];
	 postVideoID(videoID);	
	}	

}


function queryURL(){
	
	event.preventDefault();
	chrome.tabs.query({active: true,'windowId': chrome.windows.WINDOW_ID_CURRENT},
			 function(tabs) {
				testURL(tabs)			
    			});	
}

// Run our script as soon as the document's DOM is ready.
window.addEventListener('load', function (evt) {
	//chrome.extension.getBackgroundPage().getPageInfo(onPageInfo);
	//videoURL = document.location.href;
	queryURL();
	
});
