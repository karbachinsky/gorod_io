(window.getEnv = function(var_name, default_value) {
    if(typeof(window[var_name]) != 'undefined') {
        return window[var_name];
    }

    if(typeof(default_value) != 'undefined') {
        return default_value;
    }

    return;
});


(window.addPopup = function(e){

	$popup = $('.b-popup-add'),
	$window = $popup.find('.b-popup__window'),
	$addBtn = $('.b-header__add'),
	$overlay = $popup.find('.b-popup__overlay'),
	shownClass = 'b-popup_shown';

    formAjaxUrl = window.getEnv('article_add_url');

	$addBtn.on('click',function(e){
		$.get(formAjaxUrl, function(html){
			$window.html(html);
		})
		$popup.addClass(shownClass);
		$overlay.height($('body').outerHeight());
		e.preventDefault();
	});

    $window.on('submit', 'form', function(e){
        e.preventDefault();

        var data = new FormData($window.find('form')[0]);

        var Deferred = $.ajax({
            url: formAjaxUrl,
            data: data,
            cache: false,
            contentType: false,
            processData: false,
            type: 'POST'
        });

        Deferred.done(function(html){
            $window.html(html);
        });

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
		$header = $('.b-header'),
		$menu = $('.b-header__menu'),
		$topLine = $('.b-header__content'),
		$content = $('.b-js-content');

	$btn.on('click', function(e){
		$header.toggleClass('active');
		return false;
	});

	$topLine.on('click',function(e){
		var time = setTimeout(function(){
			if($header.hasClass('active') && !$(e.target).hasClass('b-header__city') ){
				$header.removeClass('active');
			}
		},50)
	});
	
})();

(window.topScrolling = function(){
	$topLine = $('.b-header__content'),
	$header = $('.b-header'),
	$menu = $('.b-header__menu');

	$('.b-header__avatar').on('click',function(e){
		e.stopPropagation();
	})
	$topLine.on('click',function(e){
		if(!$header.hasClass('active') && !$(e.target).hasClass('b-header__city')){
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