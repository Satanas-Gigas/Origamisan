document.addEventListener('DOMContentLoaded', () => {
  const typeHide = document.getElementById('type_hide');
  const typeSent = document.getElementById('type_kanji_sent');
  const extraOptions = document.getElementById('extra-options');
  const typeRadioButtons = document.querySelectorAll('input[name="test_type"]');

  if (!extraOptions) return;

  // Показываем встроенное состояние (0 — скрыто; 1 — показать сразу)
  const initialVisible = extraOptions.getAttribute('data-initial-visible') === '1';
  extraOptions.style.display = initialVisible ? 'block' : 'none';

  function updateExtraOptions() {
    const needExtra =
      (typeHide && typeHide.checked) ||
      (typeSent && typeSent.checked);

    extraOptions.style.display = needExtra ? 'block' : 'none';

    // Дополнительно: если панель скрыта — снимем выбор, чтобы не улетали лишние данные на сервер
    if (!needExtra) {
      const r1 = document.getElementById('option_with_hints');
      const r2 = document.getElementById('option_without_hints');
      if (r1) r1.checked = false;
      if (r2) r2.checked = false;
    } else {
      // если нужно — проставим дефолт «с подсказками»
      const r1 = document.getElementById('option_with_hints');
      if (r1 && !document.querySelector('input[name="extra_option"]:checked')) {
        r1.checked = true;
      }
    }
  }

  // ВАЖНО: не вызываем updateExtraOptions() на старте — чтобы не открывать панель из-за дефолтного checked
  // Покажем панель только после реального выбора пользователем:
  typeRadioButtons.forEach(radio => {
    radio.addEventListener('change', updateExtraOptions, { passive: true });
  });
});