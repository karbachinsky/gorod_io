(window.articleComments = function(e){

	if (location.hash != "#comments-cnt") {
        $(".b-comments-cnt__link").on("click", function(e) {
            $(".b-article__comments").show();
            //e.preventDefault();
        });
    }
    else {
        // Scroll to last
        $(".b-article__comments").show();
        $(location).attr('hash', "#" + $(".b-comment:last a").attr("name"));
    }

    var comments = new Comments();

});
