

function validate(){
     let mail = document.getElementById("floatingInput").value;
     const email_input = document.getElementById("floatingInput")
     const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    if(validRegex.test(mail)) {

        alert("email valid")
        return true
    }
    else {
        console.log("Email not valid")
        email_input.classList.add("is-invalid")


        return false

    }

}