$(document).ready(function(){
	$('.toggle-btn').click(function(){
		$('.sidebar').toggleClass('active');
		$('.content').toggleClass('active');
		$('.text').toggleClass('active');
		$('.toggle-btn').toggleClass('toggle');
	})
})

