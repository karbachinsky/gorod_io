(window.articleComments = function(e){

    var comments = new Comments();

	/*if (location.hash != "#comments-cnt") {
        $(".b-comments-cnt__link").on("click", function(e) {
            $(".b-article__comments").show();
            comments.getInput().focus();
            //e.preventDefault();
        });
    }
    else {
        // Scroll to last
        $(".b-article__comments").show();
        $(location).attr('hash', "#" + $(".b-comment:last a").attr("name"));
        comments.getInput().focus();
    }*/
    $(".b-comments-cnt__link").on("click", function(e) {
        $(".b-comments").slideDown(function(){
            $(this).addClass('active');
        });
        //comments.getInput().focus();
    });
});
