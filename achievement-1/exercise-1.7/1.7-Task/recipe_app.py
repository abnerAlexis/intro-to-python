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
        return (
            "<Recipe ID: "
            + str(self.id)
            + "-"
            + self.name
            + " (Difficulty: "
            + self.difficulty
            + ")>"
        )

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
        ingredient_count = len(self.ingredients.split(", "))

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
            return self.ingredients.split(", ")

    Base.metadata.create_all(engine)
    

    def create_recipe(self):
        # Collect the recipe name
        name = self.prompt_recipe_name()

        # Collect the cooking time
        cooking_time = self.prompt_cooking_time()

        # Collect the ingredients
        ingredients = self.promt_ingredients()

        # Create the new Recipe object
        recipe_entry = Recipe(
            name=name, ingredients=ingredients, cooking_time=cooking_time
        )

        # Calculate the difficulty
        recipe_entry.calculate_difficulty()

        # Add the recipe to the database
        try:
            session.add(recipe_entry)
            session.commit()
            print("Recipe added successfully!")
            print("Recipe Details:")
            print(recipe_entry)
        except Exception as e:
            session.rollback()
            print("An error occurred:", e)



    def prompt_recipe_name(self):
        while True:
            name = input("Enter the recipe name (max 50 characters): ")
            if len(name) > 50:
                print("Error: Name cannot exceed 50 characters.")
            elif not name.isalnum():
                print("Error: Name must be alphanumeric.")
            elif not name:
                print("Error: Recipe name cannot be empty.")
            else:
                break
        return self.name
    
    
    def prompt_cooking_time(self):
        while True:
            cooking_time = input("Enter the cooking time (in minutes): ")
            if not cooking_time.isnumeric():
                print("Error: Cooking time must be a number.")
            elif int(cooking_time) <= 0:
                print("Error: Cooking time must be a positive integer.")
            else:
                cooking_time = int(cooking_time)
                break


    def prompt_ingredients():
        ingredients = []
        while True:
            ingredient = input("Enter an ingredient (or press Enter to finish): ")
            if ingredient:
                ingredients.append(ingredient)
            else:
                break

        # Convert the ingredients list to a string and return
        return  ", ".join(ingredients)


def main():
    print("todo")


if __name__ == "__main__":
    main()
