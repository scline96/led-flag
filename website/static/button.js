var namespace = 'led'
var socket = io.connect('http://' + location.host);


function button(){
	socket.emit('button', 'name')
	console.log('button pressed')
}
