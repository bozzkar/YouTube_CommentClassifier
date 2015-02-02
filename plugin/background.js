var callbacks = [];

function getPageInfo(callback){
	callbacks.push(callback);
	chrome.tabs.executeScript(null,{file:'script.js'});
};

chrome.extension.onMessage.addListener(funtion(request){

	var callback = callbacks.shift();
	callback(request);
});
