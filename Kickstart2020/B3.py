'''
Your country's space agency has just landed a rover on a new planet, which can be thought of as a grid of squares containing 109 columns (numbered starting from 1 from west to east) and 109 rows (numbered starting from 1 from north to south). Let (w, h) denote the square in the w-th column and the h-th row. The rover begins on the square (1, 1).

The rover can be maneuvered around on the surface of the planet by sending it a program, which is a string of characters representing movements in the four cardinal directions. The robot executes each character of the string in order:
N: Move one unit north.
S: Move one unit south.
E: Move one unit east.
W: Move one unit west.
There is also a special instruction X(Y), where X is a number between 2 and 9 inclusive and Y is a non-empty subprogram. This denotes that the robot should repeat the subprogram Y a total of X times. For example:
2(NWE) is equivalent to NWENWE.
3(S2(E)) is equivalent to SEESEESEE.
EEEE4(N)2(SS) is equivalent to EEEENNNNSSSS.

Since the planet is a torus, the first and last columns are adjacent, so moving east from column 109 will move the rover to column 1 and moving south from row 109 will move the rover to row 1. Similarly, moving west from column 1 will move the rover to column 109 and moving north from row 1 will move the rover to row 109. Given a program that the robot will execute, determine the final position of the robot after it has finished all its movements.
'''         

T = int(input())
for _ in range(T):
    command = input()

    multi = [1]
    multiple = 1
    cmd = {'N':0, 'W':0, 'S':0, 'E':0}

    # calculate how many N/W/S/E to walk in total
    for i in command:
        if i.isdigit():
            multi.append(int(i))
            multiple *= int(i)
        elif i == '(':
            continue
        elif i == ')':
            multiple //= multi.pop()
        else:
            cmd[i] += multiple

    fx = (1 - cmd['W'] + cmd['E']) % (10 ** 9)
    fy = (1 - cmd['N'] + cmd['S']) % (10 ** 9)

    fx = fx if fx != 0 else 10 ** 9
    fy = fy if fy != 0 else 10 ** 9

    print('Case #{}: {} {}'.format(_ + 1, fx, fy))