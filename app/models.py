

from app.routes import db

# Model
class UserDetail(db.Model):
   __tablename__ = "UserDetail"
   id = db.Column(db.Integer, primary_key=True)
   first_name = db.Column(db.String(120), index=True, nullable=False)
   last_name = db.Column(db.String(120), index=True, nullable=True)
   age = db.Column(db.Integer, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)

   def create(self):
       db.session.add(self)
       db.session.commit()
       return self

   def __init__(self, first_name, last_name,age,email):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.email = email

   def __repr__(self):
       return f"{self.id}"

# db.create_all()


