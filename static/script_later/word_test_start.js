// ===============================
// word_test_start.js (идеальный)
// ===============================
// Работает только с data-атрибутами .container.py-5
// НЕ ДОЛЖНО быть других объявлений переменных questionTime/answersTime!
// ===============================

document.addEventListener("DOMContentLoaded", function () {
    // ================================
    // Получаем значения времени из data-атрибутов HTML
    // ================================
    const container = document.querySelector(".container.py-5");
    const questionTime = Number(container.getAttribute("data-question-time")) || 0;
    const answersTime = Number(container.getAttribute("data-answers-time")) || 40;
    console.log('JS: questionTime =', questionTime, 'answersTime =', answersTime);

    // ================================
    // DOM элементы
    // ================================
    const buttons = document.querySelectorAll(".answer-btn");
    const form = document.getElementById("quiz-form");
    const resultMessage = document.getElementById("result-message");
    const clockDiv = document.getElementById("clockdiv");
    const question_wordDiv = document.querySelector("[data-id='question_word-div']");
    const optionsDiv = document.querySelector("[data-id='options-div']");
    const clockDiv_hide = document.getElementById("clockdiv_hide");
    const progressBar = document.querySelector(".progress-bar");
    const progressBar_down = document.getElementById("progress-bar_down");
    const progress = document.querySelector(".progress");
    let timeInterval_hide;
    let timeInterval;
    const left_time = document.getElementById("left_time");

    // ================================
    // Запуск таймеров по условиям
    // ================================
    if (questionTime > 0) {
        // Сначала показываем вопрос N секунд, затем варианты
        const deadline_hide = new Date(Date.now() + questionTime * 1000);
        initializeClock_hide('clockdiv_hide', deadline_hide, questionTime);
    } else {
        // Показываем сразу и вопрос, и варианты
        question_wordDiv.style.display = "";
        optionsDiv.style.display = "";
        clockDiv_hide.style.display = "none";
        const deadline = new Date(Date.now() + answersTime * 1000);
        initializeClock('clockdiv', deadline, answersTime);
    }

    // ================================
    // Логика ответов
    // ================================
    buttons.forEach((button) => {
        button.addEventListener("mouseover", () => button.style.backgroundColor = "#e0e0e0");
        button.addEventListener("mouseout", () => button.style.backgroundColor = "#f5f5f5");
        button.addEventListener("click", () => {
            buttons.forEach((btn) => btn.disabled = true);
            const isCorrect = button.getAttribute("data-correct") === "true";

            if (isCorrect) {
                button.classList.add("btn-success");
                resultMessage.style.color = "green";
                resultMessage.innerText = "Правильно!";
                button.style.boxShadow = "0 0 20px 5px green";
            } else {
                button.classList.add("btn-danger");
                resultMessage.style.color = "red";
                resultMessage.innerText = "Неправильно!";
                button.style.boxShadow = "0 0 20px 5px red";
                buttons.forEach((btn) => {
                    if (btn.getAttribute("data-correct") === "true") {
                        btn.classList.add("btn-success");
                        btn.style.boxShadow = "0 0 20px 5px green";
                    }
                });
            }

            resultMessage.style.display = "block";
            clockDiv.style.display = "none";
            clearInterval(timeInterval);
            const hiddenInput = document.createElement("input");
            hiddenInput.type = "hidden";
            hiddenInput.name = "user_answer";
            hiddenInput.value = button.value;
            form.appendChild(hiddenInput);

            setTimeout(() => form.submit(), 1000);
        });
    });

    // ================================
    // Функции таймеров
    // ================================
    function getTimeRemaining(endtime, totalSeconds) {
        const t = Date.parse(endtime) - Date.now();
        const seconds = Math.ceil(t / 1000); // округление вверх, чтобы 1.3с -> 2с
        const percentage = (t / (totalSeconds * 1000)) * 100;
        progressBar_down.style.width = `${Math.max(0, percentage)}%`;
        return { total: t, seconds: Math.max(0, seconds) };
    }

    function initializeClock(id, endtime, totalSeconds) {
        const clock = document.getElementById(id);
        function updateClock() {
            const t = getTimeRemaining(endtime, totalSeconds);
            clock.innerHTML = `${t.seconds} сек.`;
            if (t.total < 0) {
                clearInterval(timeInterval);
                clock.style.display = "none";
                resultMessage.style.color = "red";
                resultMessage.innerText = "Время истекло! Неправильно!";
                resultMessage.style.display = "block";
                clockDiv.style.display = "none";
                const incorrectAnswerButton = document.querySelector('.answer-btn[data-correct="false"]');
                const hiddenInput = document.createElement("input");
                hiddenInput.type = "hidden";
                hiddenInput.name = "user_answer";
                hiddenInput.value = incorrectAnswerButton ? incorrectAnswerButton.value : '';
                form.appendChild(hiddenInput);
                setTimeout(() => form.submit(), 1000);
            }
        }
        updateClock();
        timeInterval = setInterval(updateClock, 1000);
    }

    function getTimeRemaining_hide(endtime, totalSeconds) {
        const t = Date.parse(endtime) - Date.now();
        const seconds = Math.ceil(t / 1000);
        const percentage = (t / (totalSeconds * 1000)) * 100;
        progressBar.style.width = `${Math.max(0, percentage)}%`;
        return { total: t, seconds: Math.max(0, seconds) };
    }

    function initializeClock_hide(id, endtime, totalSeconds) {
        const clock = document.getElementById(id);
        optionsDiv.style.display = "none";
        function updateClock_hide() {
            const t = getTimeRemaining_hide(endtime, totalSeconds);
            clock.innerHTML = `${t.seconds} сек.`;
            if (t.total < 0) {
                left_time.style.visibility = "hidden";
                clearInterval(timeInterval_hide);
                clock.style.display = "none";
                question_wordDiv.style.display = "none";
                optionsDiv.style.display = "";
                progressBar.style.width = "0%";
                progress.style.display = "";
                const deadline = new Date(Date.now() + answersTime * 1000);
                initializeClock('clockdiv', deadline, answersTime);
            }
        }
        updateClock_hide();
        timeInterval_hide = setInterval(updateClock_hide, 1000);
    }

});
