$(function() {

    const startQuiz = document.getElementById('start-quiz')
    const idButton = document.getElementsByClassName('quiz_desc_button')
    const url = window.location.href
    const id = idButton.getAttribute('data-id')

    startQuiz.addEventListener('click', () => {
        window.location.href = url + id;
    })

    $('.quiz_desc_button').click(function() {
        var $quiz = $(this).siblings().find('.quiz_desc_box');
        if ($quiz.hasClass('quiz_desc_box_active')) {
            $quiz.removeClass('quiz_desc_box_active');
            $quiz.fadeOut();

        } else {
            $quiz.addClass('quiz_desc_box_active');
            $quiz.fadeIn();
        }
    })}
);