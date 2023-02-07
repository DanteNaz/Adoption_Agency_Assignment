



from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPet, EditPet



app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///agency_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "Naz"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)





@app.route('/')
def home_page():
    
    display = Pet.query.all()
    
    return render_template('home.html', display=display)







@app.route("/add_pet", methods=["GET", "POST"])
def add_pet(): 

    form = AddPet()                                          


    if form.validate_on_submit():                                     
        
        name = form.name.data                                          
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)   
        db.session.add(pet)                                                 
        db.session.commit()                                           
        return redirect('/')                                    
    
    else:    
        return render_template('add_pet_form.html', form=form)   









@app.route('/<int:id>/details', methods=['GET'])
def view_pet(id):
    
    pet = Pet.query.get_or_404(id)
    
    return render_template("pet_details.html", pet=pet)










@app.route('/edit/<int:id>/details', methods=['GET', 'POST'])
def edit_employee(id):
    
    pet = Pet.query.get_or_404(id)
    form = EditPet(obj=pet)                                          
    
    # depts = db.session.query(Department.dept_code, Department.dept_name)  
    # form.dept_code.choices = depts
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data       
        db.session.commit()
        return redirect(f'/{id}/details')
    
    else:
        return render_template("edit_details_form.html", form=form)






