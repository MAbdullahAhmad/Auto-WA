chrome.runtime.onMessageExternal.addListener(
    function(request, sender, sendResponse) {
      if (request.action === "get_username") {
          sendResponse({ username: getUsername() });
      } else if (request.action === "get_unread_messages") {
          sendResponse({ messages: getUnreadMessages() });
      } else if (request.action === "send_message") {
          const success = sendMessage(request.message);
          sendResponse({ success: success });
      }
    }
  );
  
  function getUsername() {
      const element = document.querySelector("header ._21nHd"); // Update selector based on UI
      return element ? element.textContent : "Unknown";
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
      }
      return false;
  }
  