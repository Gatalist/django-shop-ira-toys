// перебор события кнопок добавления
let buttonsAdd = document.querySelectorAll(".product-add");
for (let i = 0; i < buttonsAdd.length; i++) {
	buttonsAdd[i].addEventListener("submit", function(evt) {
		evt.preventDefault();
		buttonsControlAdd(this)
	});
}
// перебор события кнопок удаления
$(document).on('click', '.product-card-removes', function(){
	this.addEventListener("submit", function(evt) {
		evt.preventDefault();
		buttonsControlRemove(this)
	});
})
// Отправляем данные с кнопки добавления продукта
function buttonsControlAdd(button) {
	let data_button = button.querySelector(".product-cart");
	let id = data_button.getAttribute('data-id');
	let image = data_button.getAttribute('data-img');
	let number = button.number.value;
	if (number < 1) {
		number = 1
	}
	let csrf_token = $('.product-add [name="csrfmiddlewaretoken"]').val();
	let url = $(button).attr("action");
	let data = {};
	data["product_id"] = id;
	data["numbers"] = number;
	data["image"] = image;
	data["csrfmiddlewaretoken"] = csrf_token;
	data["remove"] = 'false';
	ajaxSendServer(data, url);
}
// Отправляем данные с кнопки удаления продукта
function buttonsControlRemove(button) {
	let data_button = button.querySelector(".pro-remove");
	let id = data_button.getAttribute('data-id');
	let csrf_token = $('.product-card-removes [name="csrfmiddlewaretoken"]').val();
	let url = $(button).attr("action");
	let data = {};
	data["product_id"] = id;
	data["csrfmiddlewaretoken"] = csrf_token;
	data["remove"] = 'true';
	ajaxSendServer(data, url);
}
// ajax запрос на сервер
let ajaxSendServer = (data, url) => {
	let clearBasked = document.getElementById('basket-product');
	clearBasked.innerHTML = '';
	$.ajax({
		url: url,
		type: 'POST',
		data: data,
		cashe: true,
		success: function(data) {
			data_products = data.products
			// console.log(data)
			if ( data.valuta_change ) {
				window.location.reload()
			}
			// вывод количества елементов в корзине menu
			document.querySelector(".cart-item_count").innerHTML = data.products_total_nmb;		
			BasketStyle(data_products);			
			all_sum = 0;
			data_products.forEach(element => {
				addInBasket(element);
				all_sum += element.sum;
			});
			// сумма заказа в корзине header
			let tag_all_sum = document.querySelector("#all_sum");
			tag_all_sum.innerText = all_sum.toFixed(2);
			// таблица заказа
			let all_sum_table = document.querySelector(".total-amount-table");
			if (all_sum_table) {
				all_sum_table.innerText = all_sum.toFixed(2);
				if (all_sum == 0) {
					let table_delete = document.querySelector(".clear-table-all");
					table_delete.innerHTML = "<div style='min-height:200px; margin-top:120px'> <h3 class= 'text-center'>Корзина пустая</h3> </div>"
				}
				basketBtnOrder();
			}
		},
		error: function() {
			console.log(error);
		}
	})

};
// проверка суммы заказа
let basketBtnOrder = () => {
	let all_sum_table = document.querySelector(".total-amount-table");
	let valuta = $('#valuta option:selected').text();
	if (all_sum_table) {
		let btn_all_sum = document.querySelector("#all_sum").textContent;
		console.log(btn_all_sum)
		let num_num = parseInt(btn_all_sum.replace(",", "."));
		let disablet_btn_basket = document.querySelector("#checkout");
		if (valuta == 'USD' || valuta == 'EUR') {
			if (num_num < 100) {	
				disablet_btn_basket.classList.add('disabled');
			}
			else {	
				disablet_btn_basket.classList.remove('disabled');
			}
		}
		if (valuta == 'ГРН') {
			if (num_num < 3000) {		
				disablet_btn_basket.classList.add('disabled');
			}
			else {
				disablet_btn_basket.classList.remove('disabled');
			}
		}
	}
}
basketBtnOrder();
// меняем блок корзины
let BasketStyle = (products) => {
	let shopping = document.getElementById('shopping');
	if (products.length < 1) {
		shopping.style.height = '60px';
		shopping.style.overflow = 'hidden';
	}
	else if (products.length == 1) {
		shopping.style.height = '200px';
		shopping.style.overflow = 'hidden';
	}
	else if (products.length == 2) {
		shopping.style.height = '320px';
		shopping.style.overflow = 'hidden';
	}
	else {
		shopping.style.height = '350px';
		shopping.style.overflow = 'scroll';
	}
};
// Перерендеринг товаров в корзине
let addInBasket = (element) => {
	let basket = document.querySelector('#basket-product')
	let product = document.querySelector('#castom').content;
	let img = product.querySelector(".img");
	img.src = element.img;
	let name = product.querySelector(".title");
	name.innerText = element.name;
	let number = product.querySelector(".number");
	number.innerText = element.numbers;
	let summ = product.querySelector(".summ")
	summ.innerText = (element.price).toFixed(2);
	let price = product.querySelector(".cart-price > b")

	price.innerText = `${(element.sum).toFixed(2)}`;
	let id_update = product.querySelector('.pro-remove');
	id_update.dataset.id = element.id;
	let copyBlock = product.cloneNode(true);
	basket.prepend(copyBlock);
};
// изменение суммы / количества в таблице заказа
$(document).on('change', '.table-plus-minus', function(evt){
	let numbers = $(evt.target).val()
	if (numbers < 1) {
		numbers = 1
	}
	let id = $(this).data("id");
	let image = $(this).data("image");
	let csrf_token = getCookie('csrftoken');
	let url = "/orders/basket_adding/";
		
	let table = document.querySelector("tbody");
	let td = table.querySelectorAll("td");
	let price = 0;
	let sum = 0;
	for (let for_td = 0; for_td < td.length; for_td++) {
		let td_elem = td[for_td]
		let td_id = td_elem.getAttribute('data-td-id');
		if (td_id == id) {			
			if ( td_elem.classList == 'pro-price') {
				price = td_elem.querySelector('.pro-price-table').textContent;		
			}
			if ( td_elem.classList == 'pro-subtotal') {
				sum = td_elem.querySelector('.pro-subtotal-table');		
			}
			let price_2 = price.toString().replace(",", '.')
			let sum_td_table = Number(price_2) * Number(numbers);
			sum.innerText = sum_td_table.toFixed(2);;
		}
	}
	
	let data = {};
	data["product_id"] = id;
	data["numbers"] = numbers;
	data["image"] = image;
	data["csrfmiddlewaretoken"] = csrf_token;
	data["remove"] = 'false';
	ajaxSendServer(data, url);
});

