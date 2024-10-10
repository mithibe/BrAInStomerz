document.getElementById('careerForm').addEventListener('submit', function(e){
    e.preventDefault();

    // Create an object with form data
    let formData = new FormData(e.target);

    // Send the form data to the Flask backend
    fetch('/predict', {
        method: "POST",
        body: new URLSearchParams(formData)
    })
    .then(response => response.json())
    .then(data => {
        // Display the predicted career path
        document.getElementById('result').innerText = "Suggested Career Path: " + data.prediction;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});