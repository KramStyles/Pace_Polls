let justAjaxReturn;
$(document).ready(function () {

    // tooltip
    $('.tooltip').tooltipster({
        theme: 'tooltipster-sml',
        maxWidth: '260',
        animation: 'fade',
        delay: 100,
    });

    // remove variable from url
    var uri = window.location.toString();
    if (uri.indexOf("?") > 0) {
        var clean_uri = uri.substring(0, uri.indexOf("?"));
        window.history.replaceState({}, document.title, clean_uri);
    }

    // option colours
    var count = $(".poll-options .input-group:last").attr("data-id");
    count++;

    colour_count = count;
    colour_count = (colour_count - 1);
    var form_id = 1;

    var colours_list = ["red", "green", "orange", "blue", "yellow", "purple", "turquoise", "pink", "light-blue", "grey", "pale-purple", "bright-pink", "dark-grey", "bright-orange", "dark-blue", "true-purple", "jet-blue", "smashed-pumpkin", "madder-lake", "offset-purple", "fiery-rose", "eggshell", "sonic-silver", "sunset-blue", "rajah", "light-coral", "mustard", "metallic-seaweed", "sea-green", "japanese-violet"];
    tab_count = (count + 1);



    $(document).on('click', '.new-field-button', function (e) {
        e.preventDefault();
        var input_count = $(this).siblings("#input-count");
        var input_count_id = input_count.text();
        input_count_id++;
        if (input_count_id > 1) {
            $(".remove-field-button").show();
        }

        if (input_count_id > 10) {
            $(".new-field-button").hide();
            $(this).siblings(".max-option-notice").show();
        } else {
            counti = `form_${form_id}_input${input_count_id}`;
            var html = "<div class='input-group' data-id='" + counti + "'><label for='poll_option_" + counti + "'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_" + counti + "' id='poll_option_" + counti + "'  placeholder='Eg. Option " + input_count_id + "' tabindex='" + tab_count + "''/><div class='poll-option-group'><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='" + colours_list[colour_count] + "'><span></span></a></div></div></div><input type='text' value='" + colours_list[colour_count] + "' class='colour_input' name='colour_" + counti + "' id='colour_option_" + counti + "' readonly/></div>";


            $(this).parent('.input-group').siblings('.poll-options').children(".poll-options .input-group:last").after(html);

            $("#poll_option_" + counti).focus();
            //$("#scroll-point").scrollIntoView();
            colour_count = (colour_count + 1) % colours_list.length;
            tab_count = (tab_count + 1);

            input_count.text(input_count_id);
            if (input_count_id == 16) {
                $(this).hide();

                console.log($(this).siblings());
                $(this).siblings(".max-option-notice").show();
            }
        }
    });

    $(document).on('click', '.add-new-poll', function (e) {
        e.preventDefault();

        form_id++;
        var html = "<div class='input-group' data-id='" + count + "'><label for='poll_option_" + count + "'>Poll option</label><div class='input-group-field'><input type='text' name='poll_option_" + count + "' id='poll_option_" + count + "'  placeholder='Eg. Option " + count + "' tabindex='" + tab_count + "''/><div class='poll-option-group'><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='" + colours_list[colour_count] + "'><span></span></a></div></div></div><input type='text' value='" + colours_list[colour_count] + "' class='colour_input' name='colour_" + count + "' id='colour_option_" + count + "' readonly/></div>";
        var html = `<div class='new-form' id='form_${form_id}'><div class='input-group'><label for='form_${form_id}_poll-question'>POLL QUESTION ${form_id}</label><textarea placeholder='Eg. What is your favourite colour' id='form_${form_id}_poll_question' name='form_${form_id}_poll_question_1' tabindex='1' data-msg='You need to enter a poll question' autofocus required></textarea></div><div class='poll-options'><div class='input-group' data-id='1'><label for='form_${form_id}_poll_option_1'>Poll option</label><div class='input-group-field'><input type='text' name='form_${form_id}_poll_option_1' id='form_${form_id}_poll_option_1' placeholder='Eg. Option 1' tabindex='2' data-msg='You need to enter a minimum of 2 options' required/><div class='poll-option-group'><div class='poll-colour-dropdown-wrapper'><a href='#' id='colour-block-button' class='colour-option-button-one red' title='Choose a colour for your poll option'><span></span></a></div></div></div><input type='text' value='red' class='colour_input' name='form_${form_id}_colour_1' id='form_${form_id}_colour_option_1' readonly/></div></div><div class='input-group'><a href='#' class='new-field-button' title='Add another option to your poll'>Add another option</a><div id="input-count">1</div><a href='#' class='remove-field-button' title='Add another option to your poll'>Remove last option</a><p class='max-option-notice'>I believe 10 Options are already too much.</p></div><div class='form-divide'></div></div>`;

        $(".new-form:last").after(html);
        if (form_id == 5) {
            $(".add-new-poll").hide();
            alert('Enough Questions for one Poll')
        }

    });
    $(document).on('click', '.remove-last-poll', function (e) {
        e.preventDefault();
        $('.add-new-poll').show();
        if (confirm('Are you sure you want to delete the last poll?')) {
            console.log(form_id);
            if (form_id > 1) {
                $(".new-form:last").remove();
                form_id--;
            } else {
                alert('You cannot delete the only poll question')
            }
        }
    });
    $(document).on('click', '.remove-field-button', function (e) {
            e.preventDefault();
            var input_count = $(this).siblings("#input-count");
            var input_count_id = input_count.text();
            input_count_id--;

            if (input_count_id < 1) {
                $(this).hide();
            } else {
                $(this).siblings(".max-option-notice").hide();
                $(this).parent('.input-group').siblings('.poll-options').children(".poll-options .input-group:last").remove();
                input_count.text(input_count_id);
                if (input_count_id <= 10) {
                    $(".new-field-button").show();
                }
            }
        }
    );

    myAjax('.create-poll-button', '#poll-form', '/create_poll', '', 1);
    myAjax('.edit-poll-button', '#edit-poll-form', '/admin_edit_poll', '/polls');
    myAjax('#btnAdminLogin', "#login_form", '/admin_sign_in', '/admin/polls');

    // colour options click
    $(document).on('click', 'a#colour-block-button', function (e) {
        e.preventDefault();
        $(".input-group .poll-colour-dropdown").remove();
        $(".poll-colour-dropdown").clone().insertAfter(this).fadeIn(400);
    });

    $(document).on('click touchstart', 'a.colour-squares-more-button', function (e) {
        e.preventDefault();
        $(this).fadeOut(100);
        $(".poll-colour-dropdown-wrapper .poll-colour-dropdown .poll-colour-squares-hidden").delay(100).fadeIn(400);
    });

    $(document).on('click touchstart', 'a.colour-square', function (e) {
        e.preventDefault();
        var colour_variable = $(this).data('colour');
        $(this).closest('.poll-colour-dropdown-wrapper').children('#colour-block-button').removeClass().addClass(colour_variable);
        $(this).closest('.input-group').children('.colour_input').val(colour_variable);
        $(".poll-colour-dropdown").delay(100).fadeOut(100);
        setTimeout(function () {
            $(".input-group .poll-colour-dropdown").remove();
        }, 300);
    });

    $(document).on('click touchstart', function (e) {
        if ($(e.target).closest(".poll-colour-dropdown-wrapper").length === 0) {
            $(".poll-colour-dropdown").delay(100).fadeOut(100);

            setTimeout(function () {
                $(".input-group .poll-colour-dropdown").remove();
            }, 300);

        }
    });

    // security copy change based on session or cookies
    $('.radio-buttons.check #require_login').on('click', function () {
        if ($(this).is(':checked')) {
            $(".poll-secured").text("Poll secured using sessions to stop duplicate votes being cast.");
        } else {
            $(".poll-secured").text("Poll secured using cookies to prevent duplicate votes being cast.");
        }
    });

    // validate form
    $("#poll-form").validate();

    // textarea autogrow
    $('textarea').autogrow({onInitialize: true});

    // clear local localStorage
    if (localStorage.getItem("poll_question") != null) {
        var html = "<a href='https://pacesetterfrontier.com/new' class='delete-stored-data-link'>Remove saved poll data</a>";
        $(".poll-secured").after(html);
    }
    // captcha error
    $(".upload-image-button a").attr("href", "https://pacesetterfrontier.com");
});


