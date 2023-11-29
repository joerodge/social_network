from lib.post import Post
from lib.post_repository import PostRepository

def test_get_all_posts(db_connection):
    db_connection.seed("seeds/social.sql")
    post_repo = PostRepository(db_connection)
    all_posts = post_repo.all()
    assert len(all_posts) == 9
    assert all_posts == [
        Post(1, 'Test Title1 for user 1', 'Hello this is test post 1 u1', 39, 1),
        Post(2, 'Test Title2 for user 1', 'Hello this is test post 2 u1', 29, 1),
        Post(3, 'Test Title3 for user 1', 'Hello this is test post 3 u1', 102, 1),
        Post(4, 'Test Title1 for user 2', 'Hello this is test post 1 u2', 74, 2),
        Post(5, 'Test Title2 for user 2', 'Hello this is test post 2 u2', 39, 2),
        Post(6, 'Test Title3 for user 2', 'Hello this is test post 3 u2', 87, 2),
        Post(7, 'Test Title1 for user 3', 'Hello this is test post 1 u3', 21, 3),
        Post(8, 'Test Title2 for user 3', 'Hello this is test post 2 u3', 123, 3),
        Post(9, 'Test Title3 for user 3', 'Hello this is test post 3 u3', 12, 3),
    ]

def test_find_a_post_by_id(db_connection):
    db_connection.seed("seeds/social.sql")
    post_repo = PostRepository(db_connection)
    assert post_repo.find(7) == Post(7, 'Test Title1 for user 3', 'Hello this is test post 1 u3', 21, 3)

def test_find_when_id_doesnt_exist(db_connection):
    db_connection.seed("seeds/social.sql")
    post_repo = PostRepository(db_connection)
    assert post_repo.find(79) == None

def test_create_new_post(db_connection):
    db_connection.seed("seeds/social.sql")
    post_repo = PostRepository(db_connection)
    post_repo.create('New Post', 'This is a newly created post', 2)
    all_posts = post_repo.all()
    assert all_posts == [
        Post(1, 'Test Title1 for user 1', 'Hello this is test post 1 u1', 39, 1),
        Post(2, 'Test Title2 for user 1', 'Hello this is test post 2 u1', 29, 1),
        Post(3, 'Test Title3 for user 1', 'Hello this is test post 3 u1', 102, 1),
        Post(4, 'Test Title1 for user 2', 'Hello this is test post 1 u2', 74, 2),
        Post(5, 'Test Title2 for user 2', 'Hello this is test post 2 u2', 39, 2),
        Post(6, 'Test Title3 for user 2', 'Hello this is test post 3 u2', 87, 2),
        Post(7, 'Test Title1 for user 3', 'Hello this is test post 1 u3', 21, 3),
        Post(8, 'Test Title2 for user 3', 'Hello this is test post 2 u3', 123, 3),
        Post(9, 'Test Title3 for user 3', 'Hello this is test post 3 u3', 12, 3),
        Post(10, 'New Post', 'This is a newly created post', 0, 2),
    ]
    
def test_delete_a_post(db_connection):
    db_connection.seed("seeds/social.sql")
    post_repo = PostRepository(db_connection)
    post_repo.delete(3)
    all_posts = post_repo.all()
    assert all_posts == [
        Post(1, 'Test Title1 for user 1', 'Hello this is test post 1 u1', 39, 1),
        Post(2, 'Test Title2 for user 1', 'Hello this is test post 2 u1', 29, 1),
        Post(4, 'Test Title1 for user 2', 'Hello this is test post 1 u2', 74, 2),
        Post(5, 'Test Title2 for user 2', 'Hello this is test post 2 u2', 39, 2),
        Post(6, 'Test Title3 for user 2', 'Hello this is test post 3 u2', 87, 2),
        Post(7, 'Test Title1 for user 3', 'Hello this is test post 1 u3', 21, 3),
        Post(8, 'Test Title2 for user 3', 'Hello this is test post 2 u3', 123, 3),
        Post(9, 'Test Title3 for user 3', 'Hello this is test post 3 u3', 12, 3),
    ]