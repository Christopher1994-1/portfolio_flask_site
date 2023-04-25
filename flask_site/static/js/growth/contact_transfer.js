const form = document.getElementById('message-form')

form.addEventListener("submit", async (event) => {
    event.preventDefault(); // prevent the form from submitting normally

    let name = document.getElementById('name').value
    let message = document.getElementById('message').value
    let email = document.getElementById('email').value
    let subject = document.getElementById('subject').value

    let contact_container = document.getElementById('message-form-container')
    let thank_you_container = document.getElementById('thank-you-form')

    contact_container.style.display = 'none'

    thank_you_container.style.display = 'block'
    thank_you_container.style.display = 'flex'
    thank_you_container.style.flexDirection = 'column'

  });
