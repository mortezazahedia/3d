from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '567ABCcde'
# db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app_database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)
# migrate = Migrate(app, db)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#name of the method
login_manager.login_view = "login"
login_manager.login_message = u"Please login!!!"
login_manager.login_message_category = "warning"

#with app.app_context():
    # Create the User table
    #db.drop_all()
    #db.create_all()
    #migrate.init_app(app, db)
    #db.session.add(User(name='morteza zahedi', age=41, email='aaa@gmail.com', Gender='Men', Password='12345'))
    #db.session.add(User(name='reza zahedi', age=31, email='b@gmail.com', Gender='Both', Password='125655'))
    #db.session.add(User(name='reyhane zahedi', age=21, email='ff@gmail.com', Gender='Men', Password='1545'))
    #db.session.add(User(name='shab zahedi', age=11, email='ee@gmail.com', Gender='Men', Password='14445'))
    #db.session.add(User(name='mard zahedi', age=51, email='dd@gmail.com', Gender='Men', Password='11125'))
    #db.session.add(User(name='baran zahedi', age=11, email='ee@gmail.com', Gender='Men', Password='14445'))
    #db.session.add(User(name='rozbeh zahedi', age=51, email='dd@gmail.com', Gender='Men', Password='11125'))
    #db.session.add(User(name='roz zahedi', age=51, email='dd@gmail.com', Gender='Men', Password='11125'))
    #db.session.commit()

    #print("DB Created")

from easystudy import routes