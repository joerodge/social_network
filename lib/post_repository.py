from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        posts = []
        for row in rows:
            posts.append(Post(row['id'], row['title'], row['content'], row['views'], row['user_id']))
        return posts

    def find(self, id):
        rows = self._connection.execute(
            "SELECT * FROM posts WHERE id = %s", [id]
        )
        if rows:
            row = rows[0]
            return Post(row['id'], row['title'], row['content'], row['views'], row['user_id'])

    def create(self, title, content, user_id):
        self._connection.execute(
            "INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s)",
            [title, content, 0, user_id])

    def delete(self, id):
        self._connection.execute(
            "DELETE FROM posts WHERE id = %s", [id]
        )