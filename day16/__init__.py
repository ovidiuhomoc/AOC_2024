demoinput = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

demoinput2= """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

input1 = """#############################################################################################################################################
#.....#...#.......#.............#...#...........#...........#.#.......#.............#...#.......#.........#...#...#........................E#
#.#.#.#.#.#.#####.#.#.###.#####.###.#.###.#####.#.#.#######.#.#.#####.#########.###.#.#.#.#######.#.#####.#.###.#.#.###.#####.#.###########.#
#.#.#.#.#...#.....#.#...#.....#...#...#...#.....#.#.#...#...#.#.........................#.......#.#.....#.#.....#.#.#...#.....#.......#...#.#
###.#.#.#.#######.#####.#.#.#####.#.###.#######.#.#.#.#.#.###.###.#####.#.###.###.#.#.#.#.#####.#.#####.#.#######.#.#.###.###########.#.#.###
#...#.#.#.#.....#.#...#...#...#...#.#...#.........#...#.#.#...#.#.................#...#.#.....#.#.#...#.#.....#...#.#.....#.....#.#...#.#...#
#.###.#.#.#.###.#.#.#.#.#.#.#.#.###.#.###.#####.#.#####.#.#.#.#.###.#######.###########.###.#.#.#.###.#.#####.#.#.#.#######.#.#.#.#.###.###.#
#...#.#.#.#.#...#...#.#.#.#.#...#...#.....#.#...#...#...#...#...#...#...#.............#.....#.#.......#.......#...#...#.....#.#...#.....#...#
#.#.#.#.###.#.#######.#.#.#####.###.#######.#.#.#####.#.#######.#.###.#.###.#.###############.#.#####.#.#.#######.###.###.#.#.#.#.#######.#.#
#.#.#.#.....#.#.#...#.#.#.....#...#...#.....#.#.......#.....#...#...#.#...#.#.............#...#.#...#...#.#.........#.....#.#.#...#...#...#.#
#.#.#.#######.#.#.#.#.###.#.#.###.###.#.#.###.#########.#.#.#.#####.#.###.###.#######.###.#.#####.#.###.#.#.###############.#.#.#####.#.###.#
#.#.#.......#.#...#...#...#.#.#...#.....#.#...#.......................#.#...#.#.......#...#.......#.....#.#.#.....#.......#...#.#...#.#.....#
#.#.#######.#.#.#######.#.###.#.#######.###.###.#.#####.###.#####.#####.###.###.#######.#################.#.#.###.#.#.#####.###.#.#.#.#.###.#
#.#.#.....#...#.#.......#.#...#.......#.#...#...#...#.#...#...#.#.......#...#...#.....#...#.#.......#...#.#...#.#...#.#.....................#
#.#.#.#.#######.#.###.###.#.#########.###.###.#####.#.#.#.###.#.#####.###.###.#######.###.#.#.###.###.#.#.#.###.#####.#.#.#.###.###.#####.#.#
#.#.#.#.........#.#...#.#.#.......#.......#.#.#.#...#...#...#...#.....#.............#...#.#...#.#.....#.#.#...#.....#.......#.....#.#...#.#.#
#.#.###.###.#.#.#.#.###.#.###.###.###.#####.#.#.#.#########.###.#.#####.###.#######.###.#.#.###.#####.#.#.###.#.###.#########.#.#.#.#.#.#.###
#.....#...#.#.#.#.#...#.#.......#...#.........#.#.........#...#.#.#...#...#.#.....#.....#.#.#.......#.#.#...#.#...#.#.....#...#...#.#.#.#...#
#####.#####.###.#.###.#.###.#####.#.#.#####.#.#.#########.###.#.#.#.#.###.#.#.###.###.#.#.#.###.###.#.#.###.#.###.#.#.#####.###.#####.#.#.#.#
#...#.#...#...#.#.#.#.#...#.#...#.#...#.....#.#.#.......#...#...#.#.#...#.#.#.#.....#.#.#.#.#...#.....#...#.#.....#...#.....#...#.....#...#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###.#.#.#####.#.#.#####.###.#.###.#.###.#.#.###.#####.#.#.#.#.#######.#.#.#.#######.###.#####.#.#.#####.###.#
#.#.#...#.#.#.#.#...#.#.#.#...#.....#.#.......#.#...#...#...#...#.#...#.#.....#.#.....#...#...#...#.#.#.#.#.#...#...#...#...#...#.#...#.....#
#.#.###.#.###.#.#.#.#.###.#############.#.#####.###.#.###.#######.###.#.#.###.#.#.#####.#######.#.#.#.#.###.#.###.###.###.#.###.#.#.#######.#
#.#.....#...#.#...#.#...#.....#...#.....#.#.......#.#...#.#.....#.....#.#.#.#...#.#.....#.....#.#.#...#.....#.......#.....#...#.#.#.........#
#.#####.###.#.###.#.###.#.#####.#.#.#.###.#####.###.###.#.#.###.#####.#.#.#.#.#.#.#.###.###.#.#.#.#####.#.#####.#.###########.#.#.#.#.#######
#...#...#...#.#...#.....#.......#.#.#.....#...#.......#.#...#.#.#...#.#...#...#...#.....#...#...#.......#.......#.............#...#.#.#.....#
#.#.#.#.#.###.#.#######.#.#######.#.#######.#.#########.#####.#.#.#.#.#.#######.#.#.#####.#####.###############.#.#.#.#####.#.#####.#.#.###.#
#.#.#.#...#...#.#.......#...#...#...#.......#.....#.......#...#.#.#...#.#.......#.#.#.....#.....#.....#.........#.#.#.#...#.#.....#...#.#...#
###.#.#.#.#.#.#.###.#######.#.#######.#.#########.#.#####.###.#.#.###.#.#.#.#####.#.###.###.#####.###.#.###.###.###.###.#.###.###.#.#####.#.#
#...#.....#.#.#...#.#.....#.#.........#.#.....#.#.#.#...#.....#...#...#.#.#...#...#.....#.#...#.....#.#...#.....#...#...#.....#...#.....#.#.#
#.###########.###.#.#.###.#.#.#.#.#######.###.#.#.#.#.#######.#######.#.#####.#.#.#######.#.###.#####.###.#####.#.###.#######.#.#######.#.#.#
#.#.............#...#.#...#.#.#.#.#.....#.#.#.#.#.........#.#.#.......#.#.......#...#...#...#.....#...#...#.#...#...#.........#.#.........#.#
#.#.###.#######.#######.#.#.#.#.###.###.#.#.#.#.#####.#.#.#.#.#.#.#####.#.#########.#.#.#.###.#####.#.#.###.#.#.#.#.#########.#.#############
#.#...#.#.....#.........#.#.#.#...#.#.#...#.#.#.......#.#...#...#.#...#.#.#.......#.#.#...#...#...#.#.#...#...#...#.........#.#.......#.....#
#.#####.#####.###########.#.#####.#.#.#####.#.#.###.###.###.#####.#.#.#.#.###.#.#.#.#.#####.###.#.#.#.###.#.#########.#.#####.#.#####.#.###.#
#.....#.#...#.........#...........#.#.....#.#.#.#.....#...#.....#.#.....#...#.#.#...#...#.....#.#.#.#...#.#.....#...#.#.#...................#
#####.#.#.#.#####.###.#.#########.#.###.#.#.#.#.###.#.###.###.###.#.#####.#.#.#.###.#.###.#####.#.#.###.#.###.#.#.###.#.#.#####.#.#.#####.#.#
#.....#...#.........#...........#.#...#.#...#.#.....#.#.#...#.#...#...#...#.#.#.#.....#...#.#...#...#...#...#.....#...#.#...#.....#...#...#.#
#.#####.#.#####.###.#############.###.#.#.###.#######.#.###.###.#####.#.###.#.#.#.#####.###.#.#########.###.#####.#.#######.#.#.#####.#.###.#
#.#.....#...#.#...#.#.......#.....#...#.#.#...#.#.....#...#.#.......#.#.#.#.#.....#...#...#.#.#.......#...#.....#.#.......#.#.......#.#...#.#
#.###.###.#.#.###.###.#####.#.###.#.###.###.###.#.#####.###.#.#######.#.#.#.###.#####.###.#.#.#.#####.#########.#.#####.###.#####.#.#.###.###
#...#...#.#...#...#.......#...#...#...#.....#...#.....#.....#...#.....#...#...#.........#...#.#.....#.....#...#.#.#...#.....#...#.#.#...#...#
#.#.###.#.###.#.###.#########.###.###.#####.###.#####.#.#.#.#.#.#.#######.###.#.#####.###.#.#.#####.#####.#.#.#.#.#.#.#######.#.###.###.###.#
#.#.#.....#...#.....#.#.....#.......#.#...#...........#.#.....#.#...#...#.#.#.....#...#...#.#.#...#...#.#...#...#...#.#.......#.#...#...#...#
#.#.#####.#.#######.#.#.###.#######.#.#.#.###.#####.###.###.###.###.#.#.#.#.#####.#####.###.#.#.#.###.#.#########.#.#.###.#####.#.###.###.###
#.#.......#.#.....#...#.#.#.#...#.......#.#...#...#.......#.......#.#.#.....#.....#...#.#...#...#...#.........#.....#.....#...#.#.#.#...#...#
#.#######.###.###.#####.#.#.#.###.#######.#.###.#.#####.#.###.###.#.#.#######.#####.#.#.###.#######.#.#.#######.#.#########.###.#.#.###.###.#
#.#.....#.......#.#...#...#.#.....#.......#.#...#.#.........#.....#.#.#...#...#.....#.#...#.......#...#.#.......#...#.....#...#...#.....#...#
###.###.#.#.#####.#.#.###.#.#####.#.#.#.###.#.###.#.#######.#######.#.#.#.#.###.#.###.###.#.#####.#####.#.#########.#.#.#.###.#####.#####.#.#
#.....#...#...#...#.#.#...#.....#.#.#.#.#.....#.....#.........#.........#.#.....#...#.....#.#.......#.......#.......#.#.#.....#...#.....#.#.#
#.###.###.#.###.###.#.#.#####.#.###.#.#.###.#########.#######.#.#########.#########.#.#####.#######.#########.#.###.#.#.#.#####.#.#.#####.###
#.#...#...#.#...#...#...#...#.#.....#.#.#...........#.#.....#...#...............#...#.......#.....#.........#.#...#.#.#.#.#.....#...#...#...#
#.#.###.#.#.#.#.#.#######.#.#####.#.#.#.#.#########.###.###.###########.#######.#.#.#######.#.###.#########.#.#.#.###.#.###.#########.#.#.#.#
#.#...#.#...#.#.#.#...#...#.....#.#.#...#.#.......#.....#...#.........#.#...#.....#.........#.#.#.......#...#.#.#.....#...#...#.......#.#.#.#
#.#.#.#.#.###.#.#.###.#.#######.#.#.###.#.#.#####.#######.###.#######.###.#.#####.#########.#.#.#######.#.###.#.#########.#.###.#######.#.#.#
#.#.#.#.#.#...#.#...#.#.#.....#...#.......#.....#.....#...#...#.....#.....#.........#...#...#.#.#.....#...#...#.............#...#...#...#.#.#
#.###.#.#.#.###.###.#.#.#.###.#######.#.#.#.###.#.###.#.#.#.###.###.###############.#.###.###.#.#.###.#.#.#.###########.#####.###.#.#.#####.#
#...#...#...#.#.#.#.#.#...#.#.#.....#.#.#.#.#.....#...#.#.#.....#...#...........#.#.#.......#...#.#...#.#.#.........#...#.....#...#...#.....#
#.#.#.###.###.#.#.#.#.#####.#.#.###.#.###.#.#.#.#.#.###.#########.#####.#######.#.#.#########.###.#.###.#.#.#.#######.###.#######.#####.###.#
#.#.#...#...#.#.#.#.#.......#...#...#.....#.#.#...#.............#.....#...#.#...#.#.#.........#...#.....#.#.#...................#.....#.#...#
#.#.###.###.#.#.#.#.#.#.#########.#.#######.#.#######.#########.#####.###.#.#.###.#.#.#########.#########.#.###########.###.###.#####.#.#.###
#.#.#.#.#...#.....#.#.#.#.........#.#.....#.#...#.....#...#.....#...#.....#.#.....#.#.....#.....#.........#.#...#.........#...#.....#...#...#
###.#.#.#.#######.#.###.#.#########.###.###.###.#.#####.#.#.###.#.#.#######.###.###.#.###.#.#######.#####.#.#.#.#.#####.#.###.#####.#######.#
#...#...#.......#.#...#.#...#.....#.#...#...#.#.#...#...#.#...#.#.#...#.........#...#.....#.#.......#.........#.#.#.....#.........#...#.....#
#.###.###.#####.#####.#.###.###.###.#.#.#.###.#.###.#.###.###.#.###.#.#.#########.#######.#.#.#####.#.###########.#####.#########.#.#.#######
#...#...............#.....#...#.....#.#.#.#...#.......#.....#.#.#...#.#.#...#...#.........#.#.#...#.#...#.......#.#.......#...#...#.#.......#
#.#.###.#######.#.###.#######.#.#####.###.#.#####.#.###.###.#.#.#.#####.#.#.###.###########.#.#.#.#####.#.#.###.#.#.#####.###.#.###.#######.#
#.#.#.....#...#.#.....#...........#.....#.#.....#.#.#...#...#.#.#.#...#...#.....#.........#.#...#.......#.#.#...#.#.....#.....#.#.#.#.#...#.#
#.#.#####.#.#.#.#.#####.#########.#####.#.#####.#.#.#.###.###.#.#.#.#.#.#######.#.#######.#.###.###########.#.###.#.###.###.###.#.#.#.#.#.#.#
#.#...#.....#...#...#...#.......#.....#...#...#.#.#.#.....#...#...#.#...#.....#.#.....#...#...#...#.........#.....#.#...#...#...#...#.#.#...#
#.###.#########.#####.#########.#####.#.###.#.#.#.#.#.#####.#######.###.#.###.#.#####.#######.###.#.#################.###.###.###.###.#.###.#
#...#.....#...........#...........#...#.....#...#...#.....#.#.......#...#.#...#.......#.......#.#...#...............#.#...#...#.......#.#...#
###.#.###.#.#########.###.#.#####.#.#####.#####.#########.#.#.#####.#.###.#.###.#####.#.#######.#####.#######.#####.#.#####.###########.#####
#.......#.#...#...#.......#.#...............#.#.#.#.......#.......#.#.....#...#.#.......#...........#.....#.#.#.......#...#.......#...#.#...#
#.###.###.#####.#.#.###.###.#.#.#.#########.#.#.#.#.#####.#####.#.#.#########.#.#.#######.#####.###.#####.#.#.###.#####.#.#.#####.#.#.#.#.#.#
#.#.#...#.#.....#.#.#...#.#.#...#...#.......#.#...#.....#...#...#.#.....#.....#.#.....#...#...#...#.....#.#.#...#.#.....#.........#.#...#.#.#
#.#.#.#.#.#.#####.#.#.###.#.###.###.#.#######.###.#####.###.#.###.#####.#.#####.#####.#####.#.###.###.###.#.###.###.#######.#######.#.###.#.#
#.#.#.#...#...#.#.#.#.#.....#.#.#.#...#...#...........#...#.#...#.#...#.#.#...#.....#...#...#...#...#.......#...#...#.......#.......#...#.#.#
#.#.#.#######.#.#.#.#.#.#####.#.#.#####.#.#.#############.#.###.#.#.#.#.#.#.#.###.#.###.#.#####.#############.###.###.#####.###.###.#.#.#.#.#
#...#.......#.#.#.#...#.....#.#...#...#.#.#.......#.....#.#...#.#.#.#.#.#...#.#...#.#...#...#.....#.....#...#.#...#...#...#...#...#...#...#.#
###.#.###.###.#.#.###.#####.#.###.#.###.#.#.#######.###.#.###.#.#.#.#.#######.###.#.#.#####.#####.#.###.#.#.#.#.###.###.#####.#.#####.#####.#
#...#.....#...#.#.#...#.........#.#.....#.#.#.......#.#.#...#.#.#.#.#.......#.#...#.#.#...#.....#...#.....#.#.#.#.....#.......#.#.....#...#.#
#.###.###.#.###.#.#.#####.#######.#.#####.#.#.#######.#.###.#.#.#.#.###.#####.#.###.#.#.#.#.###.###########.#.#.#####.#.#######.#.###.#.#.#.#
#.#...#...#...#.#.#.....#.#.......#.....#...#.#.....#.#.#...#.#...#...#.......#.....#.#.#.....#.........#.....#.......#.#.......#...#...#.#.#
#.#.#.#.#####.#.#.#####.###.###############.#.#.###.#.#.#.###.#.#.#.#.#########.#.###.#.#.#.#.#####.###.#########.#####.###.#####.#.#.#.#.#.#
#.#...........#.#.#.........#.............#.#.#...#...#...#...#.#.....#.#.....#.#...#...#.#.#.....#...#...#...........#...#.#.....#.#.#...#.#
#.###.#.#######.#.#.#####.#########.#####.###.#.#.#########.###.#######.#.###.#.#.#.#####.###.###.#.#####.#.#########.###.###.###.#.#.#.###.#
#.....#.....#...#.#.....................#.....#.#.#.........#.#...#.........#...#.....#...#...#.#...#.....#.#.......#...#.#...#...#.#.#.....#
#####.#.#.#.###.#.#.#################.#.#########.#.#########.###.#.#.#.###.#####.#.###.#.#.###.###.#.#.###.#.#####.###.#.#.#####.#.#.#####.#
#.#...#.#.#.....#.#.#.............#...#.#...#...#.#.......#...#...#.#.#...#.#.....#...#.#.#.#...#...#.....#...#.....#.#...#.....#...#.....#.#
#.#.#.#.#.#####.#.#.#.###########.#.###.#.#.#.#.#.#######.###.#.###.#.#####.#########.#.###.#.#.#.#######.#####.#####.###.#####.#.###.###.#.#
#.........#.....#.#.#.......#.#...#.#.#...#...#.#.......#.....#.#...#...........#.....#.....#.#.#.......#.....#.....#.#.......#.........#...#
#.###.#.#########.#.#.#.###.#.#.###.#.###.#####.#.#####.#.#.#.#.#####.#########.#.###.#########.#######.#.###.#####.#.#.#.###.#.#.#####.#.###
#.#.....#.........#.#...#.#.#.#...#.#.........#.#.#...#...#.#.#.....#.#.......#...#...........#.#...#...#...#.#.....#...#...#.#.......#.#...#
#.#.#.#.#.#########.#.#.#.#.#.###.#.#.###.#####.#.#.#.#.###.#.#####.###.#####.###############.#.#.#.#.#######.#.###########.#.#.#.#####.###.#
#.#.#.#.#.#.........#...#.#.#...#...#.#...#.......#.#...#...#.....#.....#...#.......#.....#.....#.#...#.......#...#.....#...#.#.#.......#...#
#.#.#.#.#.#.#############.#.#.#.#####.#.###.#####.#######.###.#.#########.#########.#.###.#.#####.#####.###.#####.#.###.#.###.###.###########
#.#.#...#.#.#.....#.......#...........#.#...#.....#.......#...#.#.......#.....#...#...#...#.#.....#.#.....#.#...#...#.#...#.#...#.#...#.....#
###.#.#.#.#.#.###.#.###.###.#.#####.###.#.###.#.#.#.#.#######.#.#.###.#.###.#.#.#.#####.###.#.#####.#.#.#.###.#.#####.#####.###.#.#.#.#.###.#
#...#...#.#.#...#...#.#...#...#.....#...#.#.#...#.#...#.......#.#.#...#.....#...#...#...#...#.#.......#.#.#...#.....#.....#.....#...#.#.#.#.#
#.###.#.#.#####.#####.###.###.#.#########.#.#.#.#####.###.#.#.#.#.#.#.#####.#########.#######.#.#######.#.#.#####.###.#.###.#.#######.#.#.#.#
#.....#.#...#...#.......#...#.#.......#...#...#.....#...#.#.#.#...#.#.....#.#.......#.......#.#.....#...#...#...#.....#.....#.........#.#.#.#
#.###.#.###.#.#######.#.###.#.#######.#.###########.###.#.#.#.###.#.###.###.#.#.###.#######.#.#####.#.#.#####.#.#############.#########.#.#.#
#.#.#.#.#...#.#.......#.#.#.#.........#.#.........#.....#.#.#...#.#.#...#...#.#...#.......#...#...#.#.#.....#.#.....#.........#...........#.#
#.#.#.#.#.#.#.#.#.#####.#.#.#########.#.#.#######.#.#####.#.###.###.#.###.###.#.#.#######.#####.#.#.#.###.#.###.#####.#######.#.#########.#.#
#...#.#...#.#.#.#.#...#.#.#...........#...#.....#.#.....#.#...#...#.#.....#.....#.......#.#.....#...#.#...#...#...#...#...#...#.....#...#.#.#
###.#.#######.#.#.#.#.#.#.###.#.###########.###.#.#####.#####.###.#.#.#####.###.#.#.#.###.#.###########.#.###.#.#.#.###.#.#.#######.#.#.###.#
#.#.#.........#.#.#.#.#.#...#...#...........#...#.....#.......#.....#...#.#...#.#.#.#.....#.#.....#.....#.#...#.#...#...#.#.#.....#.#.......#
#.#.#############.#.###.#.###################.#####.#.###.#####.#######.#.###.#.#.#.#.#.###.#.#.###.#.###.#.###.###.#.###.#.#.#.###.#.#####.#
#.#...#...........#.#...#.#...........#.......#...#.#.#.......#...#...#...#...#.#...#.#.....#.#.#...#.#...#...#.....#...#.#...#.#...#...#...#
#.###.#######.#####.#.###.#.###.###.#.#.#####.#.#.#.#.#####.#.#####.#.###.#.###.#.#.#.#########.#.###.###.###.#####.###.#.#####.#.#####.#####
#...#.....#...#.....#...#...#...#...#...#.#...#.#...#.....#.#.#...#.#...#.#.#...#.#.#...#.....#.....#.#.....#.....#...#.#.....#.#.....#.....#
#.#######.#.###.###.###.#.###.###.#.#####.#.###.#.#####.#.#.#.#.#.#.###.###.#.#.#.#.###.#.###.#######.#.#########.###.###.#####.#####.#####.#
#.......#...#.#.#.#...#.#.#.......#.#.....#.#...#.....#.#.#.#...#.....#.#...#.#...#.#.....#...#...#...#...#...#...#.#...#.....#.......#...#.#
#.#.#########.#.#.###.#.###.###.###.#.#.#.#.#.#######.#.#.#.###########.#.#########.#######.###.#.#.###.#.#.#.#.###.###.#####.###########.#.#
#.#.#.......#.......#.#...#.#.....#.#.#.#.#.#.....#.#.#.#.#.#.#.......#.#.........#.....#...#...#...#...#.#.#.#.#...........#.....#.......#.#
###.#.#.#####.#######.###.#.###.###.#.#.#.#.#####.#.#.###.#.#.#.#####.#.#########.#.###.#.#####.#####.###.#.#.#.#.#.#######.#.###.###.###.#.#
#...#.#.....#.#.#.........#...#.#...#.#.#.#.#...#.#.#...#.....#...#.........#.....#.#.#.#.....#.........#.#.#.#.#...#...#...............#.#.#
#.###.#####.#.#.#.#####.#####.###.###.#.###.#.###.#.###.#########.#########.#.#####.#.#.#####.#########.#.#.#.#.#####.#.#######.#.#.###.#.#.#
#.....#...#.....#.#.....#...#...#.....#...#.....#.#...#.........#.....#.#...#.#.......#.#...#.........#.#...#.#.......#.....#...........#.#.#
#.#####.#.###.###.#.#####.#.#.#.#.#######.#.###.#.#.###.#.#####.###.#.#.#.###.#.###.###.###.#####.###.#.#####.#.###########.#.###.#.#####.#.#
#.....#.#...#...#.#.......#.#.#.#...#.#...#.....#.#.......#...#...#.#.#.#.#.#.#...#...#.#...#...........#...#.......#.......#...#.........#.#
###.#.#.#.###.#.#.#.#.#.###.#.#.###.#.#.#.#####.#.#########.#####.###.#.#.#.#.#####.#.#.#.#.#.###########.#.#####.#.#.###########.#.#######.#
#...#...#...#.#...#.#.#.#.#.#.#.#...#.#.#.#...#.#.........#.....#...#.......#...#...#...#.#.#.......#.....#.......#.#.#...#.....#.........#.#
#.###.#.###.#.###.#.###.#.#.#.#.#.###.#.#.###.#.#########.###.#####.#.#########.#.#######.#.###.#.#.#.#.#######.#####.#.#.#.###.#.#.#####.#.#
#.#.......#.#.#...#...#.#.#.#.#.#.....#.#.....#.......#.#...#.........#.....#...#.#.............#.#...#.#.......#...#...#.....#...........#.#
#.#######.#.#.#.#####.#.#.#.###.#####.#.###.###.#####.#.###.###.#####.#.###.#.###.#.#.#.#.###.###.#####.#####.###.#.#########.#####.###.###.#
#...............#...#...#.#.....#.#...#...#.#...#...#.....#.........#.#...#.#.#...#.#.#.#.....#...#...#.#.........#.....#...#.....#.#.#.....#
#######.###.#.#.#.#.#####.#######.#.#####.###.###.#.#####.#####.###.###.###.#.#.###.#.#.#.#####.###.###.#.###.###.#.#####.#.#.###.#.#.#.#.#.#
#.....#.....#.#...#.....#.....#.....#...#.....#...#.....#.#.......#.........................#...#...#...#...#.#...#.....#.#...#.#...#...#.#.#
#.#.#####.###.###########.###.#.#####.#.#######.#######.#.#.###.#.#######.#.#####.#######.###.###.#.#.#####.#.#.#.#####.#.#####.###.#.#.#.#.#
#.#.#.....#...#.....#.....#.#...#...#.#...........................#.........#.....#.....#.#...#...#.#.#.....#...#...#...#.....#.......#.#.#.#
#.###.#####.#.#.###.#.#####.#####.#.#.#.#####.#.#######.#####.#.#.#.#######.###.###.#.###.#.#.#.###.#.#.#######.#.#.#.#.#####.###.#.#.#.#.#.#
#.#...#...#...#.#.#...#.....#...#...........#.#.......#.....#...#...#.....#...#...#.....#.#.#.....#.#...#.....#.#.#.#.#...#...#...#.#...#.#.#
#.#.#####.###.#.#.#####.###.#.#.#######.#.###.#######.#####.#.#.#######.#.###.###.###.#.#.#.#.###.#.#######.#.###.###.###.#.###.###.#.#.#.###
#...#.....#.#.#.#.......#...#.#.#...#...#.#...#...#.#...#.#.#.#...#...#...................#.......#.#.....#.#...#.#...#...#.....#.#.....#...#
#.###.###.#.#.#.#######.###.#.#.#.#.#.###.#.###.#.#.###.#.#.###.#.#.#.#.###.#.#####.#.#.#.###.#####.#.###.#.###.#.#.#######.#.###.#.#####.#.#
#.#.......................#...#.#.#...#.#...#...#...#.#.#.........#.#.#...................#.................#...............................#
#.#.###.###.#.#.#.###.###.#####.#.#####.#.###.#####.#.#.#######.###.#.#########.#####.###.#.#.#######.#.#####.###.#.#.#.#.###.#.###.#.#.###.#
#S..#.......#.....#.......#.......#...........#.......#.............#...............#.................#...........#...#.......#.......#.....#
#############################################################################################################################################"""