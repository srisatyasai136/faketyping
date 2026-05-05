// 🚫 Disable copy/paste/right click

document.addEventListener("copy", e => e.preventDefault());
document.addEventListener("paste", e => e.preventDefault());
document.addEventListener("cut", e => e.preventDefault());
document.addEventListener("contextmenu", e => e.preventDefault());

// 🚫 Disable typing paste shortcuts (Ctrl+V, Ctrl+C)
document.addEventListener("keydown", function(e) {
    if (e.ctrlKey && (e.key === 'c' || e.key === 'v' || e.key === 'x')) {
        e.preventDefault();
    }
});

// Submit function
function submitText() {
    let text = document.getElementById("typingArea").value;

    fetch("/submit_work/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ text: text })
    })
    .then(res => res.json())
    .then(data => {
        alert("Submitted!");

        // Clear textarea
        document.getElementById("typingArea").value = "";

        // Load next paragraph
        document.getElementById("para").innerText = data.new_paragraph;
    });
}

// CSRF helper
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie) {
        document.cookie.split(';').forEach(cookie => {
            let c = cookie.trim();
            if (c.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(c.substring(name.length + 1));
            }
        });
    }
    return cookieValue;
}