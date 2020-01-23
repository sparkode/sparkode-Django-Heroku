$(document).ready(function()
	{
		var altura= $('.menu').offset().top;

		$(window).on('scroll',function()
						{
							if ($(window).scrollTop()>altura)
							{
								$('.menu').addClass('menu-fixed');
							}
							else
							{
								$('.menu').removeClass('menu-fixed');
							}
						}
					);
	});


$( function() {
    $( "#draggable2" ).draggable({ revert: "invalid" });
    $( "#draggable1" ).draggable({ revert: "invalid" });
    $( "#draggable4" ).draggable({ revert: "invalid" });
    $( "#draggable3" ).draggable({ revert: "invalid" });
    $( "#draggable6" ).draggable({ revert: "invalid" });
    $( "#draggable5" ).draggable({ revert: "invalid" });
    $( "#draggable8" ).draggable({ revert: "valid" });
    $( "#draggable7" ).draggable({ revert: "valid" });
    $( "#draggable10" ).draggable({ revert: "valid" });
    $( "#draggable9" ).draggable({ revert: "valid" });
    $( "#draggable12" ).draggable({ revert: "valid" });
    $( "#draggable11" ).draggable({ revert: "valid" });
    $( "#draggable13" ).draggable({ revert: "valid" });
    $( "#draggable14" ).draggable({ revert: "invalid" });
    $( "#draggable15" ).draggable({ revert: "invalid" });
    $( "#temp2" ).droppable({
      classes: {
        "ui-droppable-active": "ui-state-active",
        "ui-droppable-hover": "ui-state-hover"
      }
    });
  } );

