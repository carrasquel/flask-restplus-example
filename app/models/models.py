# app/models/models.py

from .utils import hash_password, verify_password, generate_key
from .. import db


class User(db.Model):

    __tablename__ = 'todos'
    
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    key = db.Column(db.String(20), default="")
    email = db.Column(db.String(20))
    
    todos = db.relationship('ToDo', backref='user', lazy=True)
    events = db.relationship('Event', backref='user', lazy=True)
    
    def __repr__(self):

        return '<User: {0}>'.format(self.username)
    
    @staticmethod
    def read_user(username):
        
        user = User.query.filter_by(username=username).first()
        
        return user
        
    @staticmethod
    def read_by_key(key):
        
        user = User.query.filter_by(key=key).first()
        
        return user    
    
    @staticmethod
    def create(username, password, email):
        
        user = User(username=username, password=password, email=email)
        
        db.session.add(user)
        db.session.commit()
        
        return user
        
    @staticmethod
    def login(username, password):
    
        user = User.query.filter_by(username=username).first()
        
        try:
            User.logout(username)
        except:
            pass
            
        if verify_password(user.password, password):
            
            User.set_key(username)

            return True

        return False  

    @staticmethod
    def logout(username):

        User.delete_key(username)

        return True
    
    @staticmethod
    def _get_key(username):

        user = User.read_user(username)
        
        return user.key

    @staticmethod
    def set_key(username):
    
        user = User.read_user(username)
        key = generate_key()
        
        User.delete_key(username)

        user.key = key
        db.session.commit()
        
    @staticmethod
    def delete_key(key):
    
        try:
            user = User.read_by_key(key)
            user.key = ""
            db.session.commit()
        except:
            pass
            
    @staticmethod
    def verify_key(key):

        try:
            user = User.read_by_key(key)
            return True
        except:
            return False
            
    def add_todo(self, todo):
    
        self.todos.append(todo)
        
    def get_todos(self):
    
        return self.todos
        
    def add_event(self, event):
    
        self.events.append(event)
        
    def get_events(self):
    
        return self.events


class ToDo(db.Model):

    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80))
    finished = db.Column(db.Boolean, default=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):

        return '<Todo: {0}>'.format(self.id)
        
    def finished(self):
    
        self.finished = True
        db.session.commit()
        
    def unfinish(self):
    
        self.finished = False
        db.session.commit()
        
    @staticmethod
    def create(task):
        todo = ToDo(task=task)
        
        db.session.add(todo)
        db.session.commit()
        
        return todo
        
    @staticmethod
    def update(self, _id, values):
    
        todo = ToDo.query.filter_by(id=_id).update(values)
        db.session.commit()
        
    @staticmethod
    def delete(self, _id):
    
        todo = ToDo.query.filter_by(id=_id).first()
        db.session.delete(todo)
        db.session.commit()
    

class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(200))
    event_date = db.Column(db.String(20))
    date = db.Column(db.DateTime())
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):

        return '<Event: {0}>'.format(self.name)
        
    @staticmethod
    def create(name, description, event_date, date):
        
        event = Event(name=name, description=description, event_date=event_date, date=date)
        
        db.session.add(event)
        db.session.commit()
        
        return event
        
    @staticmethod
    def update(self, _id, values):
    
        event = Event.query.filter_by(id=_id).update(values)
        db.session.commit()
    
    @staticmethod
    def delete(self, _id):
    
        todo = ToDo.query.filter_by(id=_id).first()
        db.session.delete(todo)
        db.session.commit()