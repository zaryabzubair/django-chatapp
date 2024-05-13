const groupName = JSON.parse(document.getElementById('group-name').textContent);
console.log('Group name:', groupName);

var ws = new WebSocket(
    'ws://' + window.location.host + '/ws/sc/' + groupName + '/'
);

ws.onopen = function() {
    console.log('WebSocket is connected');
}

ws.onmessage = function(event) {
    console.log('WebSocket message received:', event.data);
    console.log('Type of message:', typeof(event.data));
    const data = JSON.parse(event.data);
    console.log('Data:', data);
    console.log('Type of data:', typeof(data));
    console.log('Actual message:', data.message);
    document.querySelector('#chat-log').value += (data.message + '\n');

}


ws.onerror = function(event) {
    console.log('WebSocket error:', event);

}

ws.onclose = function(event) {
    console.log('WebSocket is closed');
}

document.getElementById('chat-submit').onclick = function(event) {
    const messageInput = document.getElementById('chat-message');
    const message = messageInput.value
    ws.send(JSON.stringify({
        'message': message,
    }));
    messageInput.value = '';
}

