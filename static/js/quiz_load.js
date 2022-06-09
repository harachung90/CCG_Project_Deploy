// const startQuiz = document.getElementsByClassName('start-quiz')
// const descBox = document.getElementById('quiz_desc_box')
// const idButton = document.getElementsByClassName('quiz_desc_button')
const url = window.location.href

// const desc1 = document.getElementById('desc1')
// const desc2 = document.getElementById('desc2')
// const desc3 = document.getElementById('desc3')
$(document).ready(function () {
        $('.quiz_desc_button').click(function (event) {
            // var button_id = $(this).data("id")

            var clickedIndex = $(this).index();
            console.log("clicked Index: " + clickedIndex);

            $('.quiz_desc_box').hide();
            $('.quiz_desc_box').eq(clickedIndex).show();

            var id = $('.quiz_desc_box').eq(clickedIndex).data("id");
            console.log("quiz id: " + id);

            for (var i = 0; i < $('.quiz_desc_box').length; i++) {
                $('.start-quiz').eq(1).on("click", function () {
                    console.log("Clicked!");
                    window.location.href = url + id;
                }
            }
            $('.start-quiz').eq(1).on("click", function () {
                alert("Hello!");
            })

            $('.start_quiz').eq(clickedIndex).click(() => {
                console.log("Clicked!");
                window.location.href = url + id;
            })
        })
    }
);


/*
function open1() {
    descBox.style.display = 'block';
    desc1.style.display = 'block';
    desc2.style.display = 'none';
    desc3.style.display = 'none';
    startQuiz.style.display = 'block';
    const id = idButton[0].getAttribute('data-id')

    startQuiz.addEventListener('click', () => {
        window.location.href = url + id;
    })
}

function open2() {
    descBox.style.display = 'block';
    desc1.style.display = 'none';
    desc2.style.display = 'block';
    desc3.style.display = 'none';
    startQuiz.style.display = 'block';
    const id = idButton[1].getAttribute('data-id')

    startQuiz.addEventListener('click', () => {
        window.location.href = url + id;
    })
}

function open3(){
    descBox.style.display = 'block';
    desc1.style.display = 'none';
    desc2.style.display = 'none';
    desc3.style.display = 'block';
    startQuiz.style.display = 'block';
    const id = idButton[2].getAttribute('data-id')

    startQuiz.addEventListener('click', () => {
        window.location.href = url + id;
    })
}

idButton[0].addEventListener('click', open1);
idButton[1].addEventListener('click', open2);
idButton[2].addEventListener('click', open3);
*/


