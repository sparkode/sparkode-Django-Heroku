$(document).ready(main);

var contador=1;

function main()
{

	$('.menu_btn').click(function()
	{
		
		if(contador==1)
		{
			$('.menud').animate({
				left:'0'
			});
			contador=0;
			document.getElementById("hiddenMe").style.display = "none";
		}
		else
		{
			contador=1;
			$('.menud').animate({
				left:'-100%'
			});
			document.getElementById("hiddenMe").style.display = "";
		}
	});
}