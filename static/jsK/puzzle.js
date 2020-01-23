/**
* Función que se ejecuta al arrastrar el elemento. 
**/
function start(e) {
	e.dataTransfer.effecAllowed = 'move'; // Define el efecto como mover (Es el por defecto)
	e.dataTransfer.setData("Text", e.target.id); // toma el elemento que se va a mover
	e.target.style.opacity = '0.4'; 
}

/**
* Función que se ejecuta se termina de arrastrar el elemento. 
**/
function end(e){
	e.target.style.opacity = ''; // Restaura la opacidad del elemento			
	e.dataTransfer.clearData("Data");			
}

/**
* Función que se ejecuta cuando un elemento arrastrable entra en el elemento desde del que se llama. 
**/
function enter(e) {
	return true;
}

/**
* Función que se ejecuta cuando un elemento arrastrable esta sobre el elemento desde del que se llama. 
* Devuelve false si el objeto se puede soltar en ese elemento y true en caso contrario.
**/
function over(e) {
	if ((e.target.className == "row-md-3 my") || (e.target.id == "contenedorPiezas") || 
		(e.target.className == "col-md-2 img") || (e.target.className == "col drop")|| 
		(e.target.className == "col name") || (e.target.className == "data") || (e.target.className == "col funcion") ||
		 (e.target.className == "row contenedor") )
		return false;
	else 
	return true;
}
    
/**
* Función que se ejecuta cuando un elemento arrastrable se suelta sobre el elemento desde del que se llama. 
**/
function drop(e){
	e.preventDefault(); // Evita que se ejecute la accion por defecto del elemento soltado.
	var elementoArrastrado = e.dataTransfer.getData("text");
	e.target.appendChild(document.getElementById(elementoArrastrado)); // Coloca el elemento soltado sobre el elemento desde el que se llamo esta funcion
	//comprobarPuzzle();
}

function comprobarPuzzle(){
	if((document.getElementById('pieza1').parentNode.id=='uno') &&
		(document.getElementById('pieza2').parentNode.id=='dos') &&
		(document.getElementById('pieza3').parentNode.id=='tres') &&
		(document.getElementById('pieza4').parentNode.id=='cuatro'))
	{
		alert('Ejercicio resuelto');
	}
}

function puzzle(){
	if((document.getElementById('pieza1').parentNode.id=='uno')&&
		(document.getElementById('pieza2').parentNode.id=='dos') &&
		(document.getElementById('pieza3').parentNode.id=='tres') &&
		(document.getElementById('pieza4').parentNode.id=='cuatro') &&
		(document.getElementById('pieza5').parentNode.id=='cinco') &&
		(document.getElementById('pieza6').parentNode.id=='seis') &&
		(document.getElementById('pieza7').parentNode.id=='siete') &&
		(document.getElementById('pieza8').parentNode.id=='ocho'))
	{
		alert('Ejercicio resuelto');
	}
	else{alert('Ta mal');}
}

function array()
{
	var foo = document.getElementById('Padre');
	var limite = numero();
	for (var i =0; i<limite;i++) 
	{
		if (foo.childNodes[i].id == ("pieza"+(i+1))) 
		{
			if (limite == i+1) 
			{
				alert('¡Pasaste la prueba!'); 
				document.getElementById("calificacion").value=100;
			}
		
		} 
		else 
		{	

				alert('Ohhh no :( \n parece que te equivocaste!')
				break;
		}

		
	}
		
}

function array2()
{
	var foo = document.getElementById('Padre');
	if (foo.childNodes[1].id == "pieza1" && foo.childNodes[2].id == "pieza2" && foo.childNodes[3].id == "pieza3")
	{
		alert("Pasaste la prueba!");
		document.getElementById('calificacion').value=100;
	}
	else
	{
		alert("Ohh no! :C \n Parece que te equivocaste");
	}
		
}



