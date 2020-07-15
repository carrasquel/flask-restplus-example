# encoding: utf-8
# app/modules/auth/__init__.py

from app.extensions import db


class ToDo(db.Model):

    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80))
    finished = db.Column(db.Boolean, default=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
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
    

