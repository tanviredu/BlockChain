let person1 = {
	name:"mary",
	get_name: function(){
		return this.name;
	}
};

let person2 = {name:'John'};

let getName = person1.get_name.bind(person2);
console.log(getName());