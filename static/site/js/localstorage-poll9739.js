// store data in localStorage on redirect to signup
function store(){
  var poll_question= document.getElementById("poll_question");
  localStorage.setItem("poll_question", poll_question.value);

  var poll_option_1= document.getElementById("poll_option_1");
  localStorage.setItem("poll_option_1", poll_option_1.value);
  var colour_option_1= document.getElementById("colour_option_1");
  localStorage.setItem("colour_option_1", colour_option_1.value);


  var poll_option_2= document.getElementById("poll_option_2");
  localStorage.setItem("poll_option_2", poll_option_2.value);
  var colour_option_2= document.getElementById("colour_option_2");
  localStorage.setItem("colour_option_2", colour_option_2.value);


  var poll_option_3= document.getElementById("poll_option_3");
  localStorage.setItem("poll_option_3", poll_option_3.value);
  var colour_option_3= document.getElementById("colour_option_3");
  localStorage.setItem("colour_option_3", colour_option_3.value);


  if( $('#poll_option_4').length ) {
    var poll_option_4= document.getElementById("poll_option_4");
    localStorage.setItem("poll_option_4", poll_option_4.value);
    var colour_option_4= document.getElementById("colour_option_4");
    localStorage.setItem("colour_option_4", colour_option_4.value);
  }

  if( $('#poll_option_5').length ) {
    var poll_option_5= document.getElementById("poll_option_5");
    localStorage.setItem("poll_option_5", poll_option_5.value);
    var colour_option_5= document.getElementById("colour_option_5");
    localStorage.setItem("colour_option_5", colour_option_5.value);
  }


  if( $('#poll_option_6').length ) {
    var poll_option_6= document.getElementById("poll_option_6");
    localStorage.setItem("poll_option_6", poll_option_6.value);
    var colour_option_6= document.getElementById("colour_option_6");
    localStorage.setItem("colour_option_6", colour_option_6.value);
  }

  if( $('#poll_option_7').length ) {
    var poll_option_7= document.getElementById("poll_option_7");
    localStorage.setItem("poll_option_7", poll_option_7.value);
    var colour_option_7= document.getElementById("colour_option_7");
    localStorage.setItem("colour_option_7", colour_option_7.value);
  }


  if( $('#poll_option_8').length ) {
    var poll_option_8= document.getElementById("poll_option_8");
    localStorage.setItem("poll_option_8", poll_option_8.value);
    var colour_option_8= document.getElementById("colour_option_8");
    localStorage.setItem("colour_option_8", colour_option_8.value);
  }


  if( $('#poll_option_9').length ) {
    var poll_option_9= document.getElementById("poll_option_9");
    localStorage.setItem("poll_option_9", poll_option_9.value);
    var colour_option_9= document.getElementById("colour_option_9");
    localStorage.setItem("colour_option_9", colour_option_9.value);
  }

  if( $('#poll_option_10').length ) {
    var poll_option_10= document.getElementById("poll_option_10");
    localStorage.setItem("poll_option_10", poll_option_10.value);
    var colour_option_10= document.getElementById("colour_option_10");
    localStorage.setItem("colour_option_10", colour_option_10.value);
  }

  if( $('#poll_option_11').length ) {
    var poll_option_11= document.getElementById("poll_option_11");
    localStorage.setItem("poll_option_11", poll_option_11.value);
    var colour_option_11= document.getElementById("colour_option_11");
    localStorage.setItem("colour_option_11", colour_option_11.value);
  }

  if( $('#poll_option_12').length ) {
    var poll_option_12= document.getElementById("poll_option_12");
    localStorage.setItem("poll_option_12", poll_option_12.value);
    var colour_option_12= document.getElementById("colour_option_12");
    localStorage.setItem("colour_option_12", colour_option_12.value);
  }

  if( $('#poll_option_13').length ) {
    var poll_option_13= document.getElementById("poll_option_13");
    localStorage.setItem("poll_option_13", poll_option_13.value);
    var colour_option_1= document.getElementById("colour_option_13");
    localStorage.setItem("colour_option_13", colour_option_13.value);
  }

  if( $('#poll_option_14').length ) {
    var poll_option_14= document.getElementById("poll_option_14");
    localStorage.setItem("poll_option_14", poll_option_14.value);
    var colour_option_1= document.getElementById("colour_option_14");
    localStorage.setItem("colour_option_14", colour_option_14.value);
  }

  if( $('#poll_option_15').length ) {
    var poll_option_15= document.getElementById("poll_option_15");
    localStorage.setItem("poll_option_15", poll_option_15.value);
    var colour_option_15= document.getElementById("colour_option_15");
    localStorage.setItem("colour_option_15", colour_option_15.value);
  }

  var poll_category= document.getElementById("poll_category");
  localStorage.setItem("poll_category", poll_category.value);


  if ($('#poll_multiple_votes').is(':checked')) {
    var poll_multiple_votes= document.getElementById("poll_multiple_votes");
    localStorage.setItem("poll_multiple_votes", poll_multiple_votes.value);
  }

  if ($('#require_login').is(':checked')) {
    var require_login= document.getElementById("require_login");
    localStorage.setItem("require_login", require_login.value);
  }

  if ($('#enable_comments').is(':checked')) {
    var enable_comments= document.getElementById("enable_comments");
    localStorage.setItem("enable_comments", enable_comments.value);
  }

  if ($('#poll_captcha_enabled').is(':checked')) {
    var poll_captcha_enabled= document.getElementById("poll_captcha_enabled");
    localStorage.setItem("poll_captcha_enabled", poll_captcha_enabled.value);
  }

}


