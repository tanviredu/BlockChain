let person1 = {
	name:"john",age:22
}

let person2 = {
	name:'Mary',age:26
}

let sayHi = function(message){
	console.log(message +" "+ this.name);
}

sayHi.call(person1,"Hi");
sayHi.call(person2,"Hi");