#*******************************************************************************
# Author:      Natalie Moss
# Date:        March 17, 2025
# Description: This program takes a distance measured in either imperial inches
#              or imperial feet (which is based on the actual length of King
#              Henry I's foot) and returns the distance measured in the new unit,
#              the "nefeet" (based on the length of Queen Nefertiti's foot). The
#              program also takes the user's age for the output message and asks
#              if the user would like to convert another measurement to nefeet.
#              The program uses a while loop to ask the user if they want to
#              input another measurement to convert to nefeet. Once the user
#              is done, the program asks the user if they would like to create
#              a unit of measurement based on their own foot length and what
#              they would like to call it. A statement prints out giving the
#              conversion factor of their custom named unit of measurement.
#              The program uses a class Thingy to construct objects
#              with the fields _description and _length_nefeet, rather than
#              storing these attributes in separate lists.
# Input:       Description of the distance measured, choice of imperial inches
#              or imperial feet, the distance in the chosen unit, and the
#              user's age. A second input prompt asks the user if they want
#              to create a unit of measurement based on their own foot and what
#              they wish to call it. User input is validated using validation
#              functions. The program accepts all version of y/n inputs, variat-
#              ions on foot and inch spellings (In, INCHES, ft, etc), requires
#              that age is an integer between 0 and 120, accepts only positive
#              numbers for distance inputs.
# Output:      The user's chosen distance measurement converted from imperial to
#              nefeets along with their age when they learned this and the opt-
#              ion to perform another conversion. The second output, if the user
#              wants to create their own unit of measurement is the conversion
#              factor for converting decimal imperial feet to their unit.
# Sources:     Portland Community College CIS122 course instructions,
#              AI Assistant for debugging.
#*******************************************************************************
# SAMPLE RUN
#
# Welcome to "The Foot Distance Rematriation Calculator"!
#
# Did you know that the foot as an imperial unit of measure was based on the
# actual foot length of King Henry the I? Imagine a world where a standard unit
# of measure was based on a woman's body instead. The Measurement Rematriation
# Committee (MRC) determined that Queen Nefertiti's foot size is the new
# standard. It is called the nefeet. And now YOU can begin to re-measure your
# world accordingly.
#
# Please note the MRC has adopted the decimal nefeet rather than pursue the
# folly of inches. What even *was* King Henry's "inch" if the foot was his
# foot???
#
# Let's start off by putting things in perspective. What year were you born? 1976
# Wow, Queen Nefertiti was born 3,346 years before you were born and 2,438 years
# before King Hnery I was born. Okay, now that we are sufficiently humbled, let's
# get to converting some measurements.

# Description of length you are converting to nefeet: hot dog
# You can choose to enter either imperial decimal inches or imperial decimal
# feet. Please enter 'inches' or 'feet': In
# Length in imperial decimal inches: 5.7
#
#
# I was 48 years old when I learned that the measurement 'hot dog'
# is  0.692 nefeet.
# Would you like to convert another measurement to nefeet? Please enver 'yes'
# or 'no': yes
# Description of the length you are converting to nefeet: banana
# You can choose to enter either imperial decimal inches or imperial decimal
# feet. Please enter 'inches' or 'feet': feet
#
# Length in imperial decimal feet: .65
#
# The measurement 'banana' is 0.947 nefeet.
# Would you like to convert another measurement to nefeet?
# Please enter 'yes' or 'no': no
#
# Would you like to entr your own foot length so you can create your own unit
# of measurement? Please enter 'yes' or 'no': yes
# Please enter your own foot length in decimal inches: 9.2
# What would you like to call your own unit of measurement? natfeet
# To remeasure your world in natfeet, multiply any length in imperial decimal
# feet by 1.304
#
# Thanks for measuring your world with a feminist ruler!

#*******************************************************************************
import valid as v

NEFERTITI = 1.207  # Nefertiti's foot is 9.94", so this is the constant for
                    # conversion: 12" / 9.94" = 1.207
NEFERTITI_BIRTH_YEAR = 1370 #Born in 1370 BCE

