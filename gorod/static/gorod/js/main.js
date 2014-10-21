(window.getEnv = function(var_name, default_value) {
    if(typeof(globals[var_name]) != 'undefined') {
        return globals[var_name];
    }

    if(typeof(default_value) != 'undefined') {
        return default_value;
    }

    return;
});

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
	
});

(window.topScrolling = function(){
	var $topLine = $('.b-header__content'),
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

(window.grid = function(){
	/*$('.b-feed__list').imagesLoaded( function() {
		$('.b-feed__list').masonry({
			columnWidth: '.grid-sizer',
			itemSelector: '.b-feed-item',
			gutter : '.gutter-sizer',
			transitionDuration: 0
		});
	});*/

	$('.b-orgs__list').masonry({
		columnWidth: '.grid-sizer',
		itemSelector: '.b-orgs__item',
		gutter : '.gutter-sizer',
		transitionDuration: 0
	});
});


(window.loginPopup = function(e){

	var $popup = $('.b-popup-login'),
	$window = $popup.find('.b-popup__window'),
	$loginBtn = $('.b-header__login, .login-link'),
	shownClass = 'b-popup_shown',
	openPopup = function(e){
		$popup.addClass(shownClass);
		e.preventDefault();
		$('body').addClass('body-block');
	},
	closePopup = function(){
		$popup.removeClass(shownClass);
		$('body').removeClass('body-block');
	};

	$loginBtn.on('click',function(e){
        e.preventDefault();
        $('.b-header').removeClass('active');
		openPopup(e);
	});

	$popup.on('click',function(e){
		if($(e.target).hasClass('b-popup-login')){
            closePopup();
        }
	});

	$(document).keydown(function(e) {
	    if( e.keyCode === 27 ) {
	        closePopup();
	        return false;
	    }
	});

    // Click on login using simple login
    $popup.find('.login-gorod').on('click', function() {
        $(this).hide();
        $popup.find('.b-auth').show();
    });

    // Login-password auth. FIXME!
    $authForm = $popup.find('.b-auth__form');
    $authFormError = $popup.find('.b-auth__error');

    $authForm.on('submit', function(e) {
        e.preventDefault();
        var data = new FormData($(this).get(0));
        var Deferred = $.ajax({
            url: $(this).attr('action'),
            data: data,
            type: 'POST',
            dataType: "json",
            processData: false,
            cache: false,
            contentType: false
        });

        Deferred.done(function(json) {
            location.reload();
        });
        Deferred.fail(function(jqXHR, textStatus, errorThrown) {
            var errorText;
            try {
                var error = jQuery.parseJSON(jqXHR.responseText);

                errorText = error['error'][0][1][0];
            }
            catch (e) {
                errorText = self.defaultErrorMsg;
            }
            $authFormError.text(errorText);
        });

    });

});


$(function(){

	window.grid();
	window.loginPopup();
	window.addPopup();
	window.menu();
	window.topScrolling();
});