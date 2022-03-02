// var char_choice = document.getElementById("game_board").getAttribute("char_choice");

var connectionString = 'ws://' + window.location.host + '/ws/eshop/chat/';
var gameSocket = new WebSocket(connectionString);

const message_list = document.querySelector('.chat-history');
const form_submit = document.querySelector('.form-message');
const input_message = document.querySelector('.input_message');

form_submit.addEventListener('submit', function(e){
    e.preventDefault();
    const message = input_message.value;
    gameSocket.send(JSON.stringify({message}));
});

function connect() {
    gameSocket.onopen = function open() {
        console.log('WebSockets connection created.');
        // on websocket open, send the START event.
        gameSocket.send(JSON.stringify({
            "event": "START",
            "message": ""
        }));
    };

    gameSocket.onclose = function (e) {
        console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
        setTimeout(function () {
            connect();
        }, 1000);
    };
    // Sending the info about the room
    gameSocket.onmessage = function (e) {
        // On getting the message from the server
        // Do the appropriate steps on each event.
        let data = JSON.parse(e.data);
        console.log(data);
        data = data["payload"];
        let message = data['message'];
        message_list.innerHTML += `<div class="message my-message"> ${message} </div>`
    };

    if (gameSocket.readyState == WebSocket.OPEN) {
        gameSocket.onopen();
    }
}

//call the connect function at the start.
connect();