from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data ['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);'

        result = connectToMySQL('login').query_db(query,data)
        return result



    @staticmethod
    def validate_user(data):
        is_valid = True
        
        #first_name
        if len(data['first_name']) < 3 or len(data['first_name']) > 20:
            is_valid = False
            flash('first name must be between 2 and 20 characters')
        #last_name
        if len(data['last_name']) < 3 or len(data['last_name']) > 20:
            is_valid = False
            flash('last name must be between 2 and 20 characters')
        #email
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('email address must be in correct format')
        #password
        if len(data['password'])<8:
            is_valid = False
            flash('password must be at least 8 characters long')

        if data['password'] != data['confirm_password']:
            is_valid = False
            flash('password and confirm password must match')

        return is_valid