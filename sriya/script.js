async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('documentContent').innerText = result.document;

    // Show success pop-up
    showPopup("File uploaded successfully!");
}

async function queryDocument() {
    const question = document.getElementById('queryInput').value;
    const documentText = document.getElementById('documentContent').innerText;

    const response = await fetch('http://127.0.0.1:5000/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question, document: documentText })
    });

    const result = await response.json();
    document.getElementById('queryResult').innerText = result.response;
}

// Function to show pop-up notification
function showPopup(message) {
    const popup = document.createElement('div');
    popup.className = 'popup';
    popup.innerText = message;
    document.body.appendChild(popup);

    // Show popup and auto-hide after 3 seconds
    setTimeout(() => popup.classList.add('show'), 100);
    setTimeout(() => {
        popup.classList.remove('show');
        setTimeout(() => popup.remove(), 300);
    }, 3000);
}