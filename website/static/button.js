var socket = io.connect('http://' + document.domain + ":" + location.port);

function stop(){
	socket.emit('stop')
}

function button(){
	socket.emit('text',  document.getElementById('inputtext').value)
	//console.log( document.getElementById('inputtext').value)
	//console.log('button pressed')
}
