# BlogProject

# To install use pip, Install the following:

pip3 install django  
pip3 install Pillow  
pip3 install djangorestframework  
pip3 install djangorestframework-simplejwt  
pip3 install django_seed  
pip3 install mysql  


# Migrate the database  

python3 manage.py makemigrations  
python3 manage.py migrate  

# ENV File

add the env file containing the details below:

MYSQL_ROOT_PASSWORD=root  
MYSQL_USER=admin  
MYSQL_PASSWORD=password12345  
MYSQL_DATABASE=djangoblog  
MYSQL_HOST=127.0.0.1  
MYSQL_PORT=3306  

SECRET_KEY = 'django-insecure-0apg5!no#x61y=($$%25g7q8@h+665aa7pjhyna(4-9f^crjh%'


#Run the project

python3 manage.py runserver  


