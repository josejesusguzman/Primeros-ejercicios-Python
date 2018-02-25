import os
from datetime import date

password = input("Write the password\n")
loop = 'yes'
artists =['Antoine Griezman', 'Messi', 'Pikachu', 'Kamisama', 'Peña bb']

if password == 'Making Mexico':
    while loop == 'yes' or loop == 'Yes':
        Year = int(input("year of birth: " ))
        Month = input("month of birth: " ).lower()
        Day = int(input("day of birth: " ))
        Date_of_Birth = (str(Day) + "/" + Month + "/" + str(Year))
        d = date.today()
        y = d.year
        
        age = y - Year
        print('Your Date of Birth is ' + Date_of_Birth)
        print ('This year you gonna be ' + str(age) + ' years old')

        if ((Month == 'december' and Day >= 22) or (Month == 'january' and Day<= 19)):
            print("\n Capricorn")
            for name in artists:
                print(name)

        elif ((Month == 'january' and Day >= 20) or (Month == 'february' and Day<= 17)):
            print("\n Aquarium")
            for name in artists:
                print(name)

        elif ((Month == 'february' and Day >= 18) or (Month == 'march' and Day<= 19)):
            print("\n Pices")
            for name in artists:
                print(name)

        elif ((Month == 'march' and Day >= 20) or (Month == 'april' and Day<= 19)):
            print("\n Aries")
            for name in artists:
                print(name)

        elif ((Month == 'april' and Day >= 20) or (Month == 'may' and Day<= 20)):
            print("\n Taurus")
            for name in artists:
                print(name)

        elif ((Month == 'may' and Day >= 21) or (Month == 'june' and Day<= 20)):
            print("\n Gemini")
            for name in artists:
                print(name)

        elif ((Month == 'june' and Day >= 21) or (Month == 'july' and Day<= 22)):
            print("\n Cancer")
            for name in artists:
                print(name)

        elif ((Month == 'july' and Day >= 23) or (Month == 'august' and Day<= 22)): 
            print("\n Leo")
            for name in artists:
                print(name)

        elif ((Month == 'august' and Day >= 23) or (Month == 'september' and Day<= 22)): 
            print("\n Virgo")
            for name in artists:
                print(name)

        elif ((Month == 'september' and Day >= 23) or (Month == 'october' and Day<= 22)):
            print("\n Libra")
            for name in artists:
                print(name)

        elif ((Month == 'october' and Day >= 23) or (Month == 'november' and Day<= 21)): 
            print("\n Scorpio")
            for name in artists:
                print(name)

        elif ((Month == 'november' and Day >= 22) or (Month == 'december' and Day<= 21)):
            print("\n Sagittarius as:\n")
            for name in artists:
                print(name)

        loop = input('Do you want to prove it again?')
        

    else:
        print ('Goodbye! :D')

else:
    print ('Sorry wrong password')