function validation()
{
	var waa = document.getElementById("cajaImagen").children;
	var waa1 = document.getElementById("cajaNombre").children;
	var waa2 = document.getElementById("cajaFuncion").children;

	var waa0 = document.getElementById("cajaImagen1").children;
	var waa01 = document.getElementById("cajaNombre1").children;
	var waa02 = document.getElementById("cajaFuncion1").children;

	var waa00 = document.getElementById("cajaImagen2").children;
	var waa001 = document.getElementById("cajaNombre2").children;
	var waa002 = document.getElementById("cajaFuncion2").children;

	var waa000 = document.getElementById("cajaImagen3").children;
	var waa0001 = document.getElementById("cajaNombre3").children;
	var waa0002 = document.getElementById("cajaFuncion3").children;

	var waa0000 = document.getElementById("cajaImagen4").children;
	var waa00001 = document.getElementById("cajaNombre4").children;
	var waa00002 = document.getElementById("cajaFuncion4").children;

	

	var a = (waa[0].id).charAt((waa[0].id).length-1);
	var b = (waa1[0].id).charAt((waa1[0].id).length-1);
	var c = (waa2[0].id).charAt((waa2[0].id).length-1);

		if ((a == b) && (b == c))
		{

			 a = (waa0[0].id).charAt((waa0[0].id).length-1);
			 b = (waa01[0].id).charAt((waa01[0].id).length-1);
			 c = (waa02[0].id).charAt((waa02[0].id).length-1);
					
			if ((a == b) && (b == c))
			{

			 a = (waa00[0].id).charAt((waa00[0].id).length-1);
			 b = (waa001[0].id).charAt((waa001[0].id).length-1);
			 c = (waa002[0].id).charAt((waa002[0].id).length-1);
					

				if ((a == b) && (b == c))
				{


			 a = (waa000[0].id).charAt((waa000[0].id).length-1);
			 b = (waa0001[0].id).charAt((waa0001[0].id).length-1);
			 c = (waa0002[0].id).charAt((waa0002[0].id).length-1);
					
					
					if ((a == b) && (b == c))
					{

			 a = (waa0000[0].id).charAt((waa0000[0].id).length-1);
			 b = (waa00001[0].id).charAt((waa00001[0].id).length-1);
			 c = (waa00002[0].id).charAt((waa00002[0].id).length-1);
					


						if ((a == b) && (b == c))
						{
							alert('¡Pasaste la prueba!'); 
							document.getElementById("calificacion").value=100;		
						}

						else
						{
							alert("Error");
						}
								
					}

					else
					{
						alert("Error");
					}			
				}

				else
				{
					alert("Error");
				}
						
			}

			else
			{
				alert("Error");
			}

		}

		else
		{
			alert("Error");

		}
	


	
}

function valid3k()
{
	ans1 = document.getElementById("res1").value;
	ans2 = document.getElementById("res2").value;
	ans3 = document.getElementById("res3").value;

	if(ans1 == "si" && ans2 == "entonces" && ans3 == "fin_si")
	{
		alert("Correcto");
		document.getElementById("calificacion").value=100;

	}
	else
	{
		alert("Algo no está bien, revisa");
	}
}

function valid3k1()
{
	ans1 = document.getElementById("res1").value;
	ans2 = document.getElementById("res2").value;
	ans3 = document.getElementById("res3").value;
	ans4 = document.getElementById("res4").value;

	if(ans1 == "desde" && ans2 == "hasta" && ans3 == "hacer" && ans4 == "fin_desde")
	{
		alert("Correcto");
		document.getElementById("calificacion").value=100;

	}
	else
	{
		alert("Algo no está bien, revisa");
	}
}


function valid5k2()
{
	ans1 = document.getElementById("res1").value;

	if(ans1 == "int a, int b")
	{
		alert("Correcto");
		document.getElementById("calificacion").value=100;

	}
	else
	{
		alert("Algo no está bien, revisa");
	}
}

function valid4k1()
{
	ans1 = document.getElementById("res1").value;
	ans2 = document.getElementById("res2").value;
	ans3 = document.getElementById("res3").value;
	ans4 = document.getElementById("res4").value;
	ans5 = document.getElementById("res5").value;

	if(ans1 == "desde" && ans2 == "hasta" && ans3 == "hacer" && ans4 == "i" && ans5 == "fin_desde")
	{
		alert("Correcto");
		document.getElementById("calificacion").value=100;

	}
	else
	{
		alert("Algo no está bien, revisa");
	}
}

