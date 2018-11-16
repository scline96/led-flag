var socket = io.connect(location.origin + '/led');


function button(){
	socket.emit('button', 'name_of_button')
	console.log('button pressed')
}