$(".item-link-share-inline").click(function (e) {
    e.preventDefault();
    $(".item-dropdown.animated-dropdown.bounceIn.social-share-links.inline").toggle();
});

function myAjax(element, sentform, url, loc = '', refresh = 0, mod = false) {
    $(element).click(function (e) {
        e.preventDefault();
        frm = $(sentform);
        $.ajax({
            url: url,
            method: 'POST',
            data: frm.serialize(),
            success: function (data) {
                if (data == 'ok') {
                    bootbox.alert("<p class='text-success'>Successful</p>");
                    if (loc !== '') {
                        setTimeout(() => {
                            location.assign(loc)
                        }, 2000)
                    }
                    if (refresh === 1) {
                        setTimeout(() => {
                            window.top.location = window.top.location;
                        }, 2000)
                    }
                } else {
                    bootbox.alert("<p class='text-danger'>" + data + "</p>");
                }
            }
        })
    })
}
function justAjax(element, sentform, url, loc='', refresh=0) {
    btn = $(element);
    frm = $(sentform);
    btnText = btn.html();
    btn.html('Processing... <i class="bi bi-square spins"></i>');
    $.ajax({
        url: url,
        method: 'POST',
        data: frm.serialize(),
        success: function (data) {
            btn.html(btnText);
            if (data === 'ok') {
                bootbox.alert("<p class='text-success'>Successful</p>");
                if (loc !== '') {
                    setTimeout(() => {
                        location.assign(loc)
                    }, 2000);
                }
                if (refresh === 1) {
                    setTimeout(() => {
                        window.top.location = window.top.location;
                    }, 2000)
                }
                debugger;
                console.log('reached');
                justAjaxReturn = 1;
            } else {
                bootbox.alert("<p class='text-danger'>" + data + "</p>");
            }
        }
    })
}

