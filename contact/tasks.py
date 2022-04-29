from django_product.celery import app
from django_product.service_email import email, email_all_user
from .models import Mailing, Contact

@app.task
def send_mailing(usser_email):
    title = "Игрульки от Ирульки"
    message = "Вы подписались на нашу рассылку. Мы будем присылать вам новости."
    to_email = usser_email
    email(title, message, to_email)


@app.task
def send_mailing_all(task_id):
    mailing = Mailing.objects.get(id=task_id)
    
    if mailing.is_active == True:
        emails = Contact.objects.all()

        for user in emails:
            title = mailing.title
            message = mailing.text
            to_email = user.email

            email_all_user(title, message, to_email)
    