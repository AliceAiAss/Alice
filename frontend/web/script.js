const micButton = document.getElementById("mic-button");
const resultDiv = document.getElementById("result");

let mediaRecorder;
let audioChunks = [];

micButton.onclick = async () => {
  if (!mediaRecorder || mediaRecorder.state === "inactive") {
    audioChunks = [];
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    mediaRecorder.ondataavailable = event => {
      audioChunks.push(event.data);
    };

    mediaRecorder.onstop = async () => {
      const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
      const formData = new FormData();
      formData.append('file', audioBlob, 'audio.wav');

      resultDiv.textContent = "⏳ Transcribing...";

      try {
        const response = await fetch("http://127.0.0.1:8000/api/listen", {
          method: "POST",
          body: formData
        });

        const data = await response.json();
        resultDiv.textContent = `🗣️ You said: "${data.transcription || 'No speech detected.'}"`;
      } catch (error) {
        resultDiv.textContent = "❌ Error during transcription.";
        console.error(error);
      }
    };

    setTimeout(() => {
      mediaRecorder.stop();
    }, 4000); // Record for 4 seconds
  }
};
