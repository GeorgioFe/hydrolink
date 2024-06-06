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

    const response = await fetch('http://192.168.1.236:500/calculate_recommended_intake', {
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
        const response = await fetch('http://192.168.1.236:500/set_reminder', {
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
