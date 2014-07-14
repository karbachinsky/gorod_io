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
(window.ajaxFeed = function(){
	var getData = function(page,limit){
		return $.ajax({
			url : globals.url,
			data : {
				json : 1,
				limit : limit,
				page :page
			}
		});
	},
	appendElems = function(data){	
		var appendedHtml= $(''),
		curElem;

		$.each(data.feed,function(index, elem){
			curElem = $(template(elem));
			appendedHtml = appendedHtml.add(curElem);
		});
		
		$container.append(appendedHtml);
		$container.masonry( 'appended', appendedHtml );
		$container.imagesLoaded( function() {
			$container.masonry();

		});	
		//$('.b-feed__more').show();
	},
	uploadNew = function(){
		getData(curPage,LIMIT).done(appendElems).done(function(data){

			$('.b-feed').height('auto');
			pagesLen = data.total%LIMIT > 0 ? parseInt(data.total/LIMIT)+1 : parseInt(data.total/LIMIT);

			if(curPage+1 < pagesLen){
				$('.b-feed__more').show();
			}else{
				$('.b-feed__more').hide();
			}
			curPage++;
		});
	},
	source   = $("#feed-item-template").html(),
	template = Handlebars.compile(source),
	curPage=0,
	LIMIT = 10,
	$container = $('.b-feed__list'),
	pagesLen;

	
	uploadNew();
	$('.b-feed__more').hide();
	$('.b-feed__more').on('click',function(){
		uploadNew();
	});
	$('.b-feed__list').masonry({
		columnWidth: '.grid-sizer',
		itemSelector: '.b-feed-item',
		gutter : '.gutter-sizer',
		transitionDuration: 0
	});

	

});

(window.loginPopup = function(e){

	var $popup = $('.b-popup-login'),
	$window = $popup.find('.b-popup__window'),
	$loginBtn = $('.b-header__content .b-header__login'),
	$overlay = $popup.find('.b-popup__overlay'),
	shownClass = 'b-popup_shown';

	$loginBtn.on('click',function(e){
		$popup.addClass(shownClass);
		$overlay.height($('body').outerHeight());
		e.preventDefault();
	});

	$overlay.on('click',function(){
		$popup.removeClass(shownClass);
	});

	$(document).keydown(function(e) {
	    if( e.keyCode === 27 ) {
	        $popup.removeClass(shownClass);
	        return false;
	    }
	});

});


$(function(){
	
	
	window.grid();
	window.loginPopup();
	window.addPopup();
	window.menu();
	window.topScrolling();

});