// кнопка удаления с таблицы
$(document).on('click', '.pro-remove-table', function(evt){
	evt.preventDefault();
	buttonsTableRemove(this)
	id = $(this).data("id");
	let table = document.querySelector("tbody");
	let td = table.querySelectorAll("td");

	for (let elem_td = 0; elem_td < td.length; elem_td++) {
		let td_id = td[elem_td].getAttribute('data-td-id')
		if (td_id == id) {
			$(td[elem_td]).closest('td').remove();
		}
	}
});
function buttonsTableRemove(button) {
	let id = $(button).data("id")
	let csrf_token = getCookie('csrftoken');

	let url = "/orders/basket_adding/";
	let data = {};
	data["product_id"] = id;
	data["csrfmiddlewaretoken"] = csrf_token;
	data["remove"] = 'true';
	ajaxSendServer(data, url);
}
// изменение valuta
$('#valuta').on('change', function() {
	let csrf_token = getCookie('csrftoken');
	let url = "/currency/valuta/";
	let data = {};
	data["valuta"] = this.value;
	data["csrfmiddlewaretoken"] = csrf_token;
	console.log(data, url)
	ajaxSendServer(data, url);
});
// add/remove - language pc
window.addEventListener('resize', hiden_language_desktop);
function hiden_language_desktop(){
	let language = document.querySelector('#language-pc')
	let size = document.documentElement.clientWidth
	if (size <= 976) {		
		language.classList.add('d-none');
	}
	else {
		language.classList.remove('d-none');
	}
}
hiden_language_desktop()
// return cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}