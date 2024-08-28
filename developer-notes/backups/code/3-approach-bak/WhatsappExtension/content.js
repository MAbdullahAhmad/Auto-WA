// content.js

let is_wa_ready = false;

function checkWhatsAppReady() {
    const waHeader = document.querySelector("header ._21nHd"); // Update selector based on UI
    if (waHeader) {
        is_wa_ready = true;
        console.log("WhatsApp Web is ready.");
    }
}

function getUsername() {
    const element = document.querySelector("header ._21nHd"); // Update selector based on UI
    const username = element ? element.textContent : "Unknown";
    return username;
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
        return true;
    } else {
        console.log("Failed to send message: Input box or send button not found.");
        return false;
    }
}

// Run the check for WhatsApp readiness
checkWhatsAppReady();

// Listen for messages from the background script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (!is_wa_ready) {
        sendResponse({ success: false, message: "WhatsApp Web is not ready." });
        return;
    }

    if (request.action === "get_username") {
        sendResponse({ success: true, username: getUsername() });
    } else if (request.action === "get_unread_messages") {
        sendResponse({ success: true, messages: getUnreadMessages() });
    } else if (request.action === "send_message") {
        const success = sendMessage(request.message);
        sendResponse({ success: success });
    }
});
