from lib.user import User

def test_creatation():
    user = User(1, 'testuser', 'test@email.com')
    assert user.id == 1
    assert user.username == 'testuser'
    assert user.email == 'test@email.com'

def test_equal():
    user1 = User(1, 'testuser', 'test@email.com')
    user2 = User(1, 'testuser', 'test@email.com')
    assert user1 == user2

def test_repr():
    user = User(1, 'testuser', 'test@email.com')
    assert str(user) == "User(1, testuser, test@email.com)"
    
