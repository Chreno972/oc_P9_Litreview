

let success_message = document.getElementById("success");
let error_message = document.getElementById("error_message");

if (success_message.innerText) {
    success_message.style.display = "block";
    setTimeout(() => {
        success_message.style.display = "none";
    }, 3000);
}

if (error_message.innerText) {
    error_message.style.display = "block";
    setTimeout(() => {
        error_message.style.display = "none";
    }, 3000);
}
