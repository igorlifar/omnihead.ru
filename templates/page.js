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


	$('#contact-form a').click(function() {
		$("#contact-form").addClass("loading");
		$.ajax({
			url: '/feedback/',
			type: 'POST',
			data: $("#contact-form").serialize(),
			success: function(data) {
				var res = $.evalJSON(data);
				$("#contact-form").removeClass("loading");

				fields = ['author', 'email', 'message']
				var cnt = 0;

				for (var i = 0; i < fields.length; i++) {
					var field = fields[i]
					if (field in res.errors) {
						$("li." + field).addClass('error');
						cnt++;
					} else {
						$("li." + field).removeClass('error');
					}
				}

				if (cnt == 0) {
					$("#contact-form").fadeOut('fast', function() {
						$("#feedback-sent").fadeIn('fast');
					});
				}

			}
		})
	});

});