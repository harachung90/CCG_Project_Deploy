$(function() {

    $('.quiz_desc_button').click(function() {
        var $quiz = $(this).siblings().find('.quiz_desc_box');
        if ($quiz.hasClass('quiz_desc_box_active')) {
            $quiz.removeClass('quiz_desc_box_active');
            $('.demo-container').not('div.quiz_desc_box_active').css('display', 'none');
            $quiz.fadeOut();
        } else {
            $quiz.addClass('quiz_desc_box_active');
            $('.demo-container').not('div.quiz_desc_box_active').css('display', 'none');
            $quiz.fadeIn();
        }
    })}
);