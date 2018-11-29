var socket = io.connect('http://' + document.domain + ":" + location.port);


function button(){
	socket.emit('button',  document.getElementById('inputtext').value)
	console.log( document.getElementById('inputtext').value)
	console.log('button pressed')
}
