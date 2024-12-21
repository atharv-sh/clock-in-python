function updateTime() {
    const clockElement = document.getElementById('clock');
    const currentTime = new Date().toLocaleTimeString();
    clockElement.textContent = currentTime;
}

// Update the clock every second
setInterval(updateTime, 1000);

// Initialize the clock
updateTime();