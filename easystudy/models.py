from easystudy import db,bcrypt,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#class User(db.Model):
#    id: Mapped[int] = mapped_column(Integer, primary_key=True)
#    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
#    age: Mapped[int] = mapped_column(Integer, nullable=False)
#    email: Mapped[str] = mapped_column(String)
#    Gender: Mapped[str] = mapped_column(String)
#    Password: Mapped[str] = mapped_column(String)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)  # Set size to 20
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String)
    gender = db.Column(db.String)
    password = db.Column(db.String)
    profile_pic = db.Column(db.String(15) , nullable=False , default='profile.jpeg')
    posts= db.relationship("Post", backref='author', lazy=True)

    def __repr__(self):
        return f"user is {self.name} and I am {self.age} years old."



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)  # Set size to 20
    content = db.Column(db.String(2000), nullable=False)
    date = db.Column(db.String(120), nullable=False)
    #author = db.Column(db.Integr, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"title is {self.title} and content is {self.content} years old."


users = [
    {"name": "User1", "email": "user1@example.com", "age": 25},
    {"name": "User2", "email": "user2@example.com", "age": 30},
    {"name": "User3", "age": 35},
    {"name": "User4", "email": "user4@example.com", "age": 40}
]



def add_user(form):
    name = form.name.data
    age = form.age.data
    email = form.email.data
    gender = form.gender.data
    hashed_pwd = bcrypt.generate_password_hash(form.password.data)

    #db.create_all()
    user1=User(name=name,age=age,email=email,gender=gender,password=hashed_pwd)
    db.session.add(user1)
    db.session.commit()
