(window.ajaxFeed = function(){
	var getData = function(page,limit){
		return $.ajax({
			url : '/api/feed/',
			data : {
				limit : limit,
				page : page,
				city : globals.cityName,
				rubric : globals.rubric,
				user : globals.profileUserId
			}
		});
	},
	appendElems = function(data){	
		var appendedHtml= $(''),
		curElem;

		$.each(data.feed,function(index, elem){
			curElem = $(template(elem));
			appendedHtml = appendedHtml.add(curElem);
		});
		
		$container.append(appendedHtml);
		$container.masonry( 'appended', appendedHtml );
		$container.imagesLoaded( function() {
			$container.masonry();

		});	
		//$('.b-feed__more').show();
	},
	uploadNew = function(){
		getData(curPage,LIMIT).done(appendElems).done(function(data){

			$('.b-feed').height('auto');
			pagesLen = data.total%LIMIT > 0 ? parseInt(data.total/LIMIT)+1 : parseInt(data.total/LIMIT);

			if(curPage+1 < pagesLen){
				$('.b-feed__more').show();
			}else{
				$('.b-feed__more').hide();
			}
			curPage++;
		});
	},
	source   = $("#feed-item-template").html(),
	template = Handlebars.compile(source),
	curPage=0,
	LIMIT = 20,
	$container = $('.b-feed__list'),
	pagesLen;

	
	uploadNew();
	$('.b-feed__more').hide();
	$('.b-feed__more').on('click',function(){
		uploadNew();
	});
	$('.b-feed__list').masonry({
		columnWidth: '.grid-sizer',
		itemSelector: '.b-feed-item',
		gutter : '.gutter-sizer',
		transitionDuration: 0
	});
});

