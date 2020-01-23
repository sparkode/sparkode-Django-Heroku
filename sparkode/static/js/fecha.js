function calendar(){
	var day=['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes'];
	var month=['Enero','Feberero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];
	var d=new Date();
	setText('calendar-day',day[d.getDay()]);
	setText('calendar-date',d.getDate());
	setText('calendar-month-year',month[d.getMonth()]+' '+(d.getFullYear()));
};

function setText(id,val){
	if(val<10){
		val='0'+val;
	}
	document.getElementById(id).innerHTML=val;
};

window.onload=calendar;