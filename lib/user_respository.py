from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        posts = []
        for row in rows:
            posts.append(User(row['id'], row['username'], row['email']))
        return posts

    def find(self, id):
        rows = self._connection.execute(
            "SELECT * FROM users WHERE id = %s", [id]
        )
        if rows:
            row = rows[0]
            return User(row['id'], row['username'], row['email'])

    def create(self, username, email):
        self._connection.execute(
            "INSERT INTO users (username, email) VALUES (%s, %s)",
            [username, email])
        
    def delete(self, id):
        self._connection.execute(
            "DELETE FROM users WHERE id = %s", [id]
        )