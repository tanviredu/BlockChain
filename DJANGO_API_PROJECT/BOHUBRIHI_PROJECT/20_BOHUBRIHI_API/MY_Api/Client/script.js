console.log("Inside the script js file");
document.getElementById('myform').addEventListener("submit",handleSubmit);
document.getElementById('image').addEventListener("change",handleImage);

// initially 
// the image is null
let myimage = null;

function handleImage(e){
    myimage = e.target.files[0];
    // console.log(myimage);
}

function handleSubmit(e){
    e.preventDefault();
    // collect user data
    let user = document.getElementById('user').value;
    let content = document.getElementById('content').value;
    let form_data = new FormData();
    form_data.append('user',user);
    form_data.append('content',content);
    form_data.append('image',myimage);

    // for(var [key,value] of form_data.entries()){
    //     console.log(key ,":",value);
    // }
    axios.post("http://localhost:8000/apiV1/statusV3/",form_data,{
        header:{
            "Content-Type":"multipart/form-data"
        }
    }).then((res)=>{
        console.log(res);
    })
}
