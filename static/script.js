async function analyzeAudio() {
    console.log("Analyze clicked");

    const fileInput = document.getElementById("audioFile");
    const status = document.getElementById("status");

    if (fileInput.files.length === 0) {
        status.innerText = "Select a file first";
        return;
    }

    status.innerText = "Analyzing...";

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        console.log("Response:", data);

        if (data.final === "SAFE") {
            status.innerText = "✅ SAFE";
            status.style.color = "green";
        } else if (data.final === "DANGER") {
            status.innerText = "🚨 DANGER";
            status.style.color = "red";
        } else {
            status.innerText = "⚠ UNCERTAIN";
            status.style.color = "orange";
        }

    } catch (e) {
        console.error(e);
        status.innerText = "ERROR";
    }
}
