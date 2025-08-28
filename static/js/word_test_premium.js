const typeHide = document.getElementById('type_hide');
const typeSent = document.getElementById('type_kanji_sent');
const extraOptions = document.getElementById('extra-options');
const typeRadioButtons = document.querySelectorAll('input[name="test_type"]');

// Функция для обновления состояния
function updateExtraOptions() {
    if ((typeHide && typeHide.checked) || (typeSent && typeSent.checked)) {
        extraOptions.style.display = 'block';
    } else {
        extraOptions.style.display = 'none';
    }
}

// Навешиваем обработчики
typeRadioButtons.forEach(radio => {
    radio.addEventListener('change', updateExtraOptions);
});

// Вызываем один раз при загрузке страницы
updateExtraOptions();
в