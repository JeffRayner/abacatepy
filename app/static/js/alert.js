setTimeout(function() {
    var container = document.getElementById('alertas');
    container.classList.add('fade');
    setTimeout(()=>{container.remove()}, 500);
}, 5000);

document.addEventListener('DOMContentLoaded', function () {
    const cardsAlert = document.querySelectorAll('.alerta');
    cardsAlert.forEach(function(card) {
        card.addEventListener('click', function() {
            card.classList.add('fade');
            setTimeout(()=>{card.remove()}, 500);
        });
    });
});