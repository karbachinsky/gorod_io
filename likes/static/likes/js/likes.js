/*
 * Like class
 * Author: I. Karbachinsky <igorkarbachinsky@mail.ru> 10.2014
 */

(function($){
    // FIXME, use jquery cookie :)
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    /*
     * Like handler
     * @param {Jquery Object} selector for likes
     * @param {Object} additional options:
     */
    var Like = function($likeBlock, options){
        var self = this;

        self.options = {
            like: true,
            dislike: true,
            requestSuccessCallback: function () { self._defaultRequestSuccessCallback.apply(self, arguments); },
            requestFailCallback: function () { self._defaultRequestFailCallback.apply(self, arguments); },
        };

        $.extend(self.options, options);

        self.likeClass = 'like';
        self.dislikeClass = 'dislike';
        self.raitingClass = 'raiting';

        self.$likeBlock = $likeBlock;

        self.raiting = parseInt($likeBlock.data('raiting')) || 0;
        self.was_already_liked = Boolean($likeBlock.data('was-already-liked'));

        // force hide like buttons if was already liked
        if (self.was_already_liked) {
            self.options['like'] = self.options['dislike'] = false;
        }

        // Prevent multiple clicking
        self.isLocked = false;

        self.appendHTMLSceleton();
        self.bindHandlers();

        self._colorRaitingBlock();
    };

    /*
     * Adds necessary html sceleton to likeBlock
     */
    Like.prototype.appendHTMLSceleton = function() {
        var self = this;

        // Adding like button
        if (self.options.like) {
            $("<span>").addClass(self.likeClass)
                       .text('+')
                       .appendTo(self.$likeBlock);
            self.$likeButton = self.$likeBlock.find('.' + self.likeClass);
        }

        // Adding raiting
        $("<span>").addClass(self.raitingClass)
                       .text(self.raiting)
                       .appendTo(self.$likeBlock);

        self.$raitingBlock = self.$likeBlock.find('.' + self.raitingClass);

        // Adding dislike button
        if (self.options.dislike) {
            $("<span>").addClass(self.dislikeClass)
                       .text('-')
                       .appendTo(self.$likeBlock);
            self.$dislikeButton = self.$likeBlock.find('.' + self.dislikeClass);
        }
    };

    /*
     * Bind all necessary events
     */
    Like.prototype.bindHandlers = function() {
        var self = this;

        if (self.options.like) {
            self._bindButton(self.$likeButton, true);
        }
        if (self.options.dislike) {
            self._bindButton(self.$dislikeButton, false);
        }
    };

    /*
     * Bind one certain button
     * @param {Jquery selector} button
     * @param {Boolean} is_positive_like
     */
    Like.prototype._bindButton = function($button, is_positive_like) {
        var self = this;

        $button.on("click", function(e){
            e.preventDefault();

            if (self.isLocked) {
                //return;
            }

            self.isLocked = true;

            var data = {
                is_positive: is_positive_like,
                csrfmiddlewaretoken: getCookie('csrftoken'), // window.getEnv('csrfToken')
                object_pk: self.$likeBlock.data('object-pk'),
                content_type: self.$likeBlock.data('content_type')
            };

            var Deferred = $.ajax({
                url: window.getEnv('likeAddUrl'),
                data: data,
                type: 'POST',
                dataType: "json"
                //processData: false,
			    //cache: false,
			    //contentType: false
            });

            Deferred.done(function(json) {
                self.options.requestSuccessCallback($button, json);
            });
            Deferred.fail(function(jqXHR, textStatus, errorThrown) {
                self.options.requestFailCallback($button, jqXHR, textStatus, errorThrown);
            });
        });
    };

    /*
     * Default processing json request from server on success like adding.
     * @param {jQuery Object} button
     * @param {Json} server response
     */
    Like.prototype._defaultRequestSuccessCallback = function($button, json) {
        var self = this;

        if ($button.hasClass(self.likeClass)) {
            self.raiting++;
        }
        else {
            self.raiting--;
        }

        if (self.$likeButton) self.$likeButton.hide();
        if (self.$dislikeButton) self.$dislikeButton.hide();

        self.$raitingBlock.text(self.raiting);
        self._colorRaitingBlock();
    };

    /*
     * Adds special classes: negative, positive, neitral to raiting block depending on raiting's value.
     */
    Like.prototype._colorRaitingBlock = function() {
        var self = this;

        var colorClass = 'neitral-like';

        if (self.raiting > 0) {
            colorClass = 'positive-like';
        }
        else if (self.raiting < 0) {
            colorClass = 'negative-like';
        }

        self.$raitingBlock.removeClass('neitral-like')
                          .removeClass('negative-like')
                          .removeClass('positive-like');

        self.$raitingBlock.addClass(colorClass);
    };


   /*
     * Process json request from server on fail like adding.
     * @param ...
     */
    Like.prototype._defaultRequestFailCallback = function($button, jqXHR, textStatus, errorThrown) {
        var self = this;
        // Do something here
    };

    /**
     * Wrapper for JQuery
     * @param {Objeet} params
     * @return BlockScrollSlider object
     */
    $.fn.Like = function(options) {
        var self = this;

        var likes = [];
        self.each(function() {
            if($.trim($(this).html())==''){
                likes.push(
                    new Like($(this), options)
                );
            }
        });

        return likes;
    };

})(jQuery);
