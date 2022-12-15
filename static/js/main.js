let form = document.querySelector("#formdata")
let nameInput = document.querySelector(".name-input")
let subjectInput = document.querySelector(".subject-input")
let emailInput = document.querySelector(".email-input")
let phoneInput = document.querySelector(".phone-input")
let messageInput = document.querySelector(".message-input")

form.addEventListener("submit", (e) => {
  e.preventDefault();
  if (subjectInput.value == "") {
    let named = nameInput.value ? nameInput.value : "Sir/Ma" 
    Swal.fire(
      'Info',
      `Please ${named}, Subject is mandatory`,
      'warning'
    )
    named = ""
    return false;
  }
  if (emailInput.value == "" && phoneInput == "") {
    let named = nameInput.value ? nameInput.value : "Sir/Ma" 
    Swal.fire(
      'Info',
      `Please ${named}, Must provide either Email or Phone No`,
      'warning'
    )
    named = ""
    return false;
  }
  if (messageInput.value == "") {
    let named = nameInput.value ? nameInput.value : "Sir/Ma" 
    Swal.fire(
      'Info',
      `Please ${named}, Message cant be empty`,
      'warning'
    )
    named = ""
    return false;
  }
  form.submit();
  Swal.fire(
      'Success',
      "submitted successfully!!",
      'success'
    )
})