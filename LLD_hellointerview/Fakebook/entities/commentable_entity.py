import uuid
from user import User
from typing import List, Set
from comment import Comment
from datetime import datetime


class CommentableEntity:
    def __init__(self, author:'User', content:str):
        self.id = str(uuid.uuid4())
        self.author = author
        self.content = content
        self.created_at = datetime.now()
        self.comments: List['Comment']= []
        self.likes: Set['User'] = set()
        
    def add_like(self, user:'User'):
        self.likes.add(user)
        
    def add_comment(self, comment:'Comment'):
        self.comments.append(comment)  
        
    def get_id(self) -> str:
        return self.id
    
    def get_author(self) -> User:
        return self.author
    
    def get_content(self) -> str:
        return self.content
    
    def get_timestamp(self) -> datetime:
        return self.created_at
    
    def get_likes(self) -> Set['User']:
        return self.likes
    
    def get_comments(self) -> List['User']:
        return self.comments