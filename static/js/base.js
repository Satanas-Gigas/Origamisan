document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-visibility-btn");
    const toggleElements = document.querySelectorAll(".toggle-visibility");
    // Проверяем состояние из localStorage
    const isHidden = localStorage.getItem("toggleVisibility") === "true";
    if (isHidden) {
        toggleElements.forEach(element => {
            element.classList.add("hidden");
        });
    }
    // Обработчик клика по кнопке
    toggleButton.addEventListener("click", function () {
        const currentState = localStorage.getItem("toggleVisibility") === "true";
        const newState = !currentState;                
        // Сохраняем новое состояние в localStorage
        localStorage.setItem("toggleVisibility", newState);
        toggleElements.forEach(element => {
            element.classList.toggle("hidden", newState);
         });
      });
  });