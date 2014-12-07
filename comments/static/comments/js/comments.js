(function($){
    /*
     * Comments handler
     */
    var Comments = function($commentForm, options){
        var self = this;

        console.log('options', options);

        self.options = {
            like: true,
            dislike: true,
            defaultErrorMsg: "Произошла неизвестная ошибка. Попробуйте позже!",
            formRequestSuccessCallback: function () { self._defaultFormSuccessAnswerProcessing.apply(self, arguments); },
            formRequestFailCallback: function () { self._defaultFormFailAnswerProcessing.apply(self, arguments); }
        };

        $.extend(self.options, options);

        self.$commentForm = $commentForm;
        self.$commentFormError = self.$commentForm.find(".error");
        self.$commentFormSubmitButton = self.$commentForm.find("[type=submit]");
        self.$commentFormInput = self.$commentForm.find("[name=comment]");

        self.bindHandlers();
    };

    /*
     * Returns input selector for current comments objects
     */
    Comments.prototype.getInput = function() {
        var self = this;
        return self.$commentFormInput;
    };

    Comments.prototype.bindHandlers = function() {
        var self = this;
        self.formHandler();
    };

    /*
     * Bind comment add form submit event
     */
    Comments.prototype.formHandler = function() {
        var self = this;

        self.$commentForm.on("submit", function(e){
            e.preventDefault();
            self.$commentFormSubmitButton.attr("disabled", "disabled");

            var addUrl = window.getEnv('commentAddUrl');
            var data = new FormData($(this).get(0));

            var Deferred = $.ajax({
                url: addUrl,
                data: data,
                type: 'POST',
                dataType: "json",
                processData: false,
			    cache: false,
			    contentType: false
            });

            Deferred.done(function(json) {
                        self.options.formRequestSuccessCallback(json);
                    })
                    .fail(function(jqXHR, textStatus, errorThrown) {
                        self.options.formRequestFailCallback(jqXHR, textStatus, errorThrown);
                    });

        });
    };

    /*
     * Default json response processing from server on success comment adding.
     *
     * @param {json} json
     *
     */
    Comments.prototype._defaultFormSuccessAnswerProcessing = function(json) {
        var self = this;

        location.reload();
    };

   /*
     * Process json request from server on fail comment adding.
     *
     * @param ...
     * ...
     */
    Comments.prototype._defaultFormFailAnswerProcessing = function(jqXHR, textStatus, errorThrown) {
        var self = this;

        var errorText;
        try {
            var error = jQuery.parseJSON(jqXHR.responseText);

            errorText = error['error'][0][1][0];
        }
        catch (e) {
            errorText = self.options.defaultErrorMsg;
        }
        self.$commentFormError.text(errorText);
        self.$commentFormError.show();
        self.$commentFormSubmitButton.removeAttr("disabled");
    };

    window.Comments = Comments;

    /**
     * Wrapper for JQuery
     * @param {Object} params
     * @param {Object} options
     * @return Comments object
     */
    $.fn.Comments = function(options) {
        var self = this;

        console.log('opop', arguments);

        var commentsObjs = [];
        self.each(function() {
            commentsObjs.push(
                new Comments($(this), options)
            );
        });

        return commentsObjs;
    };


})(jQuery);