class Thingy:
    _description = ""
    _length_nefeet = 0.0

    def __init__(self, d, l):
        self._description = d
        self._length_nefeet = l

    def __str__(self):
        return "{: <20}{: <15}".format(self._description, self._length_nefeet)

    def get_description(self):
        return self._description

    def get_length_nefeet(self):
        return self._length_nefeet

    def set_description(self, d):
        self._description = d

    def set_length_nefeet(self, l):
        self._length_nefeet = l


def main():
    thingy_list = []    # list of Thingy objects, w/desc and length fields
    unit_choice = ""    # user's choice of decimal inch or decimal foot
    imp_dec_feet = 0.0  # input in decimal feet
    birth_year = 0      # the year the user was born
    year_difference = 0
    result = ""
    again = "yes"          # asks user if they want to calculate again

    print_welcome()

    # Input
    birth_year = ask_birth_year()

    # Calculation
    year_difference = calc_year_difference(birth_year, NEFERTITI_BIRTH_YEAR)

    # Output
    print_historical_perspective(year_difference)

    # Output
    while again == "yes":
            desc = ask_description()
            imp_dec_feet = get_unit_choice()
            length = calc_length_nefeet(imp_dec_feet)
            thingy_list.append(Thingy(desc, length))
            again = ask_again()

    print_result(thingy_list)


    # Input
    your_own = ask_own_measurement()
    if your_own == "yes":
            your_own_length = get_your_own_length()
            your_unit_name = get_own_unit_name()
            your_conversion = calc_your_conversion(your_own_length)
            print("To remeasure your world in ", your_unit_name, "multiply\n"
                   "any length in imperial decimal feet by ", your_conversion)

    print_goodbye()

def print_welcome():
    """
    Prints welcome message with information about the program.
    :return: None
    """
    print("""

    Welcome to The Foot Distance Rematriation Calculator!

    Did you know that the foot as an imperial unit of measure was based
    on the actual foot length of King Henry the I? Imagine a world where
    a standard unit of measure was based on a woman's body instead. The
    Measurement Rematriation Committee (MRC) determined that Queen 
    Nefertiti's foot size is the new standard. It is called the nefeet.
    And now YOU can begin to re-measure your world accordingly. 

    Please note the MRC has adopted the decimal nefeet rather than
    pursue the folly of inches. What even *was* King Henry's 'inch' if
    the foot was his foot???\n""")

def ask_birth_year():
    """
    Prompts user for the year they were born.
    :return: integer, the year the user was born.
    """
    birth_year = 0
    print("Let's start off by putting things in perspective.")
    while True:
        print("")
        birth_year = v.get_integer("What year were you born? ")
        return birth_year

def calc_year_difference(birth_year, NEFERTITI_BIRTH_YEAR):
    """Calculates the difference in years between the year the user
     was born and when Queen Nefertiti was born.
     return: integer, the difference in years"""
    year_difference = 0
    year_difference = (NEFERTITI_BIRTH_YEAR + birth_year)
    return year_difference

def print_historical_perspective(year_difference):
    """Uses the calculation of year difference in a fun fact for the
    user.
    return: none"""
    print(f"Wow, Queen Nefertiti was born {year_difference} years before you\n"
          f"were born and 2438 years before King Henry I was born. Okay, \n"
          f"now that we are sufficiently humbled, let's get to converting \n"
          f"some measurements.\n ")

def ask_description():
    """
    Prompts user for description of length they are converting to nefeet.
    :return: float, the description of length they are converting to nefeet.
    """
    description = ""
    description = input("Description of length you are converting to nefeet: ")
    return description

def get_unit_choice():
    """
    Prompts user for choice of decimal imperial inches or decimal imperial
    feet.
    return: float, imp_dec_feet
    """
    unit_choice = ""
    unit_choice = get_valid_unit()
    if unit_choice == "inches":
        imp_dec_feet = ask_imp_inches()
    elif unit_choice == "feet":
        imp_dec_feet = ask_imp_feet()
    else:
        print("Invalid unit choice.")
    return imp_dec_feet

def get_valid_unit():
    """
    Validates the user's input for the unit choice to accept various spellings
    of inches and feet.
    :param String, unit_choice
    :return: string, validated unit_choice or error message.
    """
    unit_choice = ""
    while True:
        unit_choice = input("You can choose to enter either "
                "imperial decimal inches or imperial decimal feet. Please "
                "enter 'inches' or 'feet': \n").lower()
        if unit_choice in ["inches", "inch", "in"]:
            return "inches"
        elif unit_choice in ["feet", "foot", "ft"]:
            return "feet"
        else:
            print("Invalid unit choice.")

