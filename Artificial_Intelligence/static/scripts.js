/*Esta função é responsável por enviar a mensagem do usuário para o 
servidor e atualizar a interface do usuário com a resposta do chatbot.*/

function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatBox = document.getElementById("chat-box");

    // Adiciona a mensagem do usuário ao histórico de mensagens
    chatBox.innerHTML += "<p><strong>Você:</strong> " + userInput + "</p>";

    // Faz uma solicitação AJAX para o servidor Flask
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/send-message", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Decodifica a resposta JSON e exibe o texto normalizado na interface do usuário
            var response = JSON.parse(xhr.responseText);
            chatBox.innerHTML += "<p><strong>Chatbot:</strong> " + response.response + "</p>";
        }
    };
    xhr.send(JSON.stringify({"message": userInput}));

    // Limpa o campo de entrada do usuário
    document.getElementById("user-input").value = "";

}

  