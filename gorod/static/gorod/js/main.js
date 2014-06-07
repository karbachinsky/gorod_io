(window.addPopup = function(e){
	$('.b-header__add').on('click',function(){
		$('.b-popup-add').addClass('b-popup_shown');
		return false;
	});

	$('.b-popup-add .b-popup__overlay').on('click',function(){
		$('.b-popup-add').removeClass('b-popup_shown');
	});
	$('.b-popup__window a').on('click',function(){
		$('.b-popup-add').removeClass('b-popup_shown');
	});

	$(document).keydown(function(e) {
	    if( e.keyCode === 27 ) {
	        $('.b-popup-add').removeClass('b-popup_shown');
	        return false;
	    }
	});

})();



(window.menu = function(){
	var $btn = $('.b-header__menu-btn'),
		$menu = $('.b-header__menu'),
		$topLine = $('.b-header__content'),
		$content = $('.b-js-content');

	$btn.on('click', function(e){
		$menu.toggleClass('active');
		return false;
	});

	$topLine.on('click',function(e){
		var time = setTimeout(function(){
			if($menu.hasClass('active') && !$(e.target).hasClass('b-header__city') ){
				$menu.removeClass('active');
			}
		},50)
	});
	
})();

(window.topScrolling = function(){
	$topLine = $('.b-header__content'),
	$menu = $('.b-header__menu');

	$topLine.on('click',function(e){
		if(!$menu.hasClass('active') && !$(e.target).hasClass('b-header__city')){
			$('body').animate({scrollTop:0},300);
		}
	});

});


$(function(){
	
	$('.b-feed__list').imagesLoaded( function() {
		$('.b-feed__list').masonry({
			columnWidth: '.grid-sizer',
			itemSelector: '.b-feed-item',
			gutter : '.gutter-sizer',
			transitionDuration: 0
		});
	});
	$('.b-orgs__list').masonry({
		columnWidth: '.grid-sizer',
		itemSelector: '.b-orgs__item',
		gutter : '.gutter-sizer',
		transitionDuration: 0
	});

	window.addPopup();
	window.menu();
	window.topScrolling();

});