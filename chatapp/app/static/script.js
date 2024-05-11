var ws = new WebSocket('ws://127.0.0.1:8000/ws/as/');

ws.onopen = function() {
    console.log('WebSocket is connected');
    ws.send('Hello from the client!');
}

ws.onmessage = function(e) {
    console.log('Message:', e.data);
    console.log('Message Received from server', JSON.parse(e.data));
    console.log('Type:', typeof (e.data));
    var data = JSON.parse(e.data);
    console.log('Type:', typeof (data));
    document.getElementById('chat').innerText= data.count
}

ws.onerror = function(e) {
    console.log('WebSocket error:', e);

}

ws.onclose = function(e) {
    console.log('WebSocket is closed');
}

