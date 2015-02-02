// Information from the current page

var pageInfo = {
	"url": window.location.href
};

chrome.extension.sendRequest(pageInfo);
