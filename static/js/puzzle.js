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
	if (
		
		(e.target.className == "row-md-3 my") || (e.target.id == "contenedor") || 
		(e.target.className == "col-md-2 img") || (e.target.className == "col drop")|| 
		(e.target.className == "col name") || (e.target.className == "data") || 
		(e.target.className == "col funcion") || (e.target.id == "contenedorPiezas")
		
		)
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
				document.getElementById("calificacion").innerHTML="100";
			}
		
		} 
		else 
		{	

				alert('Ohhh no :( \n parece que te equivocaste!')
				break;
		}

		
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
							alert("Ok")	
							document.getElementById("calificacion").innerHTML="100";		
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