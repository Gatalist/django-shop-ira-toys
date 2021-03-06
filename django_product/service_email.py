from django.core.mail import send_mail
from django_product.settings import DEFAULT_FROM_EMAIL
from django.template.loader import render_to_string

from django.core.mail import EmailMultiAlternatives

def send_to_email(title, to_email, file, html_content):
    irina = 'test@gmail.com'
    sergey = 'test@gmail.com'
    try:
        emailMessage = EmailMultiAlternatives(subject=title, from_email=DEFAULT_FROM_EMAIL, to=[to_email, irina, sergey])
        # emailMessage = EmailMultiAlternatives(subject=title, from_email=DEFAULT_FROM_EMAIL, to=[to_email])
        emailMessage.attach_file(file)
        emailMessage.attach_alternative(html_content, "text/html")
        emailMessage.send(fail_silently=False)

    except SMTPException as e:
        print('There was an error sending an email: ', e) 
        error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
        raise serializers.ValidationError(error)


# подписка
def email(title, message, to_email):
    send_mail(
        title, 
        message, 
        DEFAULT_FROM_EMAIL, 
        [to_email],
        fail_silently=False
    )

# заказ
def email_order(title, message, to_email):
    send_mail(
        title, 
        message, 
        DEFAULT_FROM_EMAIL, 
        [to_email], 
        fail_silently=False
    )

# рассылка
def email_all_user(title, message, to_email):
    send_mail(
        title, 
        message, 
        DEFAULT_FROM_EMAIL, 
        [to_email], 
        fail_silently=False
    )
