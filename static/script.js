document.addEventListener("DOMContentLoaded", () => {

  // -----------------------------
  // Bottom nav + footer observer
  // -----------------------------
  const nav = document.querySelector(".bottom-nav");
  const footer = document.querySelector("#page-footer");

  if (nav && footer) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          nav.style.opacity = "0";
          nav.style.transform = "translateX(-50%) translateY(20px)";
          nav.style.pointerEvents = "none";
        } else {
          nav.style.opacity = "1";
          nav.style.transform = "translateX(-50%) translateY(0)";
          nav.style.pointerEvents = "auto";
        }
      });
    }, { threshold: 0.1 });

    observer.observe(footer);
  }

  // -----------------------------
  // Transaction type toggle logic
  // -----------------------------
  const typeSelect = document.getElementById("tx-type");
  const categoryWrapper = document.getElementById("category-wrapper");

  if (typeSelect && categoryWrapper) {

    function toggleCategory() {
      const isExpense = typeSelect.value === "expense";

      categoryWrapper.classList.toggle("d-none", !isExpense);

      const select = categoryWrapper.querySelector("select");
      if (select) select.disabled = !isExpense;
    }

    typeSelect.addEventListener("change", toggleCategory);

    toggleCategory();
  }

});