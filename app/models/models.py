# app/models/models.py

from app.server import server
from .utils import hash_password, verify_password, generate_key

db = server.database


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

        user = User.query.filter_by(username=username).first()
        
        return user.key

    @staticmethod
    def set_key(username):
    
        user = User.query.filter_by(username=username).first()
        key = generate_key()
        
        User.delete_key(username)

        user.key = key
        db.session.commit()
        
    @staticmethod
    def delete_key(key):
    
        try:
            user = User.query.filter_by(key=key).first()
            user.key = ""
            db.session.commit()
        except:
            pass
            
    @staticmethod
    def verify_key(key):

        try:
            user = User.query.filter_by(key=key).first()
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
    finished = db.Column(db.Boolean)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):

        return '<Todo: {0}>'.format(self.id)
        
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
    def delete(self, _id):
    
        todo = ToDo.query.filter_by(id=_id).first()
        db.session.delete(todo)
        db.session.commit()