class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f"{self.feet}feet {self.inches}inch/es"    
    
    def __add__(self, other):
        sum_feet = self.feet + other.feet
        sum_inches = self.inches + other.inches
        if (sum_inches >= 12):
            sum_feet += 1
            sum_inches = sum_inches % 12
        else:
            sum_inches = sum_inches
        return f"Sum of {self} and {other}: {sum_feet} feet {sum_inches} inches"
    
    def __sub__(self, other):
        self_in_inches = self.feet * 12
        other_in_inches = other.feet * 12
        self_height = self_in_inches + self.inches
        other_height = other_in_inches + other.inches
        height_difference = 0
        if (self_height > other_height):
            height_difference = self_height - other_height
        else:
            height_difference = other_height - self_height
        subtracked_dif = f"{height_difference // 12} feet {height_difference % 12}"
        return subtracked_dif
    
def main():
    Adam = Height(5, 10)
    print("Adam's Height:", Adam)
    Harry = Height(3, 9)
    print("Harry's Height:", Harry)

    print(Adam + Harry)
    print(Adam - Harry)

if __name__ == '__main__':
    main()