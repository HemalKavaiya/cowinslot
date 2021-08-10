# Cowinslot

Cowinslot is a website that will notify users automatically whenever a free appointment slot for vaccines becomes available in cowin.gov.in.

## Live Demo
[Cowinslot](https://cowinslot.herokuapp.com/ "Cowinslot")

## Features
- Notify users 
- Find nearest vaccination center 

## Built with
- Python
- Django
- SMTP

## Prerequisites
1. Clone the repo

```sh 
https://github.com/HemalKavaiya/cowinslot.git
```

2. Enter your email details and secret key in [Settings.py](https://github.com/HemalKavaiya/cowinslot/blob/14f8789cdd1f84d3e47968530614863be7bb8b47/appointment/settings.py "Settings.py")

```python
SECRET_KEY = 'xyz'

EMAIL_HOST_USER = "youremail.com"
EMAIL_HOST_PASSWORD = "yourpassword"
```

3. Run manage.py

```sh
Python manage.py runserver
```

## License
[MIT](https://github.com/HemalKavaiya/cowinslot/blob/14f8789cdd1f84d3e47968530614863be7bb8b47/LICENSE)
