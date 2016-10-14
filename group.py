
# # First level functionality
# The user provides a data file path, the mean vertical and horizontal spacing for that data file, and a sea level height (L >= 0).
# The program reads the data file, verifies that it follows the YXZ format.
# The program then calculates the land area above level L using the first approximation (as described above).
# The program reports the answer, expressed in absolute terms and as a percentage of the land area above the current sea level, to the user.

def first_level_functionality(file, y=0, x=0, z=0):
    """
    Calculates the land area above sea level (z) using a given data file (file),
    the mean horizontal spacing (x) and mean vertical spacing (y) and reports
    the answer in absolute terms as well as a percentage of the land
    area above the current sea level.

    For example:
    4 inputs:
            # sydney250m.txt    (data file path)
            # y = 0.278     (the mean vertical spacing)
            # x = 0.231     (the mean horizontal spacing)
            # z = +2 meters     (a sea level height (L >= 0))
    2 outputs:
            # 1064 square kilometers        (the land area above level L)
            # 98.87%        (as a percentage of the land area above the current sea level)


    >>> first_level_functionality('sydney250m.txt', 0.278, 0.231, 2)
    The land area above water in this area at + 2  meters will be
    1064 square kilometers, which is
    98.87 % of the current land area above water.

    """

    #problem:if no inputs enters a freeze state - fix this

    fileobj = open(file,'r')

    count_above_seaLevel = 0
    count_total = 0

    for row in fileobj:
        altitude = float(row.split()[2])
        # Split the argument into words using str.split().

        if altitude > 0:
            count_total += 1

            if altitude > z:
                count_above_seaLevel += 1
                #explain double for loop here

    area_above_seaLevel = int(x * y * count_above_seaLevel)

    percentage_landArea_above_seaLevel = \
    100 * round(count_above_seaLevel/count_total,4)

    fileobj.close()

    print("The land area above water in this area at +",z," meters will be ",
    area_above_seaLevel,"square kilometers, which is ",
    percentage_landArea_above_seaLevel,
    "% of the current land area above water.")






# Second level functionality

# The user may choose to not provide a sea level increase. In this case,
# The program finds the highest elevation in the given data file, divides
# the range from zero to the highest elevation into a suitable number of steps,
# computes the land area above each of them and reports all the answers to the user.


# Third level functionality

# The program does both level 1 and 2 functions, but computes both the first and
# second approximation (as described above) and reports the results of both
# approximations. The user also does not have to provide the mean vertical and
# horizontal spacing; these are automatically computed from the coordinates in the data file.



# Fourth level functionality

# In addition to the above, the program computes the number of separate
# connected land areas (islands) within the area covered by the data file at each
# sea level, and reports this as well.
# For the purpose of deciding what is a connected land area, we consider two
# sample points that are both above the sea level and adjacent, either
# vertically, horizontally, or diagnonally in any direction, to be part of the
# same connected land area.
