# encoding: utf-8

# app/api/events.py

import datetime

from flask import request
from flask_restplus import Namespace, Resource, fields
from playhouse.shortcuts import model_to_dict

from app.extensions.api import api
from app.extensions import status
from app.modules.auth import User
from app.modules.api.utils import token_required

from .models import ToDo

ns = Namespace('todos', description='Namespace for todos')

todo_model = api.model("todo_model", {
    'task': fields.String(required=True, description='Task')
})


@ns.route('/')
class TodoCollectionResource(Resource):
    
    @api.doc(security='apikey')
    @token_required
    def get(self):

        key = request.headers['X-API-KEY']

        user = User.read_by_key(key)

        todos = user.todos

        print(todos)

        result = list()

        for t in todos:

            todo = t.__dict__
            del todo['_sa_instance_state']

            result.append(todo)

        return result

    @api.doc(security='apikey')
    @token_required
    @ns.expect(todo_model)
    def post(self):

        payload = api.payload

        todo = ToDo.create(**payload)

        key = request.headers['X-API-KEY']

        user = User.read_by_key(key)

        user.add_todo(todo)

        todo = todo.__dict__
        del todo['_sa_instance_state']
        
        return todo, status.HTTP_201_CREATED

@ns.route('/<int:todo_id>')
class TodoResource(Resource):

    @api.doc(security='apikey')
    @token_required
    def get(self, todo_id):

        todo = ToDo.read_todo(todo_id)

        todo = todo.__dict__
        del todo['_sa_instance_state']
        
        return todo

    @api.doc(security='apikey')
    @token_required
    def delete(self, todo_id):

        key = request.headers['X-API-KEY']

        user = User.read_by_key(key)

        if not user.owns_todo(todo_id):
            return "Not your todo", status.HTTP_401_UNAUTHORIZED

        todo = ToDo.delete(todo_id)

        return "Todo deleted", status.HTTP_204_NO_CONTENT

    @api.doc(security='apikey')
    @token_required
    def put(self, todo_id):

        key = request.headers['X-API-KEY']

        user = User.read_by_key(key)

        if not user.owns_todo(todo_id):
            return "Not your todo", status.HTTP_401_UNAUTHORIZED

        payload = api.paylaod

        ToDo.update(payload)

        todo = ToDo.read_event(todo_id)

        todo = todo.__dict__
        del todo['_sa_instance_state']
        
        return todo, status.HTTP_202_ACCEPTED
