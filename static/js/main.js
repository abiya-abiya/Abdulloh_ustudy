// Mobil menyu: burger tugmasi navigatsiyani ochadi/yopadi
const burger = document.querySelector('.burger');
const nav = document.getElementById('site-nav');
burger?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  burger.setAttribute('aria-expanded', open);
});
