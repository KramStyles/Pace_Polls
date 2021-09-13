$(document).ready(function(){

	$('a.avatar-nav-icon').on('click', function(e) {
		e.preventDefault();
		$(".members-nav-dropdown").show();
	});

	$('.nav-overlay').on('click', function(e) {
		e.preventDefault();
		$(".nav-overlay").hide();
		$(".members-nav-dropdown").hide();
	});

	// Hamburger icon
	$('a.hamburger').on('click', function(e) {
		e.preventDefault();
		$('.mobile-nav').fadeToggle(400);
		// $('.menu-overlay').show();
		$(this).toggleClass('is-active');
		$('body').toggleClass('no-scroll');
	});

	// team hamburger icon
	$('.team-dashboard-wrapper nav.dashboard-top .dashboard-top-inner .left a.hamburger').on('click', function(e) {
		e.preventDefault();
		$(this).toggleClass('is-active');
		$('body').toggleClass('team-mobile-nav-active');
	});

	$('.page-wrapper header.page-header .right .order-dropdown a.dropdown-link').on('click', function(e) {
		 e.preventDefault();
		 $(this).addClass('is-active');
		 $(".page-wrapper header.page-header .right .order-dropdown .order-dropdown-menu").show();
	});

});


$(document).on('click touchstart', function (e) {
	if ($(e.target).closest(".polls-list .item-wrapper .item-links-wrapper a.item-link-settings").length === 0) {
		$(".polls-list .item-wrapper .item-links-wrapper .item-dropdown").delay(100).fadeOut(100);
	}
});

$(document).on('click touchstart', function (e) {
	if ($(e.target).closest(".nav-links.members a.avatar-nav-icon").length === 0) {
		$(".nav-links.members .members-nav-menu .members-nav-dropdown").delay(100).fadeOut(100);
	}
});

$(document).on('click touchstart', function (e) {
	if ($(e.target).closest(".page-wrapper header.page-header .right .order-dropdown a.dropdown-link").length === 0) {
		$(".page-wrapper header.page-header .right .order-dropdown .order-dropdown-menu").delay(100).fadeOut(100);
		$('.page-wrapper header.page-header .right .order-dropdown a.dropdown-link').removeClass('is-active');

	}
});
