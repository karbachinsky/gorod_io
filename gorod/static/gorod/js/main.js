(window.addPopup = function(){
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
})();



(window.menu = function(){
	var $btn = $('.b-header__menu-btn'),
		$menu = $('.b-header__menu'),
		$content = $('.b-js-content');

	$btn.on('click', function(){

		$menu.toggleClass('active');

		return false;

	});
	
})();



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


});