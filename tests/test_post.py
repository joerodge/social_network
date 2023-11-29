from lib.post import Post

def test_object_created_correctly():
    post = Post(1, 'test title', 'test content', 34, 2)
    assert post.id == 1
    assert post.title == 'test title'
    assert post.content == 'test content'
    assert post.views == 34
    assert post.user_id == 2

def test_different_instances_with_same_values_are_equal():
    post1 = Post(1, 'test title', 'test content', 34, 2)
    post2 = Post(1, 'test title', 'test content', 34, 2)
    assert post1 == post2

def test_post_is_printed_correctly():
    post = Post(1, 'test title', 'test content', 34, 2)
    assert str(post) == "Post(1, test title, test content, 34, 2)"
