document.getElementById('symptomForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const symptom = document.getElementById('symptom').value;
    const resultDiv = document.getElementById('result');
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ symptom })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        resultDiv.innerHTML = `<p>You have been diagonised with: ${data.disease}</p>`;
    } catch (error) {
        resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
    }
});