// load data fron localStorage if found
$(document).ready(function(){

	if (localStorage.getItem("poll_question") != null) {
		$('#poll_question').val(localStorage.poll_question);
	}

	if (localStorage.getItem("poll_option_1") != null) {
		$('#poll_option_1').val(localStorage.poll_option_1);
		$('#colour_option_1').val(localStorage.colour_option_1);
		$('.colour-option-button-one').attr("class",localStorage.colour_option_1);

	}

	if (localStorage.getItem("poll_option_2") != null) {
		$('#poll_option_2').val(localStorage.poll_option_2);
		$('#colour_option_2').val(localStorage.colour_option_2);
		$('.colour-option-button-two').attr("class",localStorage.colour_option_2);
	}

	if (localStorage.getItem("poll_option_3") != null) {
		$('#poll_option_3').val(localStorage.poll_option_3);
		$('#colour_option_3').val(localStorage.colour_option_3);
		$('.colour-option-button-three').attr("class",localStorage.colour_option_3);
	}


	if (localStorage.getItem("poll_option_4") != null) {
		var poll_option_4_value = localStorage.getItem('poll_option_4');
		var colour_option_4_value = localStorage.getItem('colour_option_4');
		var html="<div class='input-group' data-id='4'><label for='poll_option_4'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_4' id='poll_option_4'  placeholder='Eg. Option 4' tabindex='5' value='"+poll_option_4_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_4_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_4_value+"' class='colour_input' name='colour_option_4' id='colour_option_4' readonly/></div>";
		$(".poll-options .input-group:last").after(html);

	}


	if (localStorage.getItem("poll_option_5") != null) {
		var poll_option_5_value = localStorage.getItem('poll_option_5');
		var colour_option_5_value = localStorage.getItem('colour_option_5');
		var html="<div class='input-group' data-id='5'><label for='poll_option_5'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_5' id='poll_option_5'  placeholder='Eg. Option 5' tabindex='6' value='"+poll_option_5_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_5_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_5_value+"' class='colour_input' name='colour_option_5' id='colour_option_5' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
	}

	if (localStorage.getItem("poll_option_6") != null) {
		var poll_option_6_value = localStorage.getItem('poll_option_6');
		var colour_option_6_value = localStorage.getItem('colour_option_6');
		var html="<div class='input-group' data-id='6'><label for='poll_option_6'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_6' id='poll_option_6'  placeholder='Eg. Option 6' tabindex='7' value='"+poll_option_6_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_6_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_6_value+"' class='colour_input' name='colour_option_6' id='colour_option_6' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
	}

	if (localStorage.getItem("poll_option_7") != null) {
		var poll_option_7_value = localStorage.getItem('poll_option_7');
		var colour_option_7_value = localStorage.getItem('colour_option_7');
		var html="<div class='input-group' data-id='7'><label for='poll_option_7'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_7' id='poll_option_7'  placeholder='Eg. Option 7' tabindex='8' value='"+poll_option_7_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_7_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_7_value+"' class='colour_input' name='colour_option_7' id='colour_option_7' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
	}

	if (localStorage.getItem("poll_option_8") != null) {
		var poll_option_8_value = localStorage.getItem('poll_option_8');
		var colour_option_8_value = localStorage.getItem('colour_option_8');
		var html="<div class='input-group' data-id='8'><label for='poll_option_8'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_8' id='poll_option_8'  placeholder='Eg. Option 8' tabindex='9' value='"+poll_option_8_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_8_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_8_value+"' class='colour_input' name='colour_option_8' id='colour_option_8' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
	}

	if (localStorage.getItem("poll_option_9") != null) {
		var poll_option_9_value = localStorage.getItem('poll_option_9');
		var colour_option_9_value = localStorage.getItem('colour_option_9');
		var html="<div class='input-group' data-id='9'><label for='poll_option_9'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_9' id='poll_option_9'  placeholder='Eg. Option 9' tabindex='10' value='"+poll_option_9_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_9_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_9_value+"' class='colour_input' name='colour_option_9' id='colour_option_9' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
	}

	if (localStorage.getItem("poll_option_10") != null) {
		var poll_option_10_value = localStorage.getItem('poll_option_10');
		var colour_option_10_value = localStorage.getItem('colour_option_10');
		var html="<div class='input-group' data-id='10'><label for='poll_option_10'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_10' id='poll_option_10'  placeholder='Eg. Option 10' tabindex='11' value='"+poll_option_10_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_10_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_10_value+"' class='colour_input' name='colour_option_10' id='colour_option_10' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
	}

	if (localStorage.getItem("poll_option_11") != null) {
		var poll_option_11_value = localStorage.getItem('poll_option_11');
		var colour_option_11_value = localStorage.getItem('colour_option_11');
		var html="<div class='input-group' data-id='11'><label for='poll_option_11'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_11' id='poll_option_11'  placeholder='Eg. Option 11' tabindex='12' value='"+poll_option_11_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_11_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_11_value+"' class='colour_input' name='colour_option_11' id='colour_option_11' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
	}


	if (localStorage.getItem("poll_option_12") != null) {
		var poll_option_12_value = localStorage.getItem('poll_option_12');
		var colour_option_12_value = localStorage.getItem('colour_option_12');
		var html="<div class='input-group' data-id='12'><label for='poll_option_12'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_12' id='poll_option_12'  placeholder='Eg. Option 12' tabindex='13' value='"+poll_option_12_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_12_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_12_value+"' class='colour_input' name='colour_option_12' id='colour_option_12' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
	}

	if (localStorage.getItem("poll_option_13") != null) {
		var poll_option_13_value = localStorage.getItem('poll_option_13');
		var colour_option_13_value = localStorage.getItem('colour_option_13');
		var html="<div class='input-group' data-id='13'><label for='poll_option_13'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_13' id='poll_option_13'  placeholder='Eg. Option 13' tabindex='14' value='"+poll_option_13_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_13_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_13_value+"' class='colour_input' name='colour_option_13' id='colour_option_13' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
	}

	if (localStorage.getItem("poll_option_14") != null) {
		var poll_option_14_value = localStorage.getItem('poll_option_14');
		var colour_option_14_value = localStorage.getItem('colour_option_14');
		var html="<div class='input-group' data-id='14'><label for='poll_option_14'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_14' id='poll_option_14'  placeholder='Eg. Option 14' tabindex='15' value='"+poll_option_14_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_14_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_14_value+"' class='colour_input' name='colour_option_14' id='colour_option_14' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
	}

	if (localStorage.getItem("poll_option_15") != null) {
		var poll_option_15_value = localStorage.getItem('poll_option_15');
		var colour_option_15_value = localStorage.getItem('colour_option_15');
		var html="<div class='input-group' data-id='15'><label for='poll_option_15'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_15' id='poll_option_15'  placeholder='Eg. Option 15' tabindex='16' value='"+poll_option_15_value+"'/><div class='poll-option-group'><div class='upload-image-button'><a href='#' title='Go pro to add an image'><span>Add</span> Image</a></div><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='"+colour_option_15_value+"' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='"+colour_option_15_value+"' class='colour_input' name='colour_option_15' id='colour_option_15' readonly/></div>";
		$(".poll-options .input-group:last").after(html);
		$(".new-field-button").hide();
		$(".max-option-notice").show();
	}

	var poll_multiple_votes_value = localStorage.getItem('poll_multiple_votes');
	var require_login_value = localStorage.getItem('require_login');
	var enable_comments_value = localStorage.getItem('enable_comments');
	var poll_captcha_enabled_value = localStorage.getItem('poll_captcha_enabled');
	var poll_category_value = localStorage.getItem('poll_category');


	$('#poll_category option[value="' + poll_category_value + '"]').prop("selected", "selected");

	if(poll_multiple_votes_value==='1') {
		$("#poll_multiple_votes").prop('checked',true);
	}

	if(require_login_value==='1') {
		$("#require_login").prop('checked',true);
	}

	if(enable_comments_value==='1') {
		$("#enable_comments").prop('checked',true);
	}

	if(poll_captcha_enabled_value==='1') {
		$("#poll_captcha_enabled").prop('checked',true);
	}


  // clear local storage
  $(document).on('click', 'a.delete-stored-data-link', function(e){
    localStorage.clear();
  });



});
