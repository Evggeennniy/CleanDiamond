const navbarModal = document.querySelector(".header__mini_wrapper");
const navbarBurgerBtn = document.querySelector(".navbar__burger_btn");

navbarBurgerBtn.addEventListener("click", () => {
  const isHidden = getComputedStyle(navbarModal).display === "none";

  if (isHidden) {
    navbarModal.classList.add("open");
  } else {
    navbarModal.classList.remove("open");
  }
});

window.addEventListener("resize", () => {
  if (window.innerWidth > 768 && navbarModal.classList.contains("open")) {
    navbarModal.classList.remove("open");
  }
});
