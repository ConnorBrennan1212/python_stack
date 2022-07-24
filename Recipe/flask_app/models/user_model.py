from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        # etc... 45 min in ish


    @staticmethod 
        def validate_registration(data):
            is_valid = True
            if len(data['first_name'])<2
                flash('your first name needs to have at least 2 characters')
                is_valid= False
            if len(data['last_name'])<2
                flash('your last name needs to have at least 2 characters')
                is_valid = False



