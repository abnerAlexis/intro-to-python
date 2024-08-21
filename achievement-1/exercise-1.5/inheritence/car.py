class Car:
    id = 0
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.id = Car.id
        Car.id += 1

    def __str__(self) -> str:
        output = f"\nID: {self.id}\nName: {self.name}\nModel: {self.year}"
        return output
    
def main():
    c0 = Car('Toyota', 'RAV4', '2024')
    c1 = Car("Toyota", "Corolla", "2012")
    c2 = Car("BMW", "Z3", "2001")
    c3 = Car("Audi", "A6", "2020")
    print(f"\n{c0}\n{c1}\n{c2}\n{c3}")

if __name__ == '__main__':
    main()