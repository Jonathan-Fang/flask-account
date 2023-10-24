function togglePassword() {
    var x = document.getElementById("psword");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password"
    }
}