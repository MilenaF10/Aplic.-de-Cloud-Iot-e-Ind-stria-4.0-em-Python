function updateTemperature(temperature) {
    const temperatureElement = document.getElementById('temperature');
    const alertElement = document.getElementById('alert');

    temperatureElement.textContent = `Temperatura: ${temperature}°C`;

    if (temperature < 5) {
        alertElement.textContent = 'Alerta: Temperatura muito baixa!';
        alertElement.style.color = 'blue';
    } else if (temperature > 30) {
        alertElement.textContent = 'Alerta: Temperatura muito elevada!';
        alertElement.style.color = 'red';
    } else {
        alertElement.textContent = 'Temperatura normal.';
        alertElement.style.color = 'green';
    }
}

// Simulação para teste
setInterval(() => {
    // Simular uma leitura de temperatura (exemplo)
    const simulatedTemperature = Math.floor(Math.random() * 40); // Gera uma temperatura aleatória entre 0 e 40
    updateTemperature(simulatedTemperature);
}, 3000);
