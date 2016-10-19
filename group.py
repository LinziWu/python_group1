import matplotlib as plt
import math


def first_level_functionality(file, y=0, x=0, z=0):
    """
    The first level of funcitonality calculates the land area above a certain
    sea level (z) using a given data file (file), the mean horizontal spacing
    (x) and mean vertical spacing (y) between the points. It reports the
    answer in absolute terms as well as a percentage
    of the land area above the current sea level.

    For example:
    4 inputs:
            # 'sydney250m.txt'    (file, must be in string form) or, as a full
            path like 'Users/john/Desktop/sydney250m.txt'
            # y = 0.278     (the mean vertical spacing)
            # x = 0.231     (the mean horizontal spacing)
            # z = 2 (meters)    (a sea level height where z >= 0)
    2 outputs:
            # 1064 (square kilometers of land area above sea level z)
            # 98.87%  (percentage of the total land area above sea level z)


    >>> first_level_functionality('sydney250m.txt', 0.278, 0.231, 2)
    The land area above water in this area at + 2  meters will be
    1064 square kilometers, which is
    98.87 % of the current land area above water.

    """

    fileobj = open(file,'r')

    count_above_sea_level = 0
    count_total = 0

    for row in fileobj:
        # Focuses on just the 'z' values of the data file using str.split()
        altitude = float(row.split()[2])

        if altitude > 0:
            count_total += 1

            if altitude > z:
                count_above_sea_level += 1
                # counts the amount of values above 'z'

    area_above_sea_level = int(x * y * count_above_sea_level)
    # calculates the area by multiplying the mean horizontal spacing,
    # mean vertical spacing and number of points above 'z'


    percentage_land_area_above_sea_level = \
    100 * round(count_above_sea_level/count_total,4)
    # calculates the percentage of total land area above 'z' by dividing
    # the number of points above 'z' by the total number of points and
    # multiplying that value by 100.


    fileobj.close()

    print(
    "The land area above water in this area at +",
    z,
    "meters will",
    area_above_sea_level,
    "square kilometers, which is",
    percentage_land_area_above_sea_level,
    "% of the total current land area above water.")



# Second level functionality

# The user may choose to not provide a sea level increase. In this case,
# The program finds the highest elevation in the given data file, divides
# the range from zero to the highest elevation into a suitable number of steps,
# computes the land area above each of them and reports all the answers to the user.


def second_level_functionality(file, mean_vertical, mean_horizontal):
    """ docstring goes here """

    fileobj = open (file, 'r')
    first_atltitude = fileobj.readline().split()[2]

    # Divides the range of the sea level from zero to the highest elevation
    # into a suitable number of steps

    x_max = float(first_atltitude)
    x_min = float(first_atltitude)

    for row in fileobj:
        altitude = float(row.split()[2])
        if altitude > x_max:
            x_max = altitude
        if altitude < x_min:
            x_min = altitude

    i = x_min
    k = x_max
    x_step = (i - k)/10
    points = []

    #[1,2,3,4,5,6,7,8,9,10]

    for t in range(x_min, x_max):
        for j in (i, i + x_step): #explain triple for loop
            for row in fileobj:
                if i < float(row.split()[2]) <= i + x_step:
                    count_above_seaLevel += 1 # why triple for loop? seems over the top

    points.append(count_above_seaLevel)

    area = mean_vertical * mean_horizontal

    area_list = [x*area for x in range (points)]
    result = new_list_forLevelTwo(area_list)

    n = 0

    while n < 10:
        plt.plot(points_list.extend(x_min + n * x_step , result[9 - n])) # comment explaining this
        n

    plt.ylabel('area_above_water')
    plt.xlabel('sea_level_increase')

    plt.show()

def new_list_forLevelTwo (z):
    k = 0
    new_list = []
    while z != []:
        n = len(z)
        k += z[n-1]
        new_list.append(k)

        z.pop(n-1)

    return new_list



# Third level functionality

# The program does both level 1 and 2 functions, but computes both the first and
# second approximation (as described above) and reports the results of both
# approximations. The user also does not have to provide the mean vertical and
# horizontal spacing; these are automatically computed from the coordinates in the data file.

def third_level_functionality(file):
    """ docstring goes here """

    fileobj = open(file, 'r')

    make_x_and_y_lists(file)

    fileobj.close()

def make_y_list(file):
    """ creates list of all the y values """

    fileobj = open(file, 'r')

    y_values_list = []

    for row in fileobj:
        # iterates through file for every y value and adds it to a list
        y_value = float(row.split()[0]) # the left column 'y'
        y_values_list.append(y_value)

    return y_values_list

    fileobj.close()

def make_x_list(file):
    """ creates lists of all the x values"""

    fileobj = open(file, 'r')

    x_values_list = []

    for row in fileobj:
        # iterates through every x value and adds it to a list
        x_value = float(row.split()[1]) # the middle column 'x'
        x_values_list.append(x_value)

    return x_values_list

    fileobj.close()


def mark_split_point_y(file, count=0):
    """ marks the first index point where y changes value """

    y_values_list = make_y_list(file) #makes y value list

    first_y_value = y_values_list[count] #stores the first y value on the list
    # as the reference point to see when it changes

    count = 0
    for value in y_values_list:
        if value == first_y_value:
            count += 1
            #goes through the y_valus and checks if they are the same,
            # stops when they change
    return count



def mean_horizontal_spacing(file):
    """ calculate the mean spacing between x-values on the first section
    of points (the first y value) and returns it expressed in km"""

    x_values_list = make_x_list(file) # makes list of x values

    y_value_change_index_point = mark_split_point_y(file) #finds the
    # point where the first y value changes

    end_x_value = x_values_list[y_value_change_index_point - 1]
    # finds the same point on the x value list

    horizontal_spacing = ((end_x_value - x_values_list[0]) / (y_value_change_index_point -1))
    # computes the horizontal_spacing between points on the first section of x
    #values using the formula (min - max) / (n -1) where n is the number of
    #points

    horizontal_spacing_km = (400075/360) * math.cos(horizontal_spacing)
    #converts that number into km (one arc degree of latitude )


    print(end_x_value)
    print(x_values_list[0])
    print(y_value_change_index_point - 1)
    print(horizontal_spacing)

    return horizontal_spacing_km



def mean_vertical_spacing(file):
    """ calculates the average spacing between y values on the file """

    y_values_list = make_y_list(file) #makes y value list

    #  makes a set of all the y_values to get rid of all the repeat values
    y_values_set = set(y_values_list)

    y_values_list = list(y_values_set)
    y_values_list.sort()

    positive_y_list = []

    for element in y_values_list:
        positive_element = abs(element)
        positive_y_list.append(positive_element)

    positive_y_list.sort()

    y_values_list = positive_y_list

    # converts negative list of y_values into a positive list of values with
    # no repitions


    vertical_spacing = ((max(y_values_list) - min(y_values_list)) / (len(y_values_list) - 1))

    vertical_spacing_km = (40007/360) * vertical_spacing


    print(max(y_values_list))
    print(min(y_values_list))
    print(len(y_values_list))
    print(vertical_spacing)

    return vertical_spacing_km


# Fourth level functionality

# In addition to the above, the program computes the number of separate
# connected land areas (islands) within the area covered by the data file at each
# sea level, and reports this as well.
# For the purpose of deciding what is a connected land area, we consider two
# sample points that are both above the sea level and adjacent, either
# vertically, horizontally, or diagnonally in any direction, to be part of the
# same connected land area.
