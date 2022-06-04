from mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#Create
#save new user to database
    @classmethod
    def save(cls, data):
    #prepared query
        query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at)\
            VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());'
    #data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db(query, data)

#Read
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

#view one user
    @classmethod
    def view_one(cls, id):
    #make data into usable dictionary
        data = {'id': id}
    #create query
        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
    #make variable for query result
        result = connectToMySQL('users_schema').query_db(query, data)
    #result comes back as a list
        return cls(result[0])

#Update
    @classmethod
    def update(cls, data):
    #create query
        query = """
        UPDATE users\
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at=NOW()\
        WHERE id = %(id)s
        ;"""
        return connectToMySQL('users_schema').query_db(query,data)


#Delete
    @classmethod
    def delete_user(cls, id):
    #make data into usable dictionary
        data = {'id': id}
    #create query
        query = """
        DELETE FROM users WHERE id = %(id)s
        ;"""
        return connectToMySQL('users_schema').query_db(query, data)
