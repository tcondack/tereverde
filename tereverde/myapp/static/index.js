document.querySelectorAll('nav a[href^="#"]').forEach(link => {
  link.addEventListener('click', e => {
    const destino = document.querySelector(link.getAttribute('href'));
    if (destino) {
      e.preventDefault();
      destino.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Saudação com base no horário
const hora = new Date().getHours();
let saudacao = "Bem-vindo";

if (hora < 12) saudacao = "Bom dia";
else if (hora < 18) saudacao = "Boa tarde";
else saudacao = "Boa noite";

const tituloSaudacao = document.querySelector('.welcome h2');
if (tituloSaudacao) tituloSaudacao.textContent = "${saudacao} ao ecoturismo de Teresópolis"