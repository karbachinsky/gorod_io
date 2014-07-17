(window.addPopup = function(e){

	var $popup = $('.b-popup-add'),
	$window = $popup.find('.b-popup__window'),
	$addBtn = $('.b-header__add'),
	$overlay = $popup.find('.b-popup__overlay'),
    $addList = $('.b-header__add-list'),
    $wrapper = $window.find('#b-form__wrapper'),
	shownClass = 'b-popup_shown',
    formAjaxUrl = window.getEnv('articleAddUrl');

	$addBtn.on('click',function(e){
		$addList.addClass('active');
	});
    $(document).on('click',function(e){
        if( ! $(e.target).hasClass('b-header__add') ){
            $addList.removeClass('active');
        }
    });

    $addList.find('li').on('click',function(e){
        var name  = $(this).attr('data-name'),
        title = $(this).attr('data-title');
        $wrapper.html(''); 
        $wrapper.attr('class','').addClass('b-form__wrapper_'+name);
        $.get(formAjaxUrl, function(html){
            $wrapper.html(html); 
            $wrapper.find('#id_title').attr('placeholder', 'Заголовок');
            $wrapper.find('.b-form__type span').text(title);
            $wrapper.find('#id_rubric').find('option').removeAttr('selected').filter(':contains("'+name+'")').attr("selected", "selected");        
        });
        $popup.addClass(shownClass);
        $overlay.height($('body').outerHeight());
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

        Deferred.done(function(json){
            //$window.html(html);
            var $elem;
            if(!json.success){
            	$.each(json.errors,function(index, elem){
            		$elem = $window.find('[name="'+elem[0]+'"]').closest('div');
            		$.each(elem[1],function(index, errorText){
            			$('<span/>').addClass('b-form__error').text(errorText).appendTo($elem);
            		});
            	});
            }else{
                var okText = $('<div />').addClass('b-form__ok').text('Ваше сообщение будет добавлено после модерации');
            	$window.html(okText).append('<i class="b-form__close"></i>');
            }
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
    $window.on('click', '.b-form__close', function(){
        $popup.removeClass(shownClass);
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
