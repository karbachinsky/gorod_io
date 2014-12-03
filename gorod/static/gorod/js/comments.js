(window.articleComments = function(e){
    var $commentForm = $('.b-comments__add-form');
    $commentForm.Comments();

    $(".b-comments-cnt__link").on("click", function(e) {
        $(".b-comments").slideDown(function(){
            $(this).addClass('active');
        });
    });
});
