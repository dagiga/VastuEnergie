/* ================================================
   form.js — Validation formulaire contact
   ================================================ */
(function () {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    let valid = true;

    /* Vérification RGPD obligatoire */
    const rgpd = form.querySelector('#rgpd');
    const rgpdError = form.querySelector('#rgpd-error');
    if (rgpd && !rgpd.checked) {
      e.preventDefault();
      valid = false;
      if (rgpdError) rgpdError.classList.add('is-visible');
    } else if (rgpdError) {
      rgpdError.classList.remove('is-visible');
    }

    /* Vérification email basique */
    const email = form.querySelector('#email');
    const emailError = form.querySelector('#email-error');
    if (email && email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
      e.preventDefault();
      valid = false;
      if (emailError) emailError.classList.add('is-visible');
    } else if (emailError) {
      emailError.classList.remove('is-visible');
    }

    /* Message de confirmation Formspree (si renvoyé) */
    if (valid) {
      /* Formspree redirige vers la page d'origine avec ?submitted=true */
      /* Ou affiche le message via AJAX si configuré */
    }
  });

  /* Effacer les erreurs à la saisie */
  form.querySelectorAll('.form-control').forEach(function (field) {
    field.addEventListener('input', function () {
      const errorId = this.id + '-error';
      const err = document.getElementById(errorId);
      if (err) err.classList.remove('is-visible');
    });
  });

  /* Confirmation si retour Formspree (?submitted=true dans l'URL) */
  if (window.location.search.includes('submitted=true')) {
    const success = document.getElementById('form-success');
    if (success) {
      success.style.display = 'block';
      form.style.display = 'none';
    }
  }
})();
