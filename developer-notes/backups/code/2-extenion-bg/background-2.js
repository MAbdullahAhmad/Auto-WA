chrome.runtime.onInstalled.addListener(() => {
    console.log("WhatsApp Extension Installed and Running");
});

chrome.runtime.onMessageExternal.addListener(
    function(request, sender, sendResponse) {
        console.log("Received request:", request);
        if (request.action === "get_username") {
            const username = getUsername();
            console.log("Username:", username);
            sendResponse({ username: username });
        } else if (request.action === "get_unread_messages") {
            const messages = getUnreadMessages();
            console.log("Unread Messages:", messages);
            sendResponse({ messages: messages });
        } else if (request.action === "send_message") {
            const success = sendMessage(request.message);
            console.log("Message Sent:", success);
            sendResponse({ success: success });
        }
    }
);

function getUsername() {
    // Log the action of fetching the username
    console.log("Getting username...");
    const element = document.querySelector("header ._21nHd"); // Update selector based on UI
    const username = element ? element.textContent : "Unknown";
    console.log("Fetched username:", username);
    return username;
}

function getUnreadMessages() {
    // Log the action of fetching unread messages
    console.log("Getting unread messages...");
    const messages = [];
    document.querySelectorAll(".message-in").forEach((msgElement) => {
        const message = msgElement.querySelector(".copyable-text").textContent;
        messages.push(message);
    });
    console.log("Fetched unread messages:", messages);
    return messages;
}

function sendMessage(message) {
    // Log the action of sending a message
    console.log("Sending message:", message);
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
