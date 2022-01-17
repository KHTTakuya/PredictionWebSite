import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MY_SECRET_KEY = 'django-insecure-=e$^lo8_9lh7v&!!u2d8v#(qfi)3dk39i-!3wm8s1d5%6p9%4#'

MY_DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# EMAIL
MY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
MY_EMAIL_HOST = 'smtp.gmail.com'
MY_EMAIL_HOST_USER = 'testaltopota@gmail.com'
MY_EMAIL_HOST_PASSWORD = 'rawywlwlcozkeyxv'
MY_EMAIL_PORT = 587
MY_EMAIL_USE_TLS = True
