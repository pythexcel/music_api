# MusicAPI #

## Summary: ##

A music student want to see all the assignments in one place in one simple view, so these are the server side apis to GET and POST the assignments by user.

Project stack:
1. Python3
2. Django
3. Django REST Framework


### Here we have: ###

* An assignment app where user can GET all the assignments in a single view and POST the assignment.


## Initial Project Setup ##

```bash
git clone https://github.com/pythexcel/music_api.git
cd musicApi
python -m venv env
source env\bin\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Test Case Example:

### Request (POST):

```bash
method: POST
request: http://127.0.0.1:8000/assignment/
```

```bash
Payload:

{
    "title": "Assignment One",
    "description": "This is a description.",
    "musicGenre": "Rock Music",
    "dailyPracticeTime": 6,
    "days": 5,
    "daysPracticed": 5
}
```

### Response:

```bash
{
    "id": 1,
    "title": "Assignment One",
    "description": "This is a description.",
    "musicGenre": "Rock Music",
    "dailyPracticeTime": 6,
    "days": 5,
    "daysPracticed": 5
}
```

### Request (GET):

```bash
method: GET
request: http://127.0.0.1:8000/assignment/
```

### Response:

```bash
[
    {
        "id": 1,
        "title": "Assignment One",
        "description": "This is a description.",
        "musicGenre": "Rock Music",
        "dailyPracticeTime": 6,
        "days": 5,
        "daysPracticed": 5
    },
    {
        "id": 2,
        "title": "Assignment Two",
        "description": "This is a description.",
        "musicGenre": "Soul Music",
        "dailyPracticeTime": 8,
        "days": 5,
        "daysPracticed": 4
    }
]
```
