from flask import request, jsonify, make_response
from app import db, app
from marshmallow import fields
from flask_marshmallow import Marshmallow
from app.models import UserDetail
ma = Marshmallow(app)
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class UserDetailSchema(SQLAlchemyAutoSchema):
   class Meta:
       model = UserDetail
       sqla_session = db.session
       load_instance = True

   id = fields.Number(dump_only=True)
   first_name = fields.Str(required=True)
   last_name = fields.Str(required=False)
   age = fields.Integer(required=True)
   email = fields.Email(required=True)


@app.route('/add', methods=['POST'])
def create_user():
   data = request.get_json()
   user_schema = UserDetailSchema()
   user = user_schema.load(data)
   result = user_schema.dump(user.create())
   return make_response(jsonify({"data": result}), 200)


@app.route('/list', methods=['GET'])
def list():
   get_user = UserDetail.query.all()
   user_schema = UserDetailSchema(many=True)
   list = user_schema.dump(get_user)
   return make_response(jsonify({"data": list}))



@app.route('/user/<id>', methods=['GET'])
def get_user_by_id(id):
   get_user = UserDetail.query.get(id)
   user_schema = UserDetailSchema()
   list = user_schema.dump(get_user)
   return make_response(jsonify({"data": list}))

@app.route('/user/<id>', methods=['PUT'])
def update_user_by_id(id):
   data = request.get_json()
   get_user = UserDetail.query.get(id)
   if data.get('first_name'):
       get_user.first_name = data['first_name']
   if data.get('last_name'):
       get_user.last_name = data['last_name']
   if data.get('age'):
       get_user.age = data['age']
   if data.get('email'):
       get_user.email = data['email']
   db.session.add(get_user)
   db.session.commit()
   user_schema = UserDetailSchema(only=['id', 'first_name', 'last_name','age','email'])
   user = user_schema.dump(get_user)
   return make_response(jsonify({"data": user}))


@app.route('/user/<id>', methods=['DELETE'])
def delete_user_by_id(id):
   get_user = UserDetail.query.get(id)
   db.session.delete(get_user)
   db.session.commit()
   return make_response("", 204)
