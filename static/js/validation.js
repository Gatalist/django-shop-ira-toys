// форма
let form = document.querySelector('.checkbox-form')
let button = form.querySelector('button');
// inputs
let firstname = form.querySelector("#firstname")
let lastname = form.querySelector("#lastname")
let city = form.querySelector("#city")
let email = form.querySelector("#email")
let phone = form.querySelector("#phone")
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
// делаем кнопку активной
let data = {firstname: false, lastname: false, city: false, phone: false, email: false}
let btn_active = () => {
	let check = 0;
	for (var element in data) {
		if (data[element] == true ) {
			check += 1
		}
		if (check == 5) {
			button.removeAttribute("disabled", "disabled");
		}
		else {
			button.setAttribute("disabled", "disabled");
		}
	}
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
		data.email = true;
		btn_active()
	} 
	else {
		invalide(this);
		data.email = false;
		btn_active()
	}
});
// фамилия / имя / отчество / город
let data_one = [firstname, lastname, city]
data_one.forEach(element => {
	element.addEventListener("input", function(evt) {
		let inputs = this.value.replace(/[^a-zа-я\s]+/ig, "")
		this.value = inputs
		if (inputs.length > 2 ) {
			vilide(this)
			data[element.id] = true;
			btn_active()
		} 
		else {
			invalide(this)
			data[element.id] = false;
			btn_active()
		}
	});
});
// телефон
phone.addEventListener("input", function() {
	let inputs = this.value.replace(/[^0-9\s]+/ig, "")
	this.value = inputs
	if (inputs.length > 5 ) {
		vilide(this)
		data.phone = true;
		btn_active()
	} 
	else {
		invalide(this)
		data.phone = false;
		btn_active()
	}
});