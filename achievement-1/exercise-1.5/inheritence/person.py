class Person:
    def walk():
        print('Hello, I can walk!')



class Athlete(Person):
    def run():
        print('I can run too!')



def main():
    print('Person says:')
    Person.walk()

    print('Athlete says:')
    Athlete.walk()
    Athlete.run()

if __name__ == '__main__':
    main()