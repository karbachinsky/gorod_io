(window.addPopup = function(e){

	var $popup = $('.b-popup-add'),
	$window = $popup.find('.b-popup__window'),
	$addBtn = $('.b-header__add'),
	$overlay = $popup.find('.b-popup__overlay'),
	shownClass = 'b-popup_shown';
    formAjaxUrl = window.getEnv('articleAddUrl');

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

        var data = new FormData($window.find('form')[0]),
        Deferred = $.ajax({
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

	$(document).keydown(function(e) {
	    if( e.keyCode === 27 ) {
	        $popup.removeClass(shownClass);
	        return false;
	    }
	});


	/*previw*/
	$window.on('click', '.b-form__preview', function(){
		$('.b-form__picture input').click();
	});
	$window.on('change', '.b-form__picture input', function(){
        var files = !!this.files ? this.files : [];
        if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support
 
        if (/^image/.test( files[0].type)){ // only image file
            var reader = new FileReader(); // instance of the FileReader
            reader.readAsDataURL(files[0]); // read the local file
 
            reader.onloadend = function(){ // set image data as background of div
                $('.b-form__preview').css("background-image", "url("+this.result+")");
            }
        }
    });

});
