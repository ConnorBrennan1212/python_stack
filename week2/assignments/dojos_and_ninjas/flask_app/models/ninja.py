from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.Dojos_id = data['Dojos_id']

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM ninjas WHERE Dojo_id= %(Dojo_id)s"
        results = connectToMySQL('dojosandninjas').query_db(query)
        dojos = []

        for d in results:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def save(cls, data):
        query= "INSERT INTO `dojosandninjas`.`ninjas` (`first_name`, `last_name`, `age`, `Dojos_id`) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        result = connectToMySQL('dojosandninjas').query_db(query, data)
        print('this is the result from the query...', result)
        return result


