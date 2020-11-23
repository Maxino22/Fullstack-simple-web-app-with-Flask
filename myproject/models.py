from myproject import db


class InfoTAble(db.Model):

    __tablename__ = 'Messages'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Text(35))

    message = db.Column('Message', db.String(500))

    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __repr__(self):
        return f"{self.id} {self.name}  {self.message}"
