# PDF to tag-cloud generator

## Installation

Run the following commands in terminal:

```
pip install virtualenv --user
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Running the project
```
python manage.py migrate

(Sync Dev Mode)
python manage.py runserver
(ASync Dev Mode)
pip install daphne
daphne CrossMLAssignment.asgi:application

```
## Author
Davinder Singh
https://in.linkedin.com/in/davinder-singh-73943888