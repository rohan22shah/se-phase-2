$(document).ready(function(){
		$.getJSON('http://localho.st:5000/fetch',function(data){
		document.write(data);
	});
});