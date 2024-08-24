from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://cf-python:beren@localhost/task_database")

Base = declarative_base()

class Recipe(Base):
    # Recipe (what can also be called a data model or a model), stores the representation 
    # of the table’s structure in the db.
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    

    Base.metadata.create_all(engine)


def main():
    print('todo')    


if __name__ == '__main__':
    main()