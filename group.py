import csv
import txt

# First level functionality

# The user provides a data file path, the mean vertical and horizontal
# spacing for that data file, and a sea level height (L >= 0).
def first_functionality(data_file_path, mean_vertical_spacing,
                        mean_horzontal_spacing, sea_level_height):


# The program reads the data file, verifies that it follows the YXZ format.

data_file = open(,)


# The program then calculates the land area above level L using the first
# approximation (as described above).





# The program reports the answer, expressed in absolute terms and as
# a percentage of the land area above the current sea level, to the user.



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
