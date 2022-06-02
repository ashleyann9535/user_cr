from mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#use class method to get info from database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'

    #call connection
        results = connectToMySQL('users_schema').query_db(query)
    #empty list to hold users
        users = []

    #loop through the results
        for user in results:
            users.append( cls(user))
        
        return users

#save new user to database
    @classmethod
    def save(cls, data):
    #prepared query
        query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at)\
            VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());'
    #data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db(query, data)
