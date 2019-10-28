Flask App Example 1.0
---

## Run migrations
$ python
$ from app import db
$ db.create_all()
$

## Run flask app
export FLASK_ENV=production
export FLASK_APP=app.py
flask run --reload
