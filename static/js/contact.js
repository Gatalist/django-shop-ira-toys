// форма
let email = document.querySelector("#id_email")
let button = document.querySelector("#mc-submit")
button.setAttribute("disabled", "disabled");
//-----------------////-----------------//
// форма валидная
let vilide = (element) => {
	element.classList.add('is-valid');
	element.classList.remove('is-invalid');
}
// форма невалидная
let invalide = (element) => {
	element.classList.remove('is-valid');
	element.classList.add('is-invalid');
}
// проверка email
function validateEmail(inputs) {
	var re = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
	let email = re.test(String(inputs).toLowerCase());
	return email
}
email.addEventListener("input", function() {
	let inputs = this.value
	this.value = inputs
	let valid = validateEmail(inputs)
	if (valid == true) {
		vilide(this);
		button.removeAttribute("disabled", "disabled");
	} 
	else {
		invalide(this);
		button.setAttribute("disabled", "disabled");
	}
});