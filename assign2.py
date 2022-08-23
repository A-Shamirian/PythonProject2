# Assignment 2: Annie Shamirian (251103387)

import area_calculation


def is_valid_shape(in_value):
    """ Checks whether the shape asked for by the user is one of the
    shapes that can have its area calculated."""
    if str.lower(in_value) in ('ellipse', 'trapezoid', 'rectangle', 'done'):
        valid = True
    else:
        valid = False
    return valid


def main():
    user_shape = ''  # initialize a variable for user input
    area_list = []  # initialize a list for areas calculated by main program

    while user_shape != 'done':  # only exit the loop if the user types 'done'
        user_shape = str.lower(input('What shape would you like to calculate?\n'))
        if is_valid_shape(user_shape) is False:  # check to make sure user input is valid
            print('Sorry, but that shape doesn\'t exist in our system. Please try again.\n')
        elif user_shape == 'ellipse':  # when prompted, calculate area of ellipse and add result to area_list
            major = float(input('What is the major radius of the ellipse?\n'))
            minor = float(input('What is the minor radius of the ellipse?\n'))
            area_ellipse = float(f'{area_calculation.ellipse_area(major, minor):.2f}')
            print('The calculated area is', f'{area_ellipse}' + '.')
            area_list.append(area_ellipse)
        elif user_shape == 'trapezoid':  # when prompted, calculate area of trapezoid and add result to area_list
            top = float(input('What is the length of the trapezoid\'s top?\n'))
            bottom = float(input('What is the length of the trapezoid\'s bottom?\n'))
            height = float(input('What is the trapezoid\'s height?\n'))
            area_trap = float(f'{area_calculation.trapezoid_area(top, bottom, height):.2f}')
            print('The calculated area is', f'{area_trap}' + '.')
            area_list.append(area_trap)
        elif user_shape == 'rectangle':  # when prompted, calculate area of rectangle and add result to area_list
            base = float(input('What is the length of the rectangle\'s base?\n'))
            height = float(input('What is the height of the rectangle?\n'))
            area_rect = float(f'{area_calculation.rectangle_area(base, height):.2f}')
            print('The calculated area is', f'{area_rect}' + '.')
            area_list.append(area_rect)

    print('Thanks for using this program! Here is a list of the areas that we calculated for you:')
    print()
    print(sorted(area_list))  # print a list of all the areas calculated from smallest to largest


main()
