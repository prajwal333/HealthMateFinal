const openModalBtn = document.getElementById('openModalBtn');
const closeModalBtn = document.getElementById('closeModalBtn');
const modalOverlay = document.querySelector('.modal-overlay');
const modalContent = document.querySelector('.modal-content');

openModalBtn.addEventListener('click', () => {
  modalOverlay.classList.add('open');
  modalContent.classList.add('open');
});

closeModalBtn.addEventListener('click', () => {
  modalOverlay.classList.remove('open');
  modalContent.classList.remove('open');
});


