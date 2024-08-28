chrome.runtime.onInstalled.addListener(() => {
    console.log("WhatsApp Extension Installed and Running");
});

chrome.runtime.onMessageExternal.addListener((request, sender, sendResponse) => {
    console.log("Received request:", request);

    chrome.tabs.query({ url: "*://web.whatsapp.com/*" }, (tabs) => {
        if (tabs.length === 0) {
            console.log("WhatsApp Web is not open.");
            sendResponse({ success: false, message: "WhatsApp Web is not open." });
            return;
        }

        const activeTab = tabs[0].id;

        chrome.scripting.executeScript(
            {
                target: { tabId: activeTab },
                files: ["content.js"]
            },
            () => {
                chrome.tabs.sendMessage(activeTab, request, sendResponse);
            }
        );
    });

    // Keep the message channel open for asynchronous responses
    return true;
});
