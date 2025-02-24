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
