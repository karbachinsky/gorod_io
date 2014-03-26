$(function(){
	
	$('.b-feed__list').imagesLoaded( function() {
		$('.b-feed__list').masonry({
		  columnWidth: '.grid-sizer',
		  itemSelector: '.b-feed-item',
		  gutter : '.gutter-sizer'
		});
	});
	$('.b-orgs__list').masonry({
	  columnWidth: '.grid-sizer',
	  itemSelector: '.b-orgs__item',
	  gutter : '.gutter-sizer'
	});
});