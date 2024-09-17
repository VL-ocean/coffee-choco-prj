// Remove warning about CKE editor
document.addEventListener("DOMContentLoaded", () => {
    const intId = setInterval(() => {
        const popup = document.querySelector(".cke_notifications_area");
        if (popup) {
            popup.style.display = "none";
            clearInterval(intId);
        }
    }, 100);
});


// Tooltip
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))


// Hide messages after 5 seconds 
document.addEventListener("DOMContentLoaded", () => {
    const waitingTime = setInterval(() => {
        const message = document.querySelector(".message-box");
        if (message) {
            message.style.display = "none";
            clearInterval(waitingTime)
        }
    }, 4000);
});