const startQuiz = document.getElementById('start-quiz')
const descBox = document.getElementById('quiz_desc_box')
const idButton = document.getElementsByClassName('quiz_desc_button')
const url = window.location.href

const desc1 = document.getElementById('desc1')
const desc2 = document.getElementById('desc2')
const desc3 = document.getElementById('desc3')

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


