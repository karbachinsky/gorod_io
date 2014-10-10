(function($){
    /*
     * HubAnswer handler
     */
    var HubAnswer = function(){
        var self = this;

        self.defaultErrorMsg = "Произошла неизвестная ошибка. Попробуйте позже!";

        self.$form = $(".b-hubanswer-add__form");
        self.$formError = self.$form.find(".error");
        self.$formSubmitButton = self.$form.find("[type=submit]");
        self.$formInput = self.$form.find("[name=answer]");

        self.bindHandlers();
    };

    /*
     * Returns input selector for current answer objects
     */
    HubAnswer.prototype.getInput = function() {
        var self = this;
        return self.$formInput;
    };

    HubAnswer.prototype.bindHandlers = function() {
        var self = this;
        self.formHandler();
    };

    /*
     * Bind answer form submit event
     */
    HubAnswer.prototype.formHandler = function() {
        var self = this;

        self.$form.on("submit", function(e){
            e.preventDefault();
            self.$formSubmitButton.attr("disabled", "disabled");

            var addUrl = self.$form.attr('action');
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
     * Process json request from server on success adding.
     *
     * @param {json} json
     *
     */
    HubAnswer.prototype._formSuccessAnswerProcessing = function(json) {
        var self = this;

        location.reload();
    };

   /*
     * Process json request from server on fail adding.
     *
     * @param ...
     * ...
     */
    HubAnswer.prototype._formFailAnswerProcessing = function(jqXHR, textStatus, errorThrown) {
        var self = this;

        var errorText;
        try {
            var error = jQuery.parseJSON(jqXHR.responseText);

            errorText = error['error'][0][1][0];
        }
        catch (e) {
            errorText = self.defaultErrorMsg;
        }
        self.$formError.text(errorText);
        self.$formError.show();
        self.$formSubmitButton.removeAttr("disabled");
    };

    window.HubAnswer = HubAnswer;

})(jQuery);
