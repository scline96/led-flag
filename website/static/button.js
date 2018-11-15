var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);


function button(){
	console.log('button pressed')
	socket.emit('button', 'name')
}
