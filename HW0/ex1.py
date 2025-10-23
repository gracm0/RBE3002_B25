def robot_move(moves):
    x = 0
    y = 0

    i = 0 # current index of moves
    for m in moves:
        match m[0]:
            case 'N':
                y += m[1]
            case 'E':
                x += m[1]
            case 'S':
                y -= m[1]
            case 'W':
                x -= m[1]

    return (x,y)


# # Test
# directions = [('N',2), ('E',4), ('S',1), ('W',3)]
# print(robot_move(directions))