from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://cf-python:beren@localhost/task_database")

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


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
        return "<Recipe ID: " + str(self.id) + "-" + self.name + " (Difficulty: " + self.difficulty + ")>"


    def __str__(self):
        recipe_str = (
            f"\n{'-'*40}\n"
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}\n"
            f"{'-'*40}\n"
        )
        return recipe_str
    

    def calculate_difficulty(self):
        ingredient_count = len(self.ingredients.split(', '))
        
        if self.cooking_time < 10 and ingredient_count < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and ingredient_count >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredient_count < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and ingredient_count >= 4:
            self.difficulty = "Hard"
        else:
            self.difficulty = "Difficulty Unknown"


    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        else:
            return self.ingredients.split(', ')
    

    Base.metadata.create_all(engine)

def main():
    print('todo')    


if __name__ == '__main__':
    main()