window.is_wa_ready = false;

function checkWhatsAppReady() {
    const waHeader = document.querySelector("#whatsapp-web #main");
    if (waHeader) {
        window.is_wa_ready = true;
        console.log("WhatsApp Web is ready.");
    } else {
        console.log("WhatsApp Web is not ready.");
    }
}

function getUnreadMessages() {
    const messages = [];
    document.querySelectorAll(".message-in").forEach((msgElement) => {
        const message = msgElement.querySelector(".copyable-text").textContent;
        messages.push(message);
    });
    return messages;
}

function sendMessage(message) {
    const inputBox = document.querySelector("footer ._3FRCZ");
    const sendButton = document.querySelector("footer ._4sWnG");

    if (inputBox && sendButton) {
        inputBox.textContent = message;
        sendButton.click();
        console.log("Message sent successfully.");
        return true;
    } else {
        console.log("Failed to send message: Input box or send button not found.");
        return false;
    }
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    checkWhatsAppReady();

    if (!window.is_wa_ready) {
        sendResponse({ success: false, message: "WhatsApp Web is not ready." });
        return;
    }

    if (request.action === "sync") {
        const new_messages = getUnreadMessages();
        const data = { new_messages: new_messages };

        fetch("http://localhost:5000/sync", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message_to_send) {
                sendMessage(data.message_to_send);
            }
            sendResponse(data);
        })
        .catch(error => {
            console.error("Error syncing with server:", error);
        });
    }
    return true; // Keep the message channel open for async responses
});