(function(){
    if(!document.hasRunWA){
        document.hasRunWA = true;

        let is_wa_ready = false;
        let last_message_element = null;
        let check_interval = null;
        let sync_interval = null;
        let started_syncing = false;
        let last_header = null;

        function checkWhatsAppReady() {
            const waHeader = document.querySelector("#whatsapp-web #main header");

            if (waHeader) {
                is_wa_ready = true;
                
                if(!started_syncing){
                    last_message_element = document.querySelector("#whatsapp-web #main [role='application'] [role='row']:last-child");
                    clearInterval(check_interval);
                    sync_interval = setInterval(sync, 1000);
                    started_syncing = true;
                }

                if(last_header && waHeader != last_header){
                    last_message_element = document.querySelector("#whatsapp-web #main [role='application'] [role='row']:last-child");
                    last_header = waHeader;
                }
                else if(!last_header){
                    last_header = waHeader;
                }

                // console.log("WhatsApp Web is ready.");
            } else {
                // console.log("WhatsApp Web is not ready.");
            }
        }

        check_interval = setInterval(checkWhatsAppReady, 1000);

        function getUnreadMessages() {
            const messages = [];
            while(last_message_element.nextElementSibling){
                last_message_element = last_message_element.nextElementSibling;

                // skip if message not from sender
                if(!last_message_element.querySelector('.message-in')) continue;

                // console.log("msg", last_message_element.querySelector('.copyable-text').innerText);
                messages.push(last_message_element.querySelector('.copyable-text').innerText);
            }
            return messages;
        }

        // @debug
        window.getUnreadMessages = getUnreadMessages;
        window.last_message_element = last_message_element;

        function sync(){
            checkWhatsAppReady();

            if (!is_wa_ready) {
                sendResponse({ success: false, message: "WhatsApp Web is not ready." });
                return;
            }

            const new_messages = getUnreadMessages();
            const data = { new_messages: new_messages };

            // if(new_messages.length) console.log("Data", data);
            // else console.log(last_message_element);

            fetch("http://localhost:5000/sync", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            })
            .catch(error => {
                console.error("Error syncing with server:", error);
            });
        }

    }
})();