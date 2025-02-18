fetch('http://127.0.0.1:5000/api/test')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.body.innerHTML += `<p>${data.message}</p>`;
    })
    .catch(error => console.error('Erro:', error));