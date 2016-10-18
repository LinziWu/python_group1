import matplotlib as plt


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

    fileobj = open(file,'r')

    count_above_seaLevel = 0
    count_total = 0

    for row in fileobj:
        # Split the argument into words using str.split()
        altitude = float(row.split()[2])

        if altitude > 0:
            count_total += 1

            if altitude > z:
                #explain double for loop here
                count_above_seaLevel += 1

    area_above_seaLevel = int(x * y * count_above_seaLevel)

    #comment explain this
    percentage_landArea_above_seaLevel = \
    100 * round(count_above_seaLevel/count_total,4)

    fileobj.close()

    print(
    "The land area above water in this area at +",
    z,
    "meters will be",
    area_above_seaLevel,
    "square kilometers, which is",
    percentage_landArea_above_seaLevel,
    "% of the current land area above water.")


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
        for j in (i, i + x_step):
            for row in fileobj:
                if i < float(row.split()[2]) <= i + x_step:
                    count_above_seaLevel += 1
    points.append(count_above_seaLevel)

    area = mean_vertical * mean_horizontal

    area_list = [x*area for x in range (points)]

    result = new_list_forLevelTwo(area_list)
    n = 0
    while n < 10:
        plt.plot(points_list.extend(x_min + n * x_step , result[9 - n])
        n += 1

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

    fileobj = open (file, 'r')


    x_values_list = []
    y_values_list = []

    for row in fileobj:
        # iterates through every x value and adds it to a list
        x_value = float(row.split()[1]) # the middle column 'x'
        x_values_list.append(x_value)
        # iterates through file for every y value and adds it to a list
        y_value = float(row.split()[0]) # the left column 'y'
        y_values_list.append(y_value)


    # makes a set of all the y_values to get rid of all the repeat values
    y_values_set = set(y_values_list)

    # need to figure out how to find spacing value for every different y value



    fileobj.close()



# Fourth level functionality

# In addition to the above, the program computes the number of separate
# connected land areas (islands) within the area covered by the data file at each
# sea level, and reports this as well.
# For the purpose of deciding what is a connected land area, we consider two
# sample points that are both above the sea level and adjacent, either
# vertically, horizontally, or diagnonally in any direction, to be part of the
# same connected land area.


def fourth_level_funtionality (file, h):
    """ docstring """
    fileobj = open(path, 'r')
    read_line = fileobj.readline()
    y_northest = float(read_line.split()[0])
    fileobj.close()


    # Reopen the file because we've already read one row and the next row will be the second row.
    fileobj = open(path, 'r')
    count_row_num = 0
    count_total_rows = 0        # Use array to represent the map, we need to find the number of rows and columns in the array.
    for row in fileobj:
        y_list.append(line_list[0])
        x_list.append(line_list[1])
        z_list.append(line_list[2])
        row_list = [float(row.split()[0]), float(row.split()[1]), float(row.split()[2])]

        count_total_rows += 1
        if row_list[0] == y_northest:
            count_row_num += 1


    # Make the graph as a array
    num_ROW = count_row_num
    num_COL = int(count_total_rows/count_row_num)


    count_island = 0;
    for i in range(0,ROW):
        for j in range(0, COL):
            if (Map[i][j]==1 and visited[i][j] == False):       # If a cell with value 1 is not visited yet, then new island found.
                visit_conneceted_land(visited, Map, i, j)       # Visit all cells in this island
                count_island += 1                               # Increment island count
    return count_island


def not_out_of_range (visited, Map, i, j):
     """ docstring """

     if visited[row][col] == False and M[row][col]==1 and row < ROW and col < COL :
         return True
     else:
         return False


def visit_conneceted_land(Map, row, col, visited):
    """ docstring """

        # Use a list to get row and column numbers of 8 neighbors of a given cell
        # From top to bottom, from left to right, both increment by 1.
        row_num = [-1, -1, -1,  0,  0,  1, 1, 1]
        col_num = [-1,  0,  1, -1,  1, -1, 0, 1]

        # Mark this cell as visited
        visited[row][col] = true;

        # Recur for all connected neighbours
        for i in range(0,9)
            if (not_out_of_range(visited, Map, row + row_num[i], col + col_num[i]):
                visit_conneceted_land(visited, Map, row + row_num[i], col + col_num[i])


# Just wanna know the number of the same y divided by the number of all rows
# 'sydney250m.txt': 24644/202 = 122
# 'tas2k.txt' : 41410/205 = 202
def count(path):
    """ docstring """

    fileobj = open(path, 'r')
    read_line = fileobj.readline()
    y_northest = float(read_line.split()[0])
    fileobj.close()

    total = 0
    count = 0
    fileobj = open(path, 'r')
    for row in fileobj:
        total += 1
        if (float(row.split()[0]) == y_northest):
            count += 1

    return (count,total)
