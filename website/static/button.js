var namespace = 'led'
var socket = io.connect('http://' + document.domain + ":" + location.port);


function button(){
	socket.emit('button', 'name')
	console.log('button pressed')
}
