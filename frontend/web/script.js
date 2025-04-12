async function askAlice() {
    const userInput = document.getElementById("userInput").value;
    const res = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userInput }),
    });
  
    const data = await res.json();
    document.getElementById("response").innerText = data.response;
  
    // Speak the response
    const synth = window.speechSynthesis;
    const utter = new SpeechSynthesisUtterance(data.response);
    synth.speak(utter);
  }
  
  function startListening() {
    const recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.onresult = function (event) {
      document.getElementById("userInput").value = event.results[0][0].transcript;
      askAlice();
    };
    recognition.start();
  }
  