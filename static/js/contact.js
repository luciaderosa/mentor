/**
 * contact forma validation
 */
// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()

/*
console.log("Entro a validar");
displayError("Prueba de mensaje de error");

document.getElementById("contact-button").addEventListener("click", validateForm); 

function validateForm(event) {
  console.log("Entro a la función validateForm");
  event.preventDefault();
  const name = document.getElementById("id_name");
  const email = document.getElementById("id_email");
  const subject = document.getElementById("id_subject");
  const message = document.getElementById("id_message");

  console.log(name.value);
  console.log(email.value);
  console.log(subject.value);
  console.log(message.value);

  if (name.value.length < 2) {
    displayError("Verify your name (min. 2 characters)");
    name.focus();
    return;
  }
  if (email.value.length < 2) {
    displayError("Verify your email");
    email.focus();
    return;
  }
  if (subject.value.length == 0) {
    displayError("We need a subject");
    subject.focus();
    return;
  }
  if (message.value.length == 0) {
    displayError("We are expecting a message from you");
    message.focus();
    return;
  }
  this.submit();
}

function displayError(error) {
  console.log("Entro a mostrar el error");
  errMsg = document.getElementById("err-msg");
  errMsg.innerHTML = error;
  //errMsg.classList.
  errMsg.classList.add("d-block");
}
console.log("salgo de validar");
*/