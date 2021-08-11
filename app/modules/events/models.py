# encoding: utf-8

import datetime

from app.extensions import db


class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(200))
    event_date = db.Column(db.String(20))
    date = db.Column(db.DateTime())
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):

        return '<Event: {0}>'.format(self.name)
    
    @staticmethod
    def read_event(_id):
        
        event = Event.query.filter_by(id=_id).first()
        
        return event

    @staticmethod
    def create(name, description, event_date, date):
        
        event = Event(name=name, description=description, event_date=event_date, date=date)
        
        db.session.add(event)
        db.session.commit()
        
        return event
        
    @staticmethod
    def update(_id, values):

        values["date"] = datetime.datetime.now()
    
        event = Event.query.filter_by(id=_id).update(values)
        db.session.commit()
    
    @staticmethod
    def delete(self, _id):
    
        event = Event.query.filter_by(id=_id).first()
        db.session.delete(event)
        db.session.commit()

    def to_dict(self):

        result = self.__dict__
        result["date"] = result["date"].isoformat()
        del result['_sa_instance_state']

        return result
        