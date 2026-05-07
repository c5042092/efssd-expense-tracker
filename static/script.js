
document.addEventListener("DOMContentLoaded", () => {
    const nav = document.querySelector(".bottom-nav");
    const footer = document.querySelector("#page-footer");

    if (!nav || !footer) return;

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
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
        },
        {
            root: null,
            threshold: 0.1
        }
    );

    observer.observe(footer);
});