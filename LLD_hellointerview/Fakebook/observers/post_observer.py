from abc import ABC, abstractmethod
from entities.post import Post
from entities.user import User
from entities.comment import Comment

class PostObserver(ABC):
    @abstractmethod
    def on_post_created(self, post:Post):
        pass
    
    @abstractmethod
    def on_like(self, post:Post, user:User):
        pass
    
    @abstractmethod
    def on_comment(self, post:Post, comment:Comment):
        pass