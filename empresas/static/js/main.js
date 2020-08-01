$(function(){ 
    var navMain = $(".navbar-collapse"); // avoid dependency on #id
    // "a:not([data-toggle])" - to avoid issues caused
    // when you have dropdown inside navbar
    navMain.on("click", "a:not([data-toggle])", null, function () {
        navMain.collapse('hide');
    });
});

// Animations
//-----------------------------------------------
var delay=0, setTimeoutConst;
if (($("[data-animation-effect]").length>0) && !Modernizr.touch) {
	$("[data-animation-effect]").each(function() {
		var item = $(this),
		animationEffect = item.attr("data-animation-effect");

		if(Modernizr.mq('only all and (min-width: 768px)') && Modernizr.csstransitions) {
			item.appear(function() {
				if(item.attr("data-effect-delay")) item.css("effect-delay", delay + "ms");
				setTimeout(function() {
					item.addClass('animated object-visible ' + animationEffect);

				}, item.attr("data-effect-delay"));
			}, {accX: 0, accY: -130});
		} else {
			item.addClass('object-visible');
		}
	});
};

// Jump To
//-----------------------------------------------
function jumpTo(id) {
	$('html, body').animate({
	    scrollTop: $('#'+id).offset().top - 70
	}, 500);
}

function toggleSideBar(val) {
    // var visible = $('#cart-side-bar').attr('data-toggle');

    // if (visible === true) {
    //     $('#cart-side-bar').attr('data-toggle', false);
    // } else {
    //     $('#cart-side-bar').attr('data-toggle', true);
    // }

    $('#cart-side-bar').attr('data-toggle', val);
    
}


// Carousel multiple
//-----------------------------------------------
$('#recipeCarousel').carousel({
    interval: 10000
})

$('.carousel .carousel-item').each(function(){
    var minPerSlide = 3;
    var next = $(this).next();
    if (!next.length) {
        next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));
    
    for (var i=0;i<minPerSlide;i++) {
        next=next.next();
        if (!next.length) {
            next = $(this).siblings(':first');
        }
        
        next.children(':first-child').clone().appendTo($(this));
    }
});


// Checkout cards
//-----------------------------------------------

// var addressActions = '<div '

$('.address-container').click(function(e){
    if (!$(this).hasClass('active')) {
        $('.address-container').removeClass('active');
        $(this).addClass('active')
    }
})