document.getElementById("register-form").addEventListener("submit", function (event) {
    // Get values from input fields
    var First = document.getElementById("first_name").value.trim();
    var Last = document.getElementById("last_name").value.trim();
    var email = document.getElementById("email").value.trim();
    var UserName = document.getElementById("user_name").value.trim();
    var Pw = document.getElementById("password").value;

    let isValid = true;

    // Validate only the first field if no fields are filled
    if (First === "" && Last === "" && email === "" && UserName === "" && Pw === "") {
        document.getElementById("first_name_error").innerHTML = "Enter Valid First Name";
        isValid = false;
    }

    // Validate First Name
    else if (First === "") {
        document.getElementById("first_name_error").innerHTML = "Enter Valid First Name";
        isValid = false;
    }

    // Validate Last Name (only if First is filled)
    else if (First !== "" && Last === "") {
        document.getElementById("last_name_error").innerHTML = "Enter Valid Last Name";
        isValid = false;
    }

    // Validate Email (only if First and Last are filled)
    else if (First !== "" && Last !== "" && email === "") {
        document.getElementById("email_error").innerHTML = "Enter Valid Email";
        isValid = false;
    }

    // Validate Username (only if First, Last, and Email are filled)
    else if (First !== "" && Last !== "" && email !== "" && UserName === "") {
        document.getElementById("user_name_error").innerHTML = "Enter Valid Username";
        isValid = false;
    }

    // Validate Password (only if First, Last, Email, and Username are filled)
    else if (First !== "" && Last !== "" && email !== "" && UserName !== "" && Pw === "") {
        document.getElementById("password_error").innerHTML = "Enter Valid Password";
        isValid = false;
    } else if (Pw.length < 8) {
        document.getElementById("password_error").innerHTML = "Password must be at least 8 characters";
        isValid = false;
    } else if (!/[A-Z]/.test(Pw)) {
        document.getElementById("password_error").innerHTML = "Password must include at least one uppercase letter";
        isValid = false;
    } else if (!/[a-z]/.test(Pw)) {
        document.getElementById("password_error").innerHTML = "Password must include at least one lowercase letter";
        isValid = false;
    } else if (!/[0-9]/.test(Pw)) {
        document.getElementById("password_error").innerHTML = "Password must include at least one number";
        isValid = false;
    } else if (!/[!@#$%^&*(),.?":{}|<>]/.test(Pw)) {
        document.getElementById("password_error").innerHTML = "Password must include at least one special character";
        isValid = false;
    }

    // Prevent form submission if validation fails
    if (!isValid) {
        event.preventDefault(); // Stop the form submission
    }
});

// Clear error message when user starts typing in any field
document.querySelectorAll("input").forEach(input => {
    input.addEventListener("input", function () {
        document.getElementById(this.id + "_error").innerHTML = "";
    });
});


function toggleVisibility() {
    let passwordField = document.getElementById("password");
    let eyeIcon = document.getElementById("eye");

    if (passwordField.type === "password") {
        passwordField.type = "text";
        eyeIcon.src = "../static/img/EyeSlash.svg";
    } else {
        passwordField.type = "password";
        eyeIcon.src = "../static/img/Eye.svg";
    }
}