  // Какие типы теста должны показывать extra-options:
  // Если нужно только для "hide", оставь ['hide'].
  // Если нужно и для "kanji_sent", укажи ['hide','kanji_sent'].
  const SHOW_EXTRA_FOR = new Set(['hide','kanji_sent']); 

  const extraOptions = document.getElementById('extra-options');
  const radios = document.querySelectorAll('input[name="test_type"]');

  function updateExtraOptions() {
    const selected = document.querySelector('input[name="test_type"]:checked');
    const shouldShow = selected && SHOW_EXTRA_FOR.has(selected.value);
    // Используем hidden, чтобы не смешивать inline-стили и классы
    extraOptions.hidden = !shouldShow;
  }

  // Навесить обработчики
  radios.forEach(r => r.addEventListener('change', updateExtraOptions));

  // Инициализация (на случай, если по умолчанию выбран тип без подсказок)
  updateExtraOptions();
