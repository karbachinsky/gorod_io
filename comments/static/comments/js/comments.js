(function($){
    /*
     * Comments handler
     */
    var Comments = function(){
        var self = this;

        self.defaultErrorMsg = "Произошла неизвестная ошибка. Попробуйте позже!";

        self.$commentForm = $(".b-comments__add-form");
        self.$commentFormError = self.$commentForm.find(".error");
        self.$commentFormSubmitButton = $(this).find("[type=submit]");

        self.bindHandlers();
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
                        self._formSuccessAnswerProcessing(json);
                    })
                    .fail(function(jqXHR, textStatus, errorThrown) {
                        self._formFailAnswerProcessing(jqXHR, textStatus, errorThrown);
                    });

        });
    };

    /*
     * Process json request from server on success comment adding.
     *
     * @param {json} json
     *
     */
    Comments.prototype._formSuccessAnswerProcessing = function(json) {
        var self = this;

        location.reload();
    };

   /*
     * Process json request from server on fail comment adding.
     *
     * @param ...
     * ...
     */
    Comments.prototype._formFailAnswerProcessing = function(jqXHR, textStatus, errorThrown) {
        var self = this;

        var error = jQuery.parseJSON(jqXHR.responseText);

        var errorText = error ? error['error'][0][1][0] : defaultErrorMsg;

        self.$commentFormError.text(errorText);
        self.$commentFormError.show();
        self.$commentFormSubmitButton.removeAttr("disabled");
    };

    window.Comments = Comments;

})(jQuery);
