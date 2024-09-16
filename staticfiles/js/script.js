// Remove warning about CKE editor
document.addEventListener("DOMContentLoaded", () => {
    const intId = setInterval(() => {
        const popup = document.querySelector(".cke_notifications_area");
        console.log("try");
        if (popup) {
            popup.style.display = "none";
            console.log(popup);
            clearInterval(intId);
        }
    }, 100);
});


// Tooltip
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
