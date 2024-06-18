document.addEventListener("scroll", () => {
  const nav = document.querySelector(".normal");
  const sign = document.querySelector(".login-register");
  if (window.scrollY > 50) {
    console.log(window.scrollY);
    nav.style.background = "Black";
    sign.style.display = "none";
  } else {
    nav.style.background = "rgba(0, 0, 0, 0.6)";
    sign.style.display = "flex";
  }
});