def ask_imp_inches():
    """
    Prompts user for length measured in imperial decimal inches.
    :return: float, the length measured in imperial decimal inches.
    """
    imp_dec_feet = 0.0
    while True:
        imp_dec_inches = v.get_real("Length in imperial decimal inches: ")
        imp_dec_feet = (imp_dec_inches / 12.0)
        if imp_dec_feet < 0:
            print("Number must be positive.")
        else:
            return imp_dec_feet

def ask_imp_feet():
    """
    Prompts user for length measured in imperial decimal feet.
    :return: float, the length measured in imperial decimal feet.
    """
    imp_dec_feet = 0.0
    while True:
        imp_dec_feet = v.get_real("Length in imperial decimal feet: ")
        if imp_dec_feet < 0:
            print("Number must be positive.")
        else:
            return imp_dec_feet


def calc_length_nefeet(imp_dec_feet):
    """
    Calculates the length measured in nefeet.
    :param imp_dec_feet: float, the imperial length
    :return: float, the length measured in nefeet.
    """
    length_nefeet = []
    length_nefeet = (imp_dec_feet * NEFERTITI)
    length_nefeet = format(length_nefeet, '.3f')
    return length_nefeet

def print_result(thingy_list):
    """
    Prints the result of the calculation and goodbye message.
    :param description: string, what is being converted to nefeet.
    :param imp_dec_feet: float, the imperial length
    :param age: integer, user's age
    :param length_nefeet:float, result of conversion to nefeet
    :return: string, the result of the calculation and goodbye
             message.
    """
    print("\nYour Measurements in Nefeet\n")
    print("{: <20}{: <15}".format("Description", "Length in Nefeet"))
    print("{: <20}{: <15}".format("---------------", "---------------"))

    for t in thingy_list:
        print(t)

def ask_again():
    """
    Asks user if they would like to convert another measurement to nefeet.
    :return: string, the user's choice to convert another measurement
    """
    while True:
        again = v.get_y_or_n("\nWould you like to convert another measurement to nefeet? \n"
                  "Please enter 'yes' or 'no': ").lower()
        if again == "yes" or again == "y":
            return "yes"
        elif again == "no" or again == "n":
            return "no"

def print_other_result(description, length_nefeet):
    """
       Prints the result of the next  calculation.
       :param description: string, what is being converted to nefeet.
       :param imp_dec_feet: float, the imperial length
       :param length_nefeet:float, result of conversion to nefeet
       :return: string, the result of the calculation and goodbye
                message.
       """
    print("\nThe measurement '" + description + "' is " + str(length_nefeet) + " nefeet.")


def ask_own_measurement():
    """
    Asks the user if they would like to enter their own foot length in order
    to create a ruler based on their own foot length.
    :return: String, yes or no
    """
    your_own = ""
    your_own = v.get_y_or_n("\nWould you like to enter your own foot length so you\n"
                     "can create your own unit of measurement? \n"
                     "Please enter 'yes' or 'no': ")
    if your_own == "yes" or your_own == "y":
        return "yes"
    else:
        return "no"

def get_your_own_length():
    """
    Asks the user for their own foot length.
    :return: float, the user's foot length.
    """
    your_own_length = 0.0
    while True:
        your_own_length = v.get_real("Please enter your own foot length in decimal\n"
                                  "inches: ")
        if your_own_length < 0:
            print("Number must be positive.")
        else:
            return your_own_length

def get_own_unit_name():
    """
    Asks user what they would like to call their own unit of measurement.
    :return: string, the user's length unit name
    """
    your_unit_name = ""
    your_unit_name = input("What would you like to call your own\n"
                           "unit of measurement? ")
    return your_unit_name

def calc_your_conversion(your_own_length):
    """
    Calculates the user's foot length conversion factor.
    :param: float, the user's foot length.
    :return: float, the user's foot length conversion factor."""
    your_conversion = 0.0
    your_conversion = (12 / your_own_length)
    return format(your_conversion,'.3f')

def print_goodbye():
    """
    Prints goodbye message.
    """
    print("\nThanks for measuring your world with a feminist ruler!")

main()