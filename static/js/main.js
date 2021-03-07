function navbarToggler() {
	var x = document.getElementById('Navbar')
	if (x.className === 'navbar'){
		x.className += ' responsive';

	}
	else {
		x.className = 'navbar'
	}
}

const sm = document.getElementById('cancel');
const lg = document.getElementById('side-menu');
const icon = document.getElementById('cancel-icon')

sm.onclick = hid

var i = 0;
function hid(){
	if (i == 0){
		lg.style.width = '50px';
		icon.className = 'fa fa-arrow-alt-circle-right';
		i = 1;

	}
	else if(i == 1){
		lg.style.width = '100%';
		icon.className = ' fa fa-arrow-alt-circle-left';
		i = 0;
	}
}

function showp(){
	document.getElementById('pro').style.width = 'auto';
}
