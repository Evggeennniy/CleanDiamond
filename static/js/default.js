const navbarModal = document.querySelector(".header__mini_wrapper");
const navbarBurgerBtn = document.querySelector(".navbar__burger_btn");

navbarBurgerBtn.addEventListener("click", () => {
  const isHidden = getComputedStyle(navbarModal).display === "none";

  if (isHidden) {
    navbarModal.classList.add("open");
    document.body.classList.add("overflow_hidden");
  } else {
    navbarModal.classList.remove("open");
    document.body.classList.remove("overflow_hidden");
  }
});

window.addEventListener("resize", () => {
  if (window.innerWidth > 768 && navbarModal.classList.contains("open")) {
    navbarModal.classList.remove("open");
  }
});

const modal = document.querySelector(".contact__modal_wrapper");
const sendButton = document.querySelector(".form__bottom_btns_send");

sendButton.addEventListener("click", (event) => {
  event.preventDefault();

  sendButton.disabled = true;

  modal.classList.add("visible");

  setTimeout(() => {
    modal.classList.remove("visible");
    sendButton.disabled = false;
    sendButton.closest("form").submit();
  }, 3000);
});
