const url = window.location.href

const quizBox = document.getElementById('quiz_box');
const resultBox = document.getElementById('result_box');
const totalScore = document.getElementById('total');
const message = document.getElementById('message');

$.ajax({
    type: 'GET',
    url: `${url}data/`,
    success: function (response) {
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
                                    <h4 class="num_right">You got ${response.score_num} out of ${response.total} questions right!</h4>
                                    <h4 class="your_level">You are ${response.user_level}</h4>`

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
            })
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
                console.log('End off.')
            }
        };
        requestAnimationFrame(scrollTo);
    }
};


quizForm.addEventListener('submit', e => {
    e.preventDefault()
    let radios = $('input[type=radio]:checked');
    let total = $('input[type=radio]');
    // divided by 3 because there are 3 answers to choose from - should chane if the default number of answer choices are changed.
    if (radios.length < total.length / 3) {
        alert("Not all the questions are answered.");
        return false;
    } else {
        sendData()
        open()
        animteScrollTo('#total')
    }
});

function open() {
    const hiddenBox = document.getElementById('hidden_box');
    const startLearning = document.getElementById('start_learning');
    const vheight = $('.test').height();
    hiddenBox.style.paddingBottom = vheight - 70 + "px";
    hiddenBox.style.display = 'block';
    startLearning.style.display = 'block';
}

