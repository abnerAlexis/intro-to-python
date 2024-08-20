class Date(object):
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def get_date(self):
        date = str(self.month) + '/' + str(self.day) + '/' + str(self.year)
        return date
    
    def set_date(self):
        self.month = int(input('Month: '))
        self.day = int(input('Day: '))
        self.year = int(input('Year: '))

    def is_leap_yer(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    def is_valid_date(self):
        if not (type(self.month) == int and type(self.day) == int and type(self.year) == int):
            return False
        if (self.year < 0):
            return False
        if (self.month < 1 or self.month > 12):
            return False
        
        last_dates = {
            1 : 31,
            2 : 29 if self.is_leap_yer() else 28,
            3 : 31,
            4 : 30,
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
            10 : 31,
            11 : 30,
            12 : 31,
        }

        if self.day < 1 or self.day > last_dates[self.month]:
            return False
        
        return True

def main():
    # first_moon_landing = Date(7, 20, 1969)
    # print('Date of first moon landing:', first_moon_landing.get_date())

    # first_moon_landing.set_date()
    # print('Date of first moon landing:', first_moon_landing.get_date())

    date1 = Date(2, 29, 2000)
    date2 = Date(2, 29, 2001)
    date3 = Date('fjk', 'eio', 'vdyf')
    date4 = Date(6, 25, 1990)
    print(date1.get_date() + ' : ' + str(date1.is_valid_date()))
    print(date2.get_date() + ' : ' + str(date2.is_valid_date()))
    print(date3.get_date() + ' : ' + str(date3.is_valid_date()))
    print(date4.get_date() + ' : ' + str(date4.is_valid_date()))


if __name__ == "__main__":
    main()