let message = {
	name:"John",
	regularFunction:function(){
		console.log(this);
		console.log("Hello "+this.name);
	},
	arrowFunction: ()=>{
		console.log("Hi "+ this.name);
	}
}

message.regularFunction();
message.arrowFunction();