(window.addPopup = function(){
	$('.b-header__add').on('click',function(){
		$('.b-popup-add').addClass('b-popup_shown');
		return false;
	});

	$('.b-popup-add .b-popup__overlay').on('click',function(){
		$('.b-popup-add').removeClass('b-popup_shown');
	});
})();



$(function(){
	
	$('.b-feed__list').imagesLoaded( function() {
		$('.b-feed__list').masonry({
		  columnWidth: '.grid-sizer',
		  itemSelector: '.b-feed-item',
		  gutter : '.gutter-sizer'
		});
	});
	$('.b-orgs__list').masonry({
	  columnWidth: '.grid-sizer',
	  itemSelector: '.b-orgs__item',
	  gutter : '.gutter-sizer'
	});

	addPopup();


});