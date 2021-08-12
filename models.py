from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

"""Models for Cupcake app."""

class Cupcake(db.Model):
    """Cupcake Model"""

    __tablename__= "cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)

    # Serialization. Instance method of converting a single Todo into a dictionary representation.
    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

    def __repr__(self):
        return f"<Cupcake {self.id} flavor={self.flavor} size={self.size} rating={self.rating} image={self.image}>"