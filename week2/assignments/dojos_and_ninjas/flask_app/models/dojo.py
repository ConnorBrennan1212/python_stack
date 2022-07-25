from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM dojos;"
        results = connectToMySQL('dojosandninjas').query_db(query)
        print("these are the results for get all", results)
        dojos = []

        for d in results:
            dojos.append(cls(d))
        print("these are all the dojos", dojos)
        return dojos

    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name) VALUES (%(dojoname)s);"
        result = connectToMySQL('dojosandninjas').query_db(query, data)
        print('this is the result from the query...', result)
        return result

    @classmethod
    def show_ninja_dojo(cls, data):
        query='SELECT * FROM dojos Left Join ninjas on dojos.id=ninjas.Dojos_id Where dojos.id=%(id)s;'
        result = connectToMySQL('dojosandninjas').query_db(query, data)
        dojo = cls(result[0])
        for row_from_db in result:

            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"],
                "Dojos_id": row_from_db['Dojos_id']
            }

            dojo.ninjas.append( Ninja( ninja_data ) )

        return dojo