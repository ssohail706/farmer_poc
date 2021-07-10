$(document).ready(function() {
	// Side Navigation Open Close
	$('.side-nav-icon-close').click(function(){
		$('#sideNavigation').css("left", "-250px");
		$("#main").css("marginLeft", "0px");
		$('.side-nav-icon').css("display","block");
		$('.side-nav-icon-close').css("display","none");
	});
	$('.side-nav-icon').click(function(){
		$('#sideNavigation').css("left", "0px");
		$("#main").css("marginLeft", "270px");
		$('.side-nav-icon').css("display","none");
		$('.side-nav-icon-close').css("display","block");
	});

	// small screen
	$('.side-nav-icon-close-sm').click(function(){
		$('#sideNavigation').css("left", "-250px");
		$("#main").css("marginLeft", "0px");
		$('.side-nav-icon-sm').css("display","block");
		$('.side-nav-icon-close-sm').css("display","none");
	});
	$('.side-nav-icon-sm').click(function(){
		$('#sideNavigation').css("left", "0px");
		$("#main").css("marginLeft", "270px");
		$('.side-nav-icon-sm').css("display","none");
		$('.side-nav-icon-close-sm').css("display","block");
	});


	// Toggle active class
	$(function() {
		$(".side-menu-item").click(function() {
	      $(".side-menu-item").removeClass("active");
	      $(".side-menu-item").removeClass("animated");
	      $(".side-menu-item").removeClass("fadeInLeft");
	      $(this).addClass("active");
	      $(this).addClass("animated");
	      $(this).addClass("fadeInLeft");
  		});
	});

	$(".rotate-menu1").click(function(){
		$("#manageLeave").slideUp();
		$("#manageTimesheet").slideUp();
		$("#manageUser").slideToggle();
		$(this).toggleClass("down");
		$(".rotate-menu2").removeClass("down");
	});
	$(".rotate-menu2").click(function(){
		$("#manageUser").slideUp();
		$("#manageTimesheet").slideUp();
		$("#manageLeave").slideToggle();
		$(this).toggleClass("down");
		$(".rotate-menu1").removeClass("down");
	});
	$(".rotate-menu3").click(function(){
		$("#manageLeave").slideUp();
		$("#manageUser").slideUp();
		$("#manageTimesheet").slideToggle();
		$(this).toggleClass("down");
		$(".rotate-menu2").removeClass("down");
		$(".rotate-menu1").removeClass("down");
	});
});