// Todo: Don't forget to add go to result page after voting

var section, kids;
$('#btn-vote').click(function (e) {
    e.preventDefault();
    section = $(this).parent().siblings(".poll-section");
    kids = section.children(".poll-item").children("input");
    var allClear = true;

    for (let i = 0; i < section.length; i++) {
        let currentSec = 0;
        for (elem in section[i].children) {
            if (section[i].children[elem].className === 'poll-item' && section[i].children[elem].children[0].checked) {
                currentSec = 1;
            }
        }
        if (currentSec === 0) {
            section[i].children[1].style.display = 'block';
        } else {
            section[i].children[1].style.display = 'none';
        }

        if (section[i].children[1].style.display === 'block') {
            allClear = false;
        }
    }
    if (allClear) {
        justAjax('#btn-vote', '#vote-poll-form', '/cast_votes');
    } else {
        bootbox.alert("<p class='text-danger'>All votes are necessary!</p>");
    }
});

$(document).on('click', '#adminSettings', function (e) {
    e.preventDefault();
    $(this).siblings($(".item-dropdown.animated-dropdown.bounceIn")).slideToggle();
});

$(document).on('click', '#btnDeletePoll', function (e) {
    e.preventDefault();
    let data_id = $(this).attr('data-id');
    let data_title = $(this).attr('data-title');
    bootbox.confirm("Are you sure you want to delete this poll ("+data_title+")?", function (result) {
        if (result){
            $.ajax({
                url: '/admin_delete_poll',
                method: 'POST',
                data: {data_id: data_id},
                success: function (data) {
                    if (data === 'ok'){
                        bootbox.alert(data_title + " poll has been deleted successfully!");
                        setTimeout(()=>{
                            window.top.location = window.top.location;
                        }, 2000)
                    } else{
                        bootbox.alert("<p class='text-danger'>"+data+"</p>");
                    }
                }
            })
        }
    })
});