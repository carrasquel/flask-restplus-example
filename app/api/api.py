from flask_restful import reqparse, Resource
from app.models import Event
from app import db
from app import status
import datetime


class EventAPI(Resource):

    def get(self, id):

        e = Event.query.filter_by(id=id).first()

        event = e.__dict__
        event["date"] = event["date"].isoformat()
        del event['_sa_instance_state']
        
        return event

    def delete(self, id):

        event = Event.query.filter_by(id=id).delete()

        db.session.commit()
        return '', status.HTTP_204_NO_CONTENT

    def put(self, id):

        event = Event.query.filter_by(id=id).first()

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name cannot be blank!')
        parser.add_argument('description', type=str, required=True, help='Description cannot be blank!')
        parser.add_argument('event_date', type=str, required=True, help='Date cannot be blank!')
        args = parser.parse_args()

        event.name = args["name"]
        event.description = args["description"]
        event.event_date = args["event_date"]
        event.date = datetime.datetime.now()

        db.session.commit()

        e = Event.query.filter_by(id=event.id).first()

        event = e.__dict__
        event["date"] = event["date"].isoformat()
        del event['_sa_instance_state']
        
        return event, status.HTTP_202_ACCEPTED


class EventListAPI(Resource):

    def get(self):

        result = list()

        for e in Event.query.all():

            event = e.__dict__
            event["date"] = event["date"].isoformat()
            del event['_sa_instance_state']

            result.append(event)

        return result

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name cannot be blank!')
        parser.add_argument('description', type=str, required=True, help='Description cannot be blank!')
        parser.add_argument('event_date', type=str, required=True, help='Date cannot be blank!')
        args = parser.parse_args()

        now = datetime.datetime.now()
        
        event = Event(name=args["name"],
                      description=args["description"],
                      event_date=args["event_date"],
                      date=now)

        db.session.add(event)
        db.session.commit()

        e = Event.query.filter_by(id=event.id).first()

        event = e.__dict__
        event["date"] = event["date"].isoformat()
        del event['_sa_instance_state']
        
        return event, status.HTTP_201_CREATED
