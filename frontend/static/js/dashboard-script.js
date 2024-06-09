function toggleMenu() {
    const burger = document.querySelector('.burger');
    const menu = document.querySelector('.menu');
    burger.classList.toggle('active');
    menu.classList.toggle('active');
}

async function calculateIntake(event) {
    event.preventDefault();
    console.log("Form submission intercepted.");

    const age = document.getElementById('age').value;
    const weight = document.getElementById('weight').value;
    const activity = document.getElementById('activity').value;

    const response = await fetch('http://172.20.10.2:500/calculate_recommended_intake', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ age, weight, activity })
    });

    if (response.ok) {
        const data = await response.json();
        console.log("Response received:", data);
        const resultContainer = document.getElementById('intake-result');
        resultContainer.innerHTML = `<span>Your recommended daily water intake is ${data.intake} ounces! 😁</span>`;
        resultContainer.style.display = 'flex'; // Show the result container
    } else {
        console.log("Response error:", response.statusText);
        const resultContainer = document.getElementById('intake-result');
        resultContainer.innerHTML = `<span>An error occurred. Please try again.</span>`;
        resultContainer.style.display = 'flex'; // Show the result container
    }
}

async function setReminder() {
    const interval = document.getElementById('interval').value;
    console.log(`Setting reminder interval to ${interval} minutes.`);

    try {
        const response = await fetch('http://172.20.10.2:500/set_reminder', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ interval: interval })
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Interval set:", data);
            const reminderContainer = document.getElementById('reminder-result');
            reminderContainer.innerHTML = `<span>Reminder set for every ${interval} minutes! ⏰</span>`;
            reminderContainer.style.display = 'flex'; // Show the result container
        } else {
            console.log("Response error:", response.statusText);
            const reminderContainer = document.getElementById('reminder-result');
            reminderContainer.innerHTML = `</div><span>An error occurred. Please try again.</span>`;
            reminderContainer.style.display = 'flex'; // Show the result container
        }
    } catch (error) {
        console.log("Fetch error:", error);
        const reminderContainer = document.getElementById('reminder-result');
        reminderContainer.innerHTML = `<div class="icon"></div><span>An error occurred. Please try again.</span>`;
        reminderContainer.style.display = 'flex'; // Show the result container
    }
}

async function toggleDemoMode() {
    const demoMode = document.getElementById('demo-mode').checked;
    console.log(`Demo mode is now ${demoMode ? 'enabled' : 'disabled'}.`);

    try {
        const response = await fetch('http://172.20.10.2:500/toggle_demo_mode', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ demo_mode: demoMode })
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.message);
        } else {
            console.log("Response error:", response.statusText);
        }
    } catch (error) {
        console.log("Fetch error:", error);
    }
}

function startVolumeUpdate() {
    setInterval(async () => {
        const response = await fetch('http://172.20.10.2:500/volume');
        if (response.ok) {
            const data = await response.json();
            document.getElementById('volume-display').innerText = `Volume: ${data.latest_volume} oz`;
        }
    }, 5000);
}

async function calibrate() {
    const response = await fetch('http://172.20.10.2:500/calibrate', {
        method: 'POST'
    });

    if (response.ok) {
        const data = await response.json();
        // document.getElementById('volume-display').innerText = `Volume: ${data.calibrated_distance}`;
        startVolumeUpdate(); // Start updating the volume every 5 seconds
    } else {
        const errorData = await response.json();
        document.getElementById('volume-display').innerText = `Error: ${errorData.message}`;
    }
}