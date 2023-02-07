

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, choices
from wtforms.validators import InputRequired, Email, Optional






class AddPet(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired(message="Name Required")])
    species = SelectField("Species", choices= [('cat','Cat'),('dog','Dog'),('porc', 'Porcupine')])
    photo_url = StringField("Image of Your Pet")                                                
    age = IntegerField("Age", validators=[Optional()])                                                
    notes = StringField("Notes on Your Pet")                                                                                              






class EditPet(FlaskForm):

    photo_url = StringField("Image of Your Pet")                                    
    notes = StringField("Notes on Your Pet")                                                                                              
    available = BooleanField("Is Pet Available?")


