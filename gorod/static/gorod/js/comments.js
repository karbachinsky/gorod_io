(window.articleComments = function(e){
    var comments = new Comments();
    $(".b-comments-cnt__link").on("click", function(e) {
        $(".b-comments").slideDown(function(){
            $(this).addClass('active');
        });
    });
});
