let error1= document.getElementById("error1");
let error2= document.getElementById("error2");
let mail = document.getElementById("email");
let password = document.getElementById("password");
let submit = document.getElementById("btn");

var validRegex = /^[A-Za-z\._\-0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/;

let form = document.getElementById("form");
form.addEventListener("submit", required)
function required(e){
  e.preveventDefault()

  
  if (!email.value.match(validRegex) || email.value ==='') {
    email.style.color = "red";
    email.style.border = "1px solid red";
    error1.style.display= "block";
    return;
  }
  error1.style.display = "none";
  email.style.border = "1px solid #767A77";
  email.style.color = "#767A77"

  if (password.value ===""){
    error2.style.display = "block"
    return false
  }
  error2.style.display = "none"

  if (username.value !=="" && password.value !==""){
    submit.style.backgroundColor = "#1D4025"
    submit.style.color = "#ffffff"

    const csrfmiddlewaretoken = form.csrfmiddlewaretoken.value
    var data = new FormData();
    data.append("json", JSON.stringify( obj ) );
    let data = new FormData();
    data.append('email', mail.value);
    data.append('password', password.value);
    fetch("/login",{
      method:"POST",
      headers: { "X-CSRFToken": csrfmiddlewaretoken, "Content-Type": "application/json" },
      body: data,
      // credentials: 'same-origin',
    })
    return true
  }

}