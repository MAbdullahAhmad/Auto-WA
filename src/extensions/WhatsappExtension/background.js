let tab_interval = null;
let waTabId = null;

function start_script(tabId) {
    chrome.scripting.executeScript({
        target: { tabId: tabId },
        files: ["content.js"]
    });
}

function checkForWhatsAppTab() {
    chrome.tabs.query({}, (tabs) => {
        const waTab = tabs.find(tab => tab.url && tab.url.startsWith("https://web.whatsapp.com"));

        if (waTab) {
            if (waTabId !== waTab.id) {
                waTabId = waTab.id;
                console.log("WhatsApp Web tab found:", waTabId);
                clearInterval(tab_interval);
                start_script(waTabId);
            }
        } else {
            if (waTabId !== null) {
                console.log("WhatsApp Web tab closed.");
                // stopSyncing();
                waTabId = null;
            }
        }
    });
}

chrome.runtime.onInstalled.addListener(() => {
    console.log("WhatsApp Extension Installed and Running");
    checkForWhatsAppTab();

    // Check every second to see if the WhatsApp tab opens or closes
    tab_interval = setInterval(checkForWhatsAppTab, 1000);
});

// chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
//     if (tabId === waTabId && changeInfo.status === "complete") {
//         startSyncing(tabId);
//     }
// });

// chrome.tabs.onRemoved.addListener((tabId, removeInfo) => {
//     if (tabId === waTabId) {
//         stopSyncing();
//         waTabId = null;
//     }
// });
