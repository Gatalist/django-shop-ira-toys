(function ($) {
	"use strict";

	/*----------- Menu Activation fix to scroll ------------*/
	$(window).on('scroll', function () {
		if ($(this).scrollTop() > 50) {
			$('.header-sticky').addClass('sticky');
		} else {
			$('.header-sticky').removeClass('sticky');
		}
	});

	/*----------- Off Canvas Menu mobile -----------*/
	$(".off-canvas-btn").on('click', function () {
		$("body").addClass('fix');
		$(".off-canvas-wrapper").addClass('open');
	});

	$(".btn-close-off-canvas,.off-canvas-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".off-canvas-wrapper").removeClass('open');
	});

	/*---------- Cart Plus Minus Button -------------*/
	$('.cart-plus-minus').append(
		'<div class="dec qtybutton"><i class="fa fa-minus"></i></div><div class="inc qtybutton"><i class="fa fa-plus"></i></div>'
	);
	$('.qtybutton').on('click', function () {
		var $button = $(this);
		var oldValue = $button.parent().find('input').val();
		if ($button.hasClass('inc')) {
			var newVal = parseFloat(oldValue) + 1;
		} else {
			// Don't allow decrementing below zero
			if (oldValue > 1) {
				var newVal = parseFloat(oldValue) - 1;
			} else {
				newVal = 1;
			}
		}
		$button.parent().find('input').val(newVal);
	});

	/*---------- Responsive Mobile Menu -----------*/
	//Variables
	var $offCanvasNav = $('.mobile-menu'),
	$offCanvasNavSubMenu = $offCanvasNav.find('.dropdown');
	//Add Toggle Button With Off Canvas Sub Menu
	$offCanvasNavSubMenu.parent().prepend('<span class="menu-expand"><i></i></span>');
	//Close Off Canvas Sub Menu
	$offCanvasNavSubMenu.slideUp();
	//Category Sub Menu Toggle
	$offCanvasNav.on('click', 'li a, li .menu-expand', function(e) {
	var $this = $(this);
	if ( ($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('menu-expand')) ) {
		e.preventDefault();
		if ($this.siblings('ul:visible').length){
			$this.parent('li').removeClass('active');
			$this.siblings('ul').slideUp();
		} else {
			$this.parent('li').addClass('active');
			$this.closest('li').siblings('li').removeClass('active').find('li').removeClass('active');
			$this.closest('li').siblings('li').find('ul:visible').slideUp();
			$this.siblings('ul').slideDown();
		}
	}
	});

	/*---------- Carousel - Home Slider -----------*/
	var intro11Slider = new Swiper('.intro11-slider', {
        loop: true,
        speed: 400,
		slidesPerView: 1,
        spaceBetween: 10,
		effect: 'fade',
        navigation: {
            nextEl: '.home1-slider-next',
            prevEl: '.home1-slider-prev',
		},
		pagination: {
			el: '.swiper-pagination',
			type: 'bullets',
			clickable: 'true',
		},
		
	});

	/*-------- Carousel - Новинки -----------*/
	var intro11Slider = new Swiper('.product-slider', {
		slidesPerView: 1,
		spaceBetween: 10,
		pagination: {
			el: '.swiper-pagination',
			type: 'bullets',
			clickable: 'true',
		},
		//autoplay: {},
		// Responsive breakpoints
		breakpoints: {
			// when window width is >= 320px
			320: {
			  slidesPerView: 1,
			  spaceBetween: 10
			},
			// when window width is >= 480px
			480: {
			  slidesPerView: 2,
			  spaceBetween: 10
			},
			// when window width is >= 767px
			768: {
			  slidesPerView: 3,
			  spaceBetween: 10
			},
			// when window width is >= 1200px
			1200: {
				slidesPerView: 4,
				spaceBetween: 10
			},
		}
	});

	/*------ Carousel - отзывы на главной -----------*/
	var intro11Slider = new Swiper('.testimonial-carousel', {
        loop: true,
        speed: 800,
		slidesPerView: 1,
        spaceBetween: 10,
		effect: 'slide',
        navigation: {
            nextEl: '.home1-slider-next',
            prevEl: '.home1-slider-prev',
		},
		autoplay: {},
	});

	/*----------- Slider-слайдер на продукте --------*/
	var galleryThumbs = new Swiper('.single-product-thumb', {
		spaceBetween: 10,
		slidesPerView: 4,
		loop: false,
		freeMode: true,
		loopedSlides: 5, //looped slides should be the same
		watchSlidesVisibility: true,
		watchSlidesProgress: true,
		// Responsive breakpoints
		breakpoints: {
			// when window width is >= 320px
			320: {
			  slidesPerView: 3,
			},
			// when window width is >= 767px
			767: {
			  slidesPerView: 4,
			},
			// when window width is >= 991px
			991: {
				slidesPerView: 3,
			},
			// when window width is >= 1200px
			1200: {
				slidesPerView: 4,
			},
		}
	});

	let galleryTop = new Swiper('.single-product-img', {
		spaceBetween: 10,
		loop: false,
		loopedSlides: 5, //looped slides should be the same
		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},
		thumbs: {
			swiper: galleryThumbs,
		},
	});

	/*------------  Shop Grid Activation  --------------------*/
	$('.shop_toolbar_btn > button').on('click', function (e) {
		e.preventDefault();		
		$('.shop_toolbar_btn > button').removeClass('active');
		$(this).addClass('active');	
		let parentsDiv = $('.shop_wrapper');
		let viewMode = $(this).data('role');
		parentsDiv.removeClass('grid_3 grid_4 grid_5 grid_list').addClass(viewMode);

		if(viewMode == 'grid_3'){
			parentsDiv.children().addClass('col-lg-4 col-md-6 col-sm-6').removeClass('col-lg-3 col-cust-5 col-12');	
		}
		if(viewMode == 'grid_4'){
			parentsDiv.children().addClass('col-lg-3 col-md-6 col-sm-6').removeClass('col-lg-4 col-cust-5 col-sm-6 col-12');
		}
		if(viewMode == 'grid_list'){
			parentsDiv.children().addClass('col-12').removeClass('col-lg-3 col-lg-4 col-md-6 col-sm-6 col-cust-5');
		}
	});
	
	/*-----  Scroll To Top  -----*/	
	function scrollToTop() {
		let $scrollUp = $('.scroll-to-top'),
			$lastScrollTop = 0,
			$window = $(window);

		$window.on('scroll', function () {
			let topPos = $(this).scrollTop();
			if (topPos > $lastScrollTop) {
				$scrollUp.removeClass('show');
			} 
			else {
				if ($window.scrollTop() > 200) {
					$scrollUp.addClass('show');
				} else {
					$scrollUp.removeClass('show');
				}
			}
			$lastScrollTop = topPos;
		});

		$scrollUp.on('click', function (evt) {
			$('html, body').animate({
				scrollTop: 0
			}, 600);
			evt.preventDefault();
		});
	}
	scrollToTop();

	/*-----  Preloader  -----*/	
	$(window).on('load', function () {
		$('#preloader').delay(250).fadeOut('slow')
		$('body').delay(250).css({'overflow':'visible'});
	});

})(jQuery);