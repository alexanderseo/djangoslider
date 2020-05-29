 $(document).ready(function(){
		  $('.items:not(.noslide)').bxSlider({
			slideWidth: 350,
			minSlides: 2,
			maxSlides: 6,
			slideMargin: 10,
			infiniteLoop:false
		  });
		  
		  $('.slides').bxSlider({
			  mode: 'fade',
			  captions: true
		   });
		   
		 
			
			var tabContainers = $('.wrapper > div'); // получаем массив контейнеров
			tabContainers.hide().filter(':first').show(); // прячем все, кроме первого
			// далее обрабатывается клик по вкладке
			$('ul.portfolio_tabs li a').click(function () {
				tabContainers.hide(); // прячем все табы
				tabContainers.filter(this.hash).fadeIn(); // показываем содержимое текущего
				$('ul.portfolio_tabs li a').removeClass('active'); // у всех убираем класс 'selected'
				$(this).addClass('active'); // текушей вкладке добавляем класс 'selected'
				return false;
			}).filter(':first').click();
			
			$('.open_popup').click(function() {
				var popup_id = $('#' + $(this).attr("rel"));
				$(popup_id).show();
				$('.overlay').fadeIn();
			})
			$('.popup .close, .overlay, .lost_pass').click(function() {
				$('.overlay, .popup').fadeOut();
			})
			
			
			$('.lost_pass').click(function() {
				var popup_id = $('#' + $(this).attr("rel"));
				$(popup_id).show();
				$('.overlay').fadeIn();
			})
			
			
			$(".fancybox-thumb").fancybox({
				prevEffect	: 'none',
				nextEffect	: 'none',
				helpers	: {
					title	: {
						type: 'outside'
					},
					thumbs	: {
						width	: 100,
						height	: 100
					}
				}
			});
			
			
			$('ul.list_reviews li').hover(
				function() {
					$(this).addClass("active");
				},
				function() {
					$(this).removeClass("active");        
				}
			);
			
			$('a.togle').click(function() {
				  $("ul.list_reviews li.active .full_reviews").slideToggle("slow");
				  $(this).toggleClass("t-active");
			})
			
			
		 
    
	});