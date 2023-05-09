

function validate(){
     let mail = document.getElementById("floatingInput").value;
     const display = document.getElementById("emailDisplay")
     const email_input = document.getElementById("floatingInput")
     const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    if(validRegex.test(mail)) {

        console.log("email valid")
        display.innerHTML = "Email address"
        email_input.classList.remove("is-invalid")
        return true
    }
    else {
        console.log("Email not valid")
        email_input.classList.add("is-invalid")
        display.innerHTML = "Invalid Email address"

        return false

    }

}