# BlogProject

# To install use pip, Install the following:

pip install django  
pip install Pillow  
pip install djangorestframework  
pip install djangorestframework-simplejwt  
pip install django_seed  
pip install mysql  


# Migrate the database

python manage.py makemigrations  
python manage.py migrate  

# Make some changes in the settings.py Database

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'database name',  
        'USER' : 'user name',  
        'PASSWORD':'database password',  
        'HOST': '127.0.0.1',  
        'PORT' : '3306'  
    }
}

