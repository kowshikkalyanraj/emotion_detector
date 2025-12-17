// ✅ Emotion Detection (with 5-second camera capture + countdown)
const video = document.createElement("video");
video.autoplay = true;
video.width = 400;
video.height = 300;
video.style.borderRadius = "10px";
video.style.display = "none"; // hidden until start
document.querySelector(".emotion-section").appendChild(video);

const emotionQuote = document.getElementById("emotion-quote");
const detectBtn = document.getElementById("detect-emotion");

const countdownText = document.createElement("h4");
countdownText.style.color = "#007bff";
countdownText.style.fontSize = "18px";
countdownText.style.marginTop = "10px";
document.querySelector(".emotion-section").appendChild(countdownText);

detectBtn.addEventListener("click", async () => {
    try {
        detectBtn.textContent = "Detecting...";
        detectBtn.disabled = true;
        emotionQuote.textContent = "😊 Please look at the camera...";
        countdownText.textContent = "";

        // Access camera
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
        video.style.display = "block";

        // Countdown from 5 seconds
        let timeLeft = 5;
        countdownText.textContent = `Capturing in ${timeLeft}...`;
        const countdownInterval = setInterval(() => {
            timeLeft--;
            if (timeLeft > 0) {
                countdownText.textContent = `Capturing in ${timeLeft}...`;
            } else {
                clearInterval(countdownInterval);
                countdownText.textContent = "Capturing now...";
            }
        }, 1000);

        // Capture frame after 5 seconds
        setTimeout(async () => {
            const canvas = document.createElement("canvas");
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const ctx = canvas.getContext("2d");
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

            const imageData = canvas.toDataURL("image/jpeg");

            // Stop camera
            stream.getTracks().forEach(track => track.stop());
            video.style.display = "none";

            // Send to backend
            const response = await fetch("/detect_emotion", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ image: imageData })
            });

            const data = await response.json();
            emotionQuote.textContent = `Detected Emotion: ${data.emotion.toUpperCase()} 💫\n${data.quote}`;
            countdownText.textContent = "";
            detectBtn.textContent = "Detect Emotion";
            detectBtn.disabled = false;

        }, 5000); // 5 seconds delay

    } catch (err) {
        console.error("Camera error:", err);
        emotionQuote.textContent = "⚠️ Unable to access camera.";
        detectBtn.textContent = "Detect Emotion";
        detectBtn.disabled = false;
        countdownText.textContent = "";
    }
});
