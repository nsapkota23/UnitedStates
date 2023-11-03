"""This program takes a state capital population and state
flower and manipulates the data in different ways"""

import matplotlib.pyplot as plt

# List with all the state information
united_states_data = [
    ["Alabama", "Montgomery", 5097641, "Camellia"],
    ["Alaska", "Juneau", 740339, "Alpine Forget-me-not"],
    ["Arizona", "Phoenix", 7379346, "Saguaro Cactus Blossom"],
    ["Arkansas", "Little Rock", 3040207, "Apple Blossom"],
    ["California", "Sacramento", 40223504, "California Poppy"],
    ["Colorado", "Denver", 5997070, "Rocky Mountain Columbine"],
    ["Connecticut", "Hartford", 3615499, "Mountain Laurel"],
    ["Delaware", "Dover", 1017551, "Peach Blossom"],
    ["Florida", "Tallahassee", 22359251, "Orange Blossom"],
    ["Georgia", "Atlanta", 11019186, "Cherokee Rose"],
    ["Hawaii", "Honolulu", 1483762, "Pua Aloalo"],
    ["Idaho", "Boise", 1920562, "Syringa"],
    ["Illinois", "Springfield", 12807072, "Violet"],
    ["Indiana", "Indianapolis", 6876047, "Peony"],
    ["Iowa", "Des Moines", 3233572, "Wild Rose"],
    ["Kansas", "Topeka", 2963308, "Sunflower"],
    ["Kentucky", "Frankfort", 4555777, "Goldenrod"],
    ["Louisiana", "Baton Rouge", 4695071, "Iris"],
    ["Maine", "Augusta", 1372559, "White Pine Cone and Tassel"],
    ["Maryland", "Annapolis", 6298325, "Black-eyed Susan"],
    ["Massachusetts", "Boston", 7174604, "Mayflower"],
    ["Michigan", "Lansing", 10135438, "Apple Blossom"],
    ["Minnesota", "St. Paul", 5827265, "Pink and White Lady's Slipper"],
    ["Mississippi", "Jackson", 2959473, "Magnolia"],
    ["Missouri", "Jefferson City", 6204710, "White Hawthorn Blossom"],
    ["Montana", "Helena", 1112668, "Bitterroot"],
    ["Nebraska", "Lincoln", 2002052, "Goldenrod"],
    ["Nevada", "Carson City", 3225832, "Sagebrush"],
    ["New Hampshire", "Concord", 1395847, "Purple Lilac"],
    ["New Jersey", "Trenton", 9438124, "Purple Violet"],
    ["New Mexico", "Santa Fe", 2135024, "Yucca Flower"],
    ["New York", "Albany", 20448194, "Rose"],
    ["North Carolina", "Raleigh", 10710558, "Carolina Lily"],
    ["North Dakota", "Bismarck", 811044, "Wild Prairie Rose"],
    ["Ohio", "Columbus", 11878330, "Red Carnation"],
    ["Oklahoma", "Oklahoma City", 4021753, "Oklahoma Rose"],
    ["Oregon", "Salem", 4359110, "Oregon Grape"],
    ["Pennsylvania", "Harrisburg", 13092796, "Mountain Laurel"],
    ["Rhode Island", "Providence", 1110822, "Violet"],
    ["South Carolina", "Columbia", 5266343, "Yellow Jessamine"],
    ["South Dakota", "Pierre", 908414, "American Pasque"],
    ["Tennessee", "Nashville", 7080262, "Iris"],
    ["Texas", "Austin", 30345487, "Bluebonnet"],
    ["Utah", "Salt Lake City", 3423935, "Sego Lily"],
    ["Vermont", "Montpelier", 648279, "Red Clover"],
    ["Virginia", "Richmond", 8820504, "American Dogwood"],
    ["Washington", "Olympia", 7999503, "Coast Rhododendron"],
    ["West Virginia", "Charleston", 1775932, "Rhododendron"],
    ["Wisconsin", "Madison", 5955737, "Wood Violet"],
    ["Wyoming", "Cheyenne", 580817, "Indian Paintbrush"]
]


def print_states():
    """this function will sort the states and print them alphabetically"""
    alphabetical_states = sorted(united_states_data)
    sorted_states = [print(i) for i in alphabetical_states]
    print(sorted_states)


def search_states():
    """This function searches a certain state and prints the values and
    also shows a picture of the state flower"""
    state_search = input("Enter what state you want to search for: ")

    for i in united_states_data:
        if i[0] == state_search:
            print(f"State: {i[0]}\nCapital: {i[1]}\nPopulation: {i[2]}\nFlower: {i[3]}")

            flower_pic = plt.imread("/Users/neonsapkota/Desktop/" + i[3] + ".png")
            plt.imshow(flower_pic)
            plt.show()


def population_graph():
    """This function will sort the population data and save them and then use the
    state and population as x and y variables in a bar graph"""
    sorted_states_data = sorted(united_states_data, key=lambda x: x[2], reverse=True)

    state_name = []
    for state in sorted_states_data[:5]:
        state_name.append(state[0])
    highest_population = []
    for state in sorted_states_data[:5]:
        highest_population.append(state[2])

    plt.bar(state_name, highest_population)

    # labels the x and y axis
    plt.ylabel('Population')
    plt.xlabel('State')

    plt.show()


def update_population():
    """This function will update a state of choice to a new population"""
    state_search = input("Enter what state you want update population for: ")
    new_population = input("Enter what the new population is: ")

    for state in united_states_data:
        if state[0] == state_search:
            state[2] = new_population
            print("The new population for " + state_search + " is " + new_population)




def main():
    """This main creates the User interface and calls the other functions"""
    print("This is a United States data program select an option to begin")

    while True:
        print("1. Show states in alphabetical order \n2. Search for a specific state\n"
              "3. Show a graph of the 5 most populous states \n"
              "4.""Update the population of a state\n5.Exit")

        selection = int(input("Pick a selection"))

        if selection == 1:
            print_states()
        if selection == 2:
            search_states()
        if selection == 3:
            population_graph()
        if selection == 4:
            update_population()
        if selection == 5:
            break

        print("Error! Invalid input")

    print("Thank you for using the program")


main()
