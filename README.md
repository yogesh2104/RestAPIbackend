# RestAPIbackend

## Step 1
```
pip install -r requirements.txt
```
## After Installing requirements.txt
## Add database details in settings.py file  
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #for mysql database
        'NAME': 'true_value_access', # database name
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306' #database port 
    }
}
```

```
python manage.py makemigrations
```
## Then

```
python manage.py migrate
```
## After Migrate Run Project On Local Machine
```
python manage.py runserver
```
## Project on local machine on http://127.0.0.1:8000/ this port

## For Admin Panel Create superuser

```
python manage.py createsuperuser
```
## Enter username and password then restart server and run
```
python manage.py runserver
```

## And type this url on your browser http://127.0.0.1:8000/admin 