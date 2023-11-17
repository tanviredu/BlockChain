function greeting(){
    let message = "Hello";
    let sayHi = function hi(){
        message = "hi"
    
    };
    sayHi();
    console.log(message);

}
greeting();