function validarray()
{
	ans1 = document.getElementById("res1").value;
	ans2 = document.getElementById("res2").value;
	ans3 = document.getElementById("res3").value;
	ans4 = document.getElementById("res4").value;
	ans5 = document.getElementById("res5").value;
	ans6 = document.getElementById("res6").value;
	ans7 = document.getElementById("res7").value;
	ans8 = document.getElementById("res8").value;
	ans9 = document.getElementById("res9").value;
	ans10 = document.getElementById("res10").value;
	ans11 = document.getElementById("res11").value;
	ans12 = document.getElementById("res12").value;
	ans13 = document.getElementById("res13").value;
	ans14 = document.getElementById("res14").value;
	ans15 = document.getElementById("res15").value;
	ans16 = document.getElementById("res16").value;
	ans17 = document.getElementById("res17").value;
	ans18 = document.getElementById("res18").value;


	if(ans1 == "0" && ans2 == "0" 
	&& ans3 == "0" && ans4 == "1" 
	&& ans5 == "0" && ans6 == "2"
	&& ans7 == "1" && ans8 == "0"
	&& ans9 == "1" && ans10 == "1"
	&& ans11 == "1" && ans12 == "2"
	&& ans13 == "2" && ans14 == "0"
	&& ans15 == "2" && ans16 == "1"
	&& ans17 == "2" && ans18 == "2"


	)
	{
		alert("Correcto");
		document.getElementById("calificacion").value=100;

	}
	else
	{
		alert("Algo no está bien, revisa");
	}
}



function validationk2()
{
	var waa = document.getElementById("cajaImagen").children;
	var waa1 = document.getElementById("cajaNombre").children;

	var waa0 = document.getElementById("cajaImagen1").children;
	var waa01 = document.getElementById("cajaNombre1").children;

	var waa00 = document.getElementById("cajaImagen2").children;
	var waa001 = document.getElementById("cajaNombre2").children;


	var a = (waa[0].id).charAt((waa[0].id).length-1);
	var b = (waa1[0].id).charAt((waa1[0].id).length-1);

	if(a == b)
	{
		
	var a = (waa0[0].id).charAt((waa0[0].id).length-1);
	var b = (waa01[0].id).charAt((waa01[0].id).length-1);

	if(a == b)
	{
	
	a = (waa00[0].id).charAt((waa00[0].id).length-1);
	b = (waa001[0].id).charAt((waa001[0].id).length-1);
	if(a==b)
	{
		alert("¡Pasaste la prueba!");
		document.getElementById("calificacion").value=100;
	}
	else
	{
		alert("Error");
	}

	

	}
	else
	{
		alert("Error");
	}

	}

	else
	{
		alert("Error");
	}


	
	


	
}

function numero()
{
	var num = document.getElementById("NumeroPiezas");
    var limite = parseInt(num.innerHTML);
	return limite;
}

/**
* Muestra un mensaje de advertencia si el navegador no soporta Drag & Drop. (En Windows no lo soportan ni IE ni Safari)
**/
function comprobarnavegador() {
	if( 
		(navigator.userAgent.toLowerCase().indexOf('msie ') > -1) || 
		((navigator.userAgent.toLowerCase().indexOf('safari') > -1) && (navigator.userAgent.toLowerCase().indexOf('chrome') == -1)))
	{
		alert("Tu navegador no soporta correctamente las funciones Drag & Drop de HTML5. Prueba con otro navegador.");
	}

}


var A;
var B;


function reset1(){
    var container = document.getElementById("contenedorPiezas");
	container.innerHTML= A;
	var containert = document.getElementById("Padre");
    containert.innerHTML= B;
}       

function reset2(){
    var container = document.getElementById("Padre");
	container.innerHTML= A;
	var containert = document.getElementById("ConterF");
    containert.innerHTML= B;
} 

function resetA(){
    var container = document.getElementById("Padre");
	container.innerHTML= A;
}