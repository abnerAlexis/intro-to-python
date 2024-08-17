def display(file):
    heroes = []
    for line in file:
        # Remove new line chars
        line = line.rstrip('\n')

        # Split the line into hero name and first appearance
        hero_name = line.split(', ')[0]
        first_appearance = line.split(', ')[1]

        # Append hero_name and first_appearance into a list of tuples
        heroes.append((hero_name, int(first_appearance)))

    # Sorting heroes by their first_appearance/year
    heroes.sort(key=lambda hero: hero[1])

    # Print the sorted list of heroes
    for hero in heroes:
        print("--------------------------------------")
        print('Superhero:', hero[0])
        print('First year of appearance:', hero[1])

filename = input("Enter the filename where you've stored the heroes:")

try:
    with open(filename, 'r') as file:
        display(file)
except FileNotFoundError:
    print('File not found.')
except Exception as error:
    print(f"An unexpected error occurred: {error}")
finally: 
    print('Done!')