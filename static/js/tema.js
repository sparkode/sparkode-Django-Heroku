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


$(function() {
    $( "#draggable2" ).draggable({ revert: "valid" });
    $( "#draggable1" ).draggable({ revert: "invalid" });
    $( "#draggable4" ).draggable({ revert: "valid" });
    $( "#draggable3" ).draggable({ revert: "invalid" });
    $( "#draggable6" ).draggable({ revert: "valid" });
    $( "#draggable5" ).draggable({ revert: "invalid" });
    $( "#draggable8" ).draggable({ revert: "valid" });
    $( "#draggable7" ).draggable({ revert: "invalid" });
    $( "#draggable10" ).draggable({ revert: "valid" });
    $( "#draggable9" ).draggable({ revert: "invalid" });
    $( "#draggable12" ).draggable({ revert: "valid" });
    $( "#draggable11" ).draggable({ revert: "invalid" });
    $( "#droppable" ).droppable({
      classes: {
        "ui-droppable-active": "ui-state-active",
        "ui-droppable-hover": "ui-state-hover"
      },
      drop: function( event, ui ) {
        $( this )
          .addClass( "ui-state-highlight" )
          .find( "p" )
            .html( "Correcto" );
      }
    });
  } );




