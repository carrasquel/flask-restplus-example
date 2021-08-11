# encoding: utf-8

# app/api/events.py

import datetime

from flask import request
from flask_restplus import Namespace, Resource, fields

from app.extensions.api import api
from app.extensions import status
from app.modules.auth import User
from app.modules.api.utils import token_required

from .models import Event

ns = Namespace('events', description='Namespace for events')

event_model = api.model("event_model", {
    'name': fields.String(required=True, description='Event Name'),
    'description': fields.String(required=True, description='Event Description'),
    'event_date': fields.String(required=True, description='Event Date')
})


@ns.route('/')
class EventCollectionResource(Resource):
    
    @api.doc(security='apikey')
    @token_required
    def get(self):

        key = request.headers['X-API-KEY']

        user = User.read_by_key(key)

        events = user.events
        
        result = list()

        for e in events:

            event = e.__dict__
            event["date"] = event["date"].isoformat()
            del event['_sa_instance_state']

            result.append(event)

        return result

    @api.doc(security='apikey')
    @token_required
    @ns.expect(event_model)
    def post(self):

        payload = api.payload

        payload["date"] = datetime.datetime.now()

        event = Event(**payload)

        key = request.headers['X-API-KEY']

        user = User.read_by_key(key)

        user.add_event(event)

        event = event.to_dict()
        
        return event, status.HTTP_201_CREATED

@ns.route('/<int:event_id>')
class EventResource(Resource):

    @api.doc(security='apikey')
    @token_required
    def get(self, event_id):

        event = Event.read_event(event_id)

        event = event.to_dict()
        
        return event

    @api.doc(security='apikey')
    @token_required
    def delete(self, event_id):

        key = request.headers['X-API-KEY']

        user = User.read_by_key(key)

        if not user.owns_event(event_id):
            return "Not your event", status.HTTP_401_UNAUTHORIZED

        user.delete_event(event_id)

        return "Event deleted", status.HTTP_204_NO_CONTENT

    @api.doc(security='apikey')
    @token_required
    def put(self, event_id):

        key = request.headers['X-API-KEY']

        user = User.read_by_key(key)

        if not user.owns_event(event_id):
            return "Not your event", status.HTTP_401_UNAUTHORIZED

        payload = api.payload

        Event.update(event_id, payload)

        event = Event.read_event(event_id)

        event = event.to_dict()
        
        return event, status.HTTP_202_ACCEPTED
