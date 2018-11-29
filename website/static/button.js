var socket = io.connect('http://' + document.domain + ":" + location.port);


function button(){
	socket.emit('button', 'name_of_button')
	console.log('button pressed')
}
