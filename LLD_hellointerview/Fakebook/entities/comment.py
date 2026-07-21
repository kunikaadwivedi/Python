from user import User
from commentable_entity import CommentableEntity
from typing import List

class Comment(CommentableEntity):
    def __init__(self, author:'User', content:str):
        super().__init__(author, content)
    
    def get_replies(self)-> List['Comment']:
        return self.get_comments()
    