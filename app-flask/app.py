from flask import Flask, render_template
from datetime import datetime,timedelta
from alchemyClasses import db
from contollers.ControllerStartup import startup_blueprint
from contollers.ControllerTechnologie import technologie_blueprint
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://becario:BecarioCIID24@localhost:3306/CIID'
app.config.from_mapping(
    SECRET_KEY='dev'
)

db.init_app(app)
app.register_blueprint(startup_blueprint)
app.register_blueprint(technologie_blueprint)



if __name__ == '__main__':
    app.run(port=5000)   

    
