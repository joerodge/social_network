from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository
from lib.user_respository import UserRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social.sql")

# Retrieve all users and list them
user_repository = UserRepository(connection)
users = user_repository.all()
print("Here are all the registered users:")
for user in users:
    print(user)

# Get all posts and print them out
post_repo = PostRepository(connection)
print("\nHere are all the posts:")
for post in post_repo.all():
    print(post)
