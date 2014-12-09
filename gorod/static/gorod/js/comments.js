(window.articleComments = function(e){
    var $commentForm = $('.b-comments__add-form');

    var options = {
        aaaaa: 1,
        formRequestSuccessCallback: function(json) {
            console.log('BLBLB');
            alert('BLBLBLBA');
        }
    };

    $commentForm.Comments(options);

    $(".b-comments-cnt__link").on("click", function(e) {
        $(".b-comments").slideDown(function(){
            $(this).addClass('active');
        });
    });
});
