const webSocker = new WebSocket("ws://192.168.1.156:8001/custumer/create")

function sendMessage() {
    let name = document.getElementById("name");
    let description = document.getElementById("description");

    const category = {
        name: name,
        description: description,
    }

    webSocker.send(JSON.parse({"category": category}))
}