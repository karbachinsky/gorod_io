(window.addPopup = function(e){

	var /*$popup = $('.b-popup-add'),*/
	$window = $('.b-add-form'),
	$addBtn = $('.add-form-btn'),
    $header = $('.b-header'),
    $wrapper = $('#b-form__wrapper'),
    $editLink  = $('.edit-link_article'),
	shownClass = 'b-popup_shown',
    formAjaxUrls = window.getEnv('formAjaxUrls'),
    name,
    formType,
    $previewTools,
    /*openPopup = function(){
        $popup.addClass(shownClass);
        $('body').addClass('body-block');
    },
    closePopup = function(){
        $popup.removeClass(shownClass);
        $('body').removeClass('body-block');
    },*/


    bindHandlers=function(){
        closeHandlers();
        openHandlers();
        previwHandlers();
        submitFormHadlers();

        //editFormHandlers();
    },


    closeHandlers = function(){
        $wrapper.on('click','.close',function(){
            $wrapper.html('');
        });
    },

    previwHandlers = function(){
        /*previw*/
        $window.on('click', '.b-form__preview, .b-form__change-preview', function(){
            $('.b-form__picture input').click();
        });
        $window.on('click', '.b-form__preview, .b-form__del-preview', function(){
            $('#picture-clear_id').attr('checked', 'checked');
            $('#id_picture').val('');
            $('.b-form__preview').css("background-image", "");
        });
        $window.on('change', '.b-form__picture input', function(){
            var files = !!this.files ? this.files : [];
            if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support
     
            if (/^image/.test( files[0].type)){ // only image file
                var reader = new FileReader(); // instance of the FileReader
                reader.readAsDataURL(files[0]); // read the local file
     
                reader.onloadend = function(){ // set image data as background of div
                    $('.b-form__preview').css("background-image", "url("+this.result+")");

                    $previewTools = $wrapper.find('.b-form__preview-tools');
                    $previewTools.addClass('b-form__preview-tools_active');
                    $('#picture-clear_id').removeAttr('checked');
                }
            }
        });

    },


    openHandlers = function(){
        $addBtn.on('click',function(e){
            url = window.getEnv('articleAddUrl');
            getFormHtml(url, 'add');
            formType = 'add';
        });
    },
    /*editFormHandlers = function(){
        $editLink.on('click',function(){
            url = window.getEnv('articleEditUrl');
            getFormHtml(url, 'edit');
            formType = 'edit';
        });
        $window.on('click', '.b-form__del',function(){
            location.href=window.getEnv('articleDeleteUrl');
        });

    },*/

    getFormHtml = function(url, type){
        $wrapper.html('');

        var data = {};

        if(window.getEnv('rubric')) {
            data['rubric'] = window.getEnv('rubric');
        }

        $.get(url, data, function(html){
            $wrapper.html(html); 
            $wrapper.find('#id_title').attr('placeholder', 'Введите заголовок');

            if(type=='edit' && $('.b-form__prev-picture').text().length){
                $previewTools = $popup.find('.b-form__preview-tools');
                $previewTools.addClass('b-form__preview-tools_active');
                $('.b-form__preview').css("background-image", "url(/media/"+$('.b-form__prev-picture').text()+")");
            }
            if(type=='edit'){
                $popup.find('.b-form__del').show();
            }
        });
        //openPopup();
    },
    

    submitFormHadlers = function(){
        $window.on('submit', 'form', function(e){
            e.preventDefault();
            var url;
            if(formType=='add'){
                url = window.getEnv('articleAddUrl');
            }else  if(formType=='edit'){
                url = window.getEnv('articleEditUrl');
            }
            var data = new FormData($window.find('form')[0]),
            Deferred = $.ajax({
                url: url,
                data: data,
                cache: false,
                contentType: false,
                processData: false,
                type: 'POST'
            });

            $window.find('form>div').removeClass('error');
            $('.b-form__error').remove();

            Deferred.done(formAnswerProcessing);

        });

    },
    formAnswerProcessing = function(json){
        var $elem;
            
        if(json.success){
            location.href=json.article_url;
        }else{
            /*--------------------ERRORS-------------------------*/
            $.each(json.errors,function(index, errorElem){

                if(errorElem[0]=='time'){
                    var timeText = $('<div />').addClass('b-form__time').text(errorElem[1]);
                    $wrapper.html(timeText).append('<i class="b-form__close"></i>');  
                }else{   
                    if(errorElem[0]=='picture'){
                        $elem = $window.find('.b-form__preview-wrapper');
                    }else if(errorElem[0]=='internal'){
                        $elem = $window.find('.b-form__preview-wrapper');
                        //$elem = $elem.add($window.find('.b-form__text'));
                    }else{
                        $elem = $window.find('[name="'+errorElem[0]+'"]').closest('div');
                    }

                    $elem.addClass('error');
                    $.each(errorElem[1],function(index, errorText){
                        $('<span/>').addClass('b-form__error').text(errorText).appendTo($elem);
                    });
                }
            });
        }
    }; 

    
    bindHandlers();

});
