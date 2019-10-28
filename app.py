# app.py

# Import packages/modules
from flask import Flask, escape, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import math
import json

# Init flask
app = Flask(__name__)

# Configs
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://daniel:d4n13l@localhost:3306/contacts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Init SQLAlchemy
db = SQLAlchemy(app)


# Models
class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(128), nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.utcnow())
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Contact(name='%s')>" % (self.name)
    
    @property
    def serialize(self):
        return {
            'name': self.name
        }

def get_contacts():
    contacts = Contact.query.all()
    return jsonify(data=[c.serialize for c in contacts])

def post_contact(name):
    contact = Contact(name=name)
    db.session.add(contact)
    db.session.commit()
    return jsonify(data=contact.serialize)

@app.route('/api/contacts', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return get_contacts()
    elif request.method == 'POST':
        name = request.form.get('name', '')
        return post_contact(name)

if __name__ == '__main__':
    app.run(debug=True)
