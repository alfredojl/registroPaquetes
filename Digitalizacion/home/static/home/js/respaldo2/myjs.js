function acr(form)
{
	window.location.href = 'index.php?x=search/search&palabra='+form.palabra.value; 
}

/*
$(document).ready(function(){
	
    	$("#boton").click(function(){
        	$("#boton2").click();
    	});
	
		$("#boton2").click(function(){
        	$("#boton2").attr("value","hola");
    	});
	
	
	var i = 2;
var len = cars.length;
var text = "";
for (; i < len; i++) { 
    text += cars[i] + "<br>";
}
});
*/


function Seleccionar(tr, value){
	$(function(){
		if ($("#lib"+value).attr("checked") == "checked"){
			//$("#lib"+value).removeAttr("checked");
			//$("#lib"+value).prop("checked", false);
			$(tr).css("background-color", "#FFFFFF");
		}else{
			$(tr).css("background-color", "#00000");
			
			//$("#Libro"+value).submit();
			//$("#Libro"+value).click();
			//$("#infoLibro").click();
			//("#Libro"+value).trigger("click");
			
			//$("#infoLibro").click();
			//$("#infoLibro").trigger("click");
			//$("#infoLibro").trigger("click");
			$("#Libro"+value).trigger("submit", true);
			$("#infoLibro").trigger("click");
			/*
			$("#infoLibro").on("click", function(){
				$("#Libro"+value).trigger("click");
			});*/
      }
      })
}