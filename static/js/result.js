const url = window.location.href

const quizBox = document.getElementById('quiz_box');
const resultBox = document.getElementById('result_box');
const totalScore = document.getElementById('total');
const message = document.getElementById('message');
const ticketList = ['6099', '9238', '6772', '1323', '2705', '9985', '9179', '6029', '3983'];

const toPS = url.replace('quiz_list/1', 'quiz_list/2');
const toCongrats = url.replace('quiz_list/2/', 'congratulations');

$.ajax({
    type: 'GET',
    url: `${url}data/`,
    success: function (response) {
        if (window.location.href.indexOf("/quiz_list/2") != -1) {
            var codeInput = prompt("Enter a code that you were offered when you passed the Level Assessment Quiz:");

            String.prototype.includes = function (str) { // PS Quiz
                return this.indexOf(str) !== -1;
            }

            if (ticketList.includes(codeInput)) {
                alert("Good luck with your quiz!");
            } else if (codeInput === null) {
                return false;
            } else {
                alert("Oh no, that's not the correct code. Try again, please.")
                return false;
                //history.back(); // go back to previous page
            }
        }

        const data = response.data
        data.forEach(ele => {
            for (const [question, answers] of Object.entries(ele)) {
                quizBox.innerHTML += `
                <div class="mb-2 q_text">
                    <b>${question}</b>
                </div>
                `
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                        <div>
                            
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label style="cursor: pointer;" for="${question}-${answer}" class="answer">${answer}</label>
                        </div>
                    `
                });
            }
        });
    },
    error: function (error) {
        console.log(error)
    }
});

const quizForm = document.getElementById('quiz_form');
const csrf = document.getElementsByName('csrfmiddlewaretoken');

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    });

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function (response) {
            const marks = response.marks
            totalScore.innerHTML = `<h3>${response.name}, here are your results:</h3>
                                    <h2 class="num_right">You got ${response.score_num} out of ${response.total} questions right!</h2>`

            if (window.location.href.indexOf("/quiz_list/1") != -1) {
                totalScore.innerHTML += `<h4 class="your_level">You are ${response.user_level}</h4>`
            } else {

            }

            const user_level = response.user_level;

            marks.forEach(res => {
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)) {

                    resDiv.innerHTML += question
                    const cls = ['container', 'h5']
                    resDiv.classList.add(...cls)

                    if (resp == 'not answered') {
                        resDiv.innerHTML += ' - Not Answered'
                        resDiv.classList.add('bg-info')
                    } else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']

                        if (answer == correct) {
                            resDiv.classList.add('d-lg-none')
                        } else {
                            resDiv.classList.add('wrong-q')
                            resDiv.innerHTML += `<br> | You answered: ${answer}`
                        }
                    }
                    $('#submitBtn').attr("disabled", true);
                }
                resultBox.append(resDiv)

                let cnt = document.getElementsByClassName('wrong-q').length;
                if (cnt == 0) {
                    message.innerHTML = `<h3>You got it all right!</h3>`
                } else if (cnt == 1) {
                    message.innerHTML = `<h3>You got this question wrong:</h3>`
                } else {
                    message.innerHTML = `<h3>You got these questions wrong:</h3>`
                }
            }) // here!


            if (window.location.href.indexOf("/quiz_list/1") != -1) { // Level Assessment Quiz
                if (user_level === "Advanced") {

                    let randomNum = Math.floor(Math.random() * 9);
                    let ticketNum = ticketList[randomNum];
                    const ticketDiv = document.getElementById('ticket');
                    ticketDiv.innerHTML += `<h2>You passed! Use this code to unlock the Port Scanner Quiz!</br><span style="background-color: #ffd500">${ticketNum}</span></h2>`
                    const learningDiv = document.getElementById('start_learning');
                    //learningDiv.style.display = 'none';
                    // add a link to PS Quiz
                    learningDiv.innerText = `Click on the button below to go to Port Scanner Quiz right away!`
                    const learningBtn = document.getElementsByClassName('learning_btn');

                    learningDiv.innerHTML += `</br><button onclick="directPS()">Port Scanner Quiz</button></a>`
                } else {

                } // nothing happens

            } else if (window.location.href.indexOf("/quiz_list/2") != -1) { // Port Scanner Quiz
                const passed = response.passed;
                if (passed === true) { // if passed the PS Quiz, redirect to Congratulations page
                    window.location = toCongrats;
                } else {
                    // nothing happens
                }
            } else {
                // nothing happens
            }
        },
        error: function (error) {
            console.log(error)
        }
    })
}

/**
 * Animate scrolling to a target position
 * @param {string} _selector Target selector
 * @param {number} _duration (Option) Duration time(ms) (Default. 800ms)
 * @param {number} _adjust (Option) Adjustment value of position
 */
animteScrollTo = function (_selector, _duration, _adjust) {
    const targetEle = document.querySelector(_selector);
    if (!targetEle) return;

    // - Get current &amp; target positions
    const scrollEle = document.documentElement || window.scrollingElement,
        currentY = scrollEle.scrollTop,
        targetY = targetEle.offsetTop - (_adjust || 0);
    animateScrollTo(currentY, targetY, _duration);

    // - Animate and scroll to target position
    function animateScrollTo(_startY, _endY, _duration) {
        _duration = _duration ? _duration : 600;
        const unitY = (targetY - currentY) / _duration;
        const startTime = new Date().getTime();
        const endTime = new Date().getTime() + _duration;

        const scrollTo = function () {
            let now = new Date().getTime();
            let passed = now - startTime;
            if (now <= endTime) {
                scrollEle.scrollTop = currentY + (unitY * passed);
                requestAnimationFrame(scrollTo);
            } else {
                //console.log('End off.')
            }
        };
        requestAnimationFrame(scrollTo);
    }
};


quizForm.addEventListener('submit', e => {
    e.preventDefault()
    let radios = $('input[type=radio]:checked');
    let total = $('input[type=radio]');
    // divided by 3 because there are 3 answers to choose from - should change if the default number of answer choices are changed.
    if (radios.length < total.length / 4) {
        alert("Not all the questions are answered.");
        return false;
    } else {
        sendData()
        open()
        animteScrollTo('#total')
    }
});

function open() {
    const vheight = $('.test').height();
    const hiddenBox = document.getElementById('hidden_box');

    //hiddenBox.style.paddingBottom = vheight - 70 + "px";

    $('#hidden_box').css('display', 'block');
    $('#start_learning').css('display', 'block');
}

function directPS() {
    window.location = toPS;
}

