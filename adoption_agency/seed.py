

"""Seed file to make sample data for db."""




from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()




Pet.query.delete()


sherry = Pet(name='Sherry', species='Dog', photo_url='https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2018/08/golden-retriever-detail.jpg?bust=1535565857&width=355', age=3, notes="Playful, loving, and a mans best friend!", available=True)
spot = Pet (name='Spot', species='Cat', age=2, notes="Just a beaut!", available=True)
sleepy = Pet (name='Sleepy', species='Porcupine', age=6, notes="What more could you want in a dog.", available=False)




db.session.add_all([sherry, spot, sleepy])
db.session.commit()

