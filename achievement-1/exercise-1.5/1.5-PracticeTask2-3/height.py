class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f"{self.feet} feet {self.inches} inch/es"    
    
    def __add__(self, other):
        sum_feet = self.feet + other.feet
        sum_inches = self.inches + other.inches
        if (sum_inches >= 12):
            sum_feet += 1
            sum_inches = sum_inches % 12
        else:
            sum_inches = sum_inches
        return f"Sum of {self} and {other}: {sum_feet} feet {sum_inches} inches"
    
    def __lt__(self, other):
        return (self.feet * 12) + self.inches < (other.feet * 12 + other.inches)
    
    def __le__(self, other):
        return (self.feet * 12) + self.inches <= (other.feet * 12 + other.inches)
    
    def __eq__(self, other):
        return (self.feet * 12) + self.inches == (other.feet * 12 + other.inches)
    
    def __gt__(self, other):
        return (self.feet * 12) + self.inches > (other.feet * 12 + other.inches)
    
    def __ge__(self, other):
        return (self.feet * 12) + self.inches >= (other.feet * 12 + other.inches)
    
    def __ne__(self, other):
        return (self.feet * 12) + self.inches != (other.feet * 12 + other.inches)
    
    def __sub__(self, other):
        difference_in_inches = (self.feet * 12 + self.inches) - (other.feet * 12 + other.inches)
        feet = difference_in_inches // 12
        inches = difference_in_inches % 12
        return f"{feet} feet {inches} inches"
    
def main():
    Adam = Height(5, 10)
    print("Adam's Height:", Adam)
    Harry = Height(3, 9)
    print("Harry's Height:", Harry)

    print("Adam's height + Harries height", Adam + Harry)
    print("Adam's height - Harries height", Adam - Harry)

    print("Is Adam's height less than Harries height? ", Adam < Harry)

    print("Is 5 feet 9 inches less than 6 feet 2 inches", Height(5, 9) < Height(6, 2))
    print("Is 5 feet 9 inches less than or equal to 6 feet 2 inches", Height(5, 9) <= Height(6, 2))
    print("Is 5 feet 9 inches not equal to 6 feet 2 inches", Height(5, 9) != Height(6, 2))
    print("Is 6 feet 2 inches equal to 6 feet 2 inches", Height(4, 5) == Height(4, 5))
    print("Harry", Harry)
    print('==============================================================================================')

    a = Height(4, 10)
    b = Height(5, 6)
    c = Height(7, 1)
    d = Height(5, 5)
    e = Height(6, 7)
    f = Height(5, 6)

    heights = [a, b, c, d, e, f]

    heights = sorted(heights)
    print("List of heights (Ascending):")
    for height in heights:
        print(height)
    print("Reversed list of heights (Descending):")
    heights = sorted(heights, reverse = True)
    for height in heights:
        print(height)

if __name__ == '__main__':
    main()