## Разработан интернет магазин https://ira-toys-by-7km.com/ с таким функционалом

1) Корзина заказа
2) Новости сайта
3) Отзывы пользователей
4) Добавлена мультиязычность сайта - ru, ua
5) Минимальная сумма заказа для оформления
6) Подписка на рассылку по Email. Рассылка писем
7) Главная страница с баннерами, последними добавленными товарами, последними отзывами
8) Блок Новинки показывает все товары добавленные за последние 14 дней, а также по дням, если товару больше 14 дней после публикации ссылка убирается и на товаре пропадает стикер Новинка
9) Добавлено Кеширование меню для более быстрой  загрузки сайта, кеш обновляется автоматически каждые 10 мин
10) Поиск на сайте по названию и ид товара
11) Отображение цены в валюте - ГРН, USD. Курс валюты настраивается через админку
12) Обновление статусов карточек товара через Excel документ ( есть в наличии, нет в наличии, наличие уточняет менеджер). Просмотр результата обновления.
13) Добавлен текстовый редактор CKEDITOR
14) Формирование заказа в базу данных (также отображение в админке), дополнительное формирование Excel документа и отправка на Email менеджеру и клиенту
15) Используется менеджер задач Celery в связке с Redis
16) База данных Postgresql
17) Сайт работает через прокси-сервер Nginx
18) Давлена автоматическая генерация сертификата https через сервис certbot

## В разработке, заказчик еще думает:
1) Автоматическая генерация sitemaps
2) Управление SEO тегами через административную панель
3) файл Robots.txt