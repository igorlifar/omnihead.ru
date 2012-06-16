$(document).ready(function() {
   
    $('a.scroll-top').click(function(){
    	console.log("test")
        $('html, body').animate({scrollTop:0}, 'slow');
        return false;
    });

	$(".scroll").click(function(event){		
		event.preventDefault();
		$('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);
	});
});