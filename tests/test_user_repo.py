from lib.user import User
from lib.user_respository import UserRepository

def test_get_all_users(db_connection):
    db_connection.seed("seeds/social.sql")
    user_repo = UserRepository(db_connection)
    all_users = user_repo.all()
    assert all_users == [
        User(1, 'TestUsername1', 'test1@email.com'),
        User(2, 'TestUsername2', 'test2@email.com'),
        User(3, 'TestUsername3', 'test3@email.com'),
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social.sql")
    user_repo = UserRepository(db_connection)
    assert user_repo.find(2) == User(2, 'TestUsername2', 'test2@email.com')

def test_find_isnt_in_db(db_connection):
    db_connection.seed("seeds/social.sql")
    user_repo = UserRepository(db_connection)
    assert user_repo.find(53) == None

def test_create(db_connection):
    db_connection.seed("seeds/social.sql")
    user_repo = UserRepository(db_connection)
    user_repo.create('NewUser', 'new@email.com')
    all_users = user_repo.all()
    assert all_users == [
        User(1, 'TestUsername1', 'test1@email.com'),
        User(2, 'TestUsername2', 'test2@email.com'),
        User(3, 'TestUsername3', 'test3@email.com'),
        User(4, 'NewUser', 'new@email.com')
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/social.sql")
    user_repo = UserRepository(db_connection)
    user_repo.delete(2)
    all_users = user_repo.all()
    assert all_users == [
        User(1, 'TestUsername1', 'test1@email.com'),
        User(3, 'TestUsername3', 'test3@email.com'),
    ]
