from post_observer import PostObserver
from entities.post import Post
from entities.user import User
from entities.comment import Comment
from entities.commentable_entity import CommentableEntity

class UserNotifier(PostObserver):
    def on_post_created(self, post:Post):
        author = post.get_author()
        for friend in author.get_friends():
            