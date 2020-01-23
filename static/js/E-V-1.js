function evaluar(){
	var questions = document.getElementsByTagName("input");

	var total = 0;
	var t = 0.0;

	for(var i = 0; i < questions.length; i++)
		if(questions[i].type == "radio" && questions[i].checked)
			
			total += Number(questions[i].value);
		t = Number.parseFloat(total).toFixed(0);

 //     alert("El valor total es: " + total);
		alert("El valor total es: "+ t);

}

function validar(){

	var questions1 = document.getElementsByName("respuesta1");
  	var questions2 = document.getElementsByName("respuesta2");
  	var questions3 = document.getElementsByName("respuesta3");
  	var questions4 = document.getElementsByName("respuesta4");
  	var questions5 = document.getElementsByName("respuesta5");
  	var questions6 = document.getElementsByName("respuesta6");
  	
  	var seleccion = false;

  	for(var i = 0; i < questions1.length; i++){
            for(var j = 0; j < questions2.length; j++){
                for(var k = 0; k < questions3.length; k++){
                            for(var l = 0; l < questions4.length; l++){
                            	for(var m = 0; m < questions5.length; m++){
                            		for (var n = 0; n < questions6.length; n++) {
                            			                                 
        if(questions1[i].checked && questions2[j].checked && questions3[k].checked && 
        	questions4[l].checked && questions5[m].checked && questions6[n].checked){
            seleccion = true;
            evaluar();
 			    	   }
    			}
			}
		}
                            	}
                            }
    }

	if(!seleccion){
                alert("Responde todas las preguntas");
                return false;
            }
}