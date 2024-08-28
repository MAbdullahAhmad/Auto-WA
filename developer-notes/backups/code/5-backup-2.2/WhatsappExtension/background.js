let syncIntervalId = null;
let waTabId = null;

function startSyncing(tabId) {
    if (!syncIntervalId) {
        syncIntervalId = setInterval(() => syncWithServer(tabId), 5000);
        console.log("Started syncing with WhatsApp Web.");
    }
}

function stopSyncing() {
    if (syncIntervalId) {
        clearInterval(syncIntervalId);
        syncIntervalId = null;
        console.log("Stopped syncing with WhatsApp Web.");
    }
}

function syncWithServer(tabId) {
    chrome.scripting.executeScript({
        target: { tabId: tabId },
        files: ["content.js"]
    }, () => {
        chrome.tabs.sendMessage(tabId, { action: "sync" }, (response) => {
            if (response && response.message_to_send) {
                console.log("Message to send:", response.message_to_send);
            }
        });
    });
}

function checkForWhatsAppTab() {
    chrome.tabs.query({}, (tabs) => {
        const waTab = tabs.find(tab => tab.url && tab.url.startsWith("https://web.whatsapp.com"));
        
        if (waTab) {
            waTabId = waTab.id;
            console.log("WhatsApp Web tab found:", waTabId);
            startSyncing(waTabId);
        } else {
            console.log("No WhatsApp Web tab found.");
            stopSyncing();
            waTabId = null;
        }
    });
}

chrome.runtime.onInstalled.addListener(() => {
    console.log("WhatsApp Extension Installed and Running");
    checkForWhatsAppTab();

    // Check every second to see if the WhatsApp tab opens or closes
    setInterval(checkForWhatsAppTab, 1000);
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (tabId === waTabId && changeInfo.status === "complete") {
        startSyncing(tabId);
    }
});

chrome.tabs.onRemoved.addListener((tabId, removeInfo) => {
    if (tabId === waTabId) {
        stopSyncing();
        waTabId = null;
    }
});
