(window.addPopup = function(e){

	$popup = $('.b-popup-add'),
	$window = $popup.find('.b-popup__window'),
	$addBtn = $('.b-header__add'),
	$overlay = $popup.find('.b-popup__overlay'),
	shownClass = 'b-popup_shown';

	$addBtn.on('click',function(e){
		$.get('/town/PK/article/add',function(html){
			$window.html(html);
		})
		$popup.addClass(shownClass);
		$overlay.height($('body').outerHeight());
		e.preventDefault();
	});

	$overlay.on('click',function(){
		$popup.removeClass(shownClass);
	});
	/*$('.b-popup__window a').on('click',function(){
		$('.b-popup-add').removeClass('b-popup_shown');
	});*/

	$(document).keydown(function(e) {
	    if( e.keyCode === 27 ) {
	        $popup.removeClass(shownClass);
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

	$('.b-header__avatar').on('click',function(e){
		e.stopPropagation();
	})
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