# encoding: utf-8
# app/modules/auth/__init__.py

from app.extensions import db
from .utils import hash_password, verify_password, generate_key


class User(db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(20))
    password = db.Column(db.String(32))
    key = db.Column(db.String(36), default="")
    email = db.Column(db.String(40))
    
    todos = db.relationship('ToDo', backref='user', lazy=True)
    events = db.relationship('Event', backref='user', lazy=True)
    
    def __repr__(self):

        return '<User: {0}>'.format(self.username)
    
    @staticmethod
    def read_user(username):
        
        user = User.query.filter_by(username=username).first()
        
        return user

    @staticmethod
    def verify_username(username):
        
        user = User.read_user(username)

        if user:
            return True
        
        return False
        
    @staticmethod
    def read_by_key(key):
        
        user = User.query.filter_by(key=key).first()
        
        return user    
    
    @staticmethod
    def create(username, password, email):

        password = hash_password(password)
        
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
    def get_key(username):

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
        db.session.commit()
        
    def get_todos(self):
    
        return self.todos

    def delete_todo(self, todo_id):

        for todo in self.todos:
            if todo.id == todo_id:
                db.session.delete(todo)
                db.session.commit()
                
                return True
        
        return False
        
    def owns_todo(self, todo_id):

        for todo in self.todos:
            if todo.id == todo_id:
                return True
        
        return False
    
    def add_event(self, event):
    
        self.events.append(event)
        db.session.commit()

    def delete_event(self, event_id):

        for event in self.events:
            if event.id == event_id:
                db.session.delete(event)
                db.session.commit()
                
                return True
        
        return False
        
    def get_events(self):
    
        return self.events

    def owns_event(self, event_id):

        for event in self.events:
            if event.id == event_id:
                return True
        
        return False