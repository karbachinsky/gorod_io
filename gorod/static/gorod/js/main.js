(window.addPopup = function(){
	$('.b-header__add').on('click',function(){
		$('.b-popup-add').addClass('b-popup_shown');
		return false;
	});

	$('.b-popup-add .b-popup__overlay').on('click',function(){
		$('.b-popup-add').removeClass('b-popup_shown');
	});
})();

(window.menu = function(){
	var $btn = $('.b-header__menu-btn i'),
		$menu = $('.b-header__menu');

	$btn.on('click', function(){
		$menu.addClass('active');
		var docHeight = $(document).height(),
			menuPadding = parseInt($menu.css('paddingTop')) + parseInt($menu.css('paddingBottom'));
			menuHeight = docHeight - menuPadding;

		$menu.height(menuHeight);

		return false;

	});
	$(document).on('click', function(e) {
		$self = $(e.target);
		if($menu.hasClass('active') && !($self.closest('.b-header__menu').length )) {
			$menu.removeClass('active');
		}
	});
	$(window).resize(function(){
		$menu.removeClass('active');
		$menu.height('auto');
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