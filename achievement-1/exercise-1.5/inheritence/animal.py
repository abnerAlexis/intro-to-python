class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name
    
    def __str__(self):
        output = f"\nClass: Animal\nName: {self.name}\nAge: {self.age}"
        return output
    
class Cat(Animal):
    def speak(self):
        print('Meowwwww!')

    def __str__(self):
        output = f"\nClass: Cat\nName: {self.name}\nAge: {self.age}"
        return output

class Dog(Animal):
    def speak(self):
        print('Woffffff!')

    def __str__(self):
        output = f"\nClass: Dog\nName: {self.name}\nAge: {self.age}"
        return output

class Human(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age) # Initialize Animal class first like so. Then set name.
        self.set_name(name)
        # new attribute for humans, 'friends'!
        self.friends = []

    # add friends
    def add_friend(self, friend_name):
        self.friends.append(friend_name)  

    # display friends 
    def display_friends(self):
        for friend in self.friends:
            print(friend)

    def speak(self):
        print(f"Hello, my name is {self.name}!")

    def __str__(self):
        output = f"\nClass: Human\nName: {self.name}\nAge: {self.age}\nFriends:\n" 
        for friend in self.friends:
            output += f"{friend}\n"
        return output

def main():
    a = Animal(5)
    print(a)
    a.set_name('Rufus')
    print(a)

    c = Cat(2)
    print(c)
    c.set_name('Missy')
    print(c)
    c.speak()

    d = Dog(4)
    d.set_name('Teddy')
    print(d)
    d.speak()

    h = Human('Alexis', 18)
    h.add_friend('Jennifer')
    h.add_friend('Lucy')
    h.add_friend('Carmen')
    h.add_friend('Elizabeth')
    h.add_friend('Milly')
    h.add_friend('Brooke')
    h.add_friend('Sue')
    h.add_friend('Jessica')
    h.add_friend('Holly')
    h.add_friend('Francine')
    h.add_friend('Leila')
    h.add_friend('Marry')
    h.add_friend('Tom')
    h.add_friend('Natalie')
    h.add_friend('Allison')
    print(h)

if __name__ == '__main__':
    main()