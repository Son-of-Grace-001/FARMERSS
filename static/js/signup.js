let error1 = document.getElementById("required1");
let error2 = document.getElementById("required2");
let error3 = document.getElementById("required3");
let error4 = document.getElementById("required4");
let error5 = document.getElementById("required5");
let error6 = document.getElementById("required6");
let fname = document.getElementById("fname");
let lname = document.getElementById("lname");
let username = document.getElementById("username");
let mail = document.getElementById("mail");
let password = document.getElementById("password");
let cpassword = document.getElementById("cpassword");
let form = document.getElementById("form");
let submit = document.getElementById("btn");

var validRegex = /^[A-Za-z\._\-0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/;

form.addEventListener("submit", function (e) {
  e.preventDefault();

  // Reset error messages
  // error1.style.display = "none";
  // error2.style.display = "none";
  // error3.style.display = "none";
  // error4.style.display = "none";
  // error5.style.display = "none";
  // error6.style.display = "none";

  // Validation checks
  if (fname.value === '') {
    error1.style.display = "block";
  }
  
  if (lname.value === '') {
    error2.style.display = "block";
  }
  else{
    return true;
  }

  if (username.value === '') {
    error3.style.display = "block";
  }
  else{
    return true;
  }

  if (!mail.value.match(validRegex) || mail.value === '') {
    mail.style.color = "red";
    mail.style.border = "1px solid red";
    error4.style.display = "block";
  }
  else{
    return true;
  }

  if (password.value === '') {
    error5.style.display = "block";
  }
  else{
    return true;
  }

  if (cpassword.value !== password.value) {
    error6.style.display = "block";
  }
  else{
    return true;
  }

  // If all validation checks pass, submit the form
  if (
    fname.value !== "" &&
    lname.value !== "" &&
    username.value !== "" &&
    password.value !== "" &&
    (mail.value.match(validRegex) && mail.value !== "") &&
    cpassword.value === password.value
  ) {
    // You can choose to submit the form here or return true
    // Use the correct endpoint for user registration in your fetch request
    const csrfmiddlewaretoken = form.csrfmiddlewaretoken.value;
    const formData = new FormData(form);

    fetch("/signup", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfmiddlewaretoken,
      },
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the server (e.g., display success message)
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
});
