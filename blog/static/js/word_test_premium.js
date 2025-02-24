const typeHide = document.getElementById('type_hide');
const extraOptions = document.getElementById('extra-options');
const typeRadioButtons = document.querySelectorAll('input[name="test_type"]');

// Добавляем обработчик события
typeRadioButtons.forEach(radio => {
    radio.addEventListener('change', function () {
        if (typeHide.checked) {
            extraOptions.style.display = 'block';
        } else {
            extraOptions.style.display = 'none';
        }
    });
});