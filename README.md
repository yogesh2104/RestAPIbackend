# RestAPIbackend

## Install Requirement.txt file
```
pip install -r requirements.txt
```
## After Installing
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
# Afert Adding database details in settings.py make Migrations and Migrate
```
python manage.py makemigrations
```
```
python manage.py migrate
```
## After Migrate Run Project On Local Machine
```
python manage.py runserver
```
## Project on local machine on http://127.0.0.1:8000/api/users/ this port
## Api Endpoint
```
1. api/user # ListDown All User List by default show 5 user and sort list by name
2. api/user-detail/<id>/ # Return specific user details
3. api/create-list/ #Make new user data
4. api/update-list/<id>   #Update details of a user
5. api/delete-user/<id>  #Delete a user
```

## For Admin Panel Create superuser

```
python manage.py createsuperuser
```
## Enter username and password then restart server and run
```
python manage.py runserver
```

## And type this url on your browser http://127.0.0.1:8000/admin 
