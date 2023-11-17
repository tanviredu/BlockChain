function greet(message, ... names){
	console.log(...names);
	names.forEach( function(element, index) {
		console.log(message+ " "+ element);
	});
}


greet("welcome","Tanvir","Rahman","Ornob");