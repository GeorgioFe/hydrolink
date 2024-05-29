let waterIntake = 0;
let lastDrinkTime = new Date();

function setTimeFrame(frame) {
    // Logic to filter and display water intake data based on the selected timeframe
    console.log(`Timeframe set to: ${frame}`);
}

function setReminder() {
    const interval = document.getElementById('reminder-interval').value;
    if (interval) {
        setInterval(() => {
            alert('Time to drink water!');
        }, interval * 60000);
    } else {
        alert('Please enter a valid interval.');
    }
}

function updateWaterIntake(amount) {
    waterIntake += amount;
    const percentage = (waterIntake / 2) * 100; // Assuming 2L is the daily goal
    document.getElementById('water-intake-percentage').innerText = `${percentage}%`;
    document.getElementById('liquid-volume').innerText = `${waterIntake.toFixed(2)} L`;
    lastDrinkTime = new Date();
    document.getElementById('last-drink-time').innerText = 'Just now';
}

// Simulate water intake for demonstration
setTimeout(() => {
    updateWaterIntake(0.25); // Add 250mL
}, 5000);

function toggleMenu() {
    const menu = document.getElementById('menu');
    const burger = document.getElementById('burger');
    if (menu && burger) {
        menu.classList.toggle('active');
        burger.classList.toggle('active');
    }
}


