from mongoengine import *

class Task(Document):
    local_id = StringField()
    name = StringField()
    done = BooleanField()
class Message(Document):
    message = StringField()