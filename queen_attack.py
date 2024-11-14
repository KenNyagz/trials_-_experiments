def right_diagonal(r_q, c_q, n):
    """gets all possible moves on the right leaning diagonal of the queen"""
    r_q1 = r_q2 = r_q
    c_q1 = c_q2 = c_q
    #lower side of diagonal from position of queen
    lower_side = []
    for i in range(r_q - 1, 0, -1):
        r_q1 -= 1
        c_q1 -= 1
        if c_q1 > 0 and r_q1 > 0:
            lower_side.append([r_q1, c_q1])

    lower_side = list(reversed(lower_side))

    # upper side of diagonal from queen position
    upper_side = []
    for j in range(r_q + 1, n + 1, 1):
        r_q2 += 1
        c_q2 += 1
        #if r_q2 < n and c_q2 < n:
        upper_side.append([r_q2, c_q2])
    
    return lower_side + upper_side


def left_diagonal(r_q, c_q, n):
    """gets all possible moves on the left leaning diagonal of the queen"""
    r_q1 = r_q2 = r_q
    c_q1 = c_q2 = c_q
    #upper side of diagonal from position of queen
    upper_side = []
    for i in range(r_q + 1, n + 1, 1):
        r_q1 += 1
        c_q1 -= 1
        if c_q1 > 0 and r_q1 > 0:
            upper_side.append([r_q1, c_q1])

    upper_side = list(reversed(upper_side))

    # lower side of diagonal from queen position
    lower_side = []
    for j in range(r_q - 1, 0, -1):
        r_q2 -= 1
        c_q2 += 1
        if r_q2 <= n and c_q2 <= n:
            lower_side.append([r_q2, c_q2])

    return upper_side + lower_side
	
def vertical(r_q, c_q, n):
    """Finds all possible vertical positions the queen is eligible"""
    r_q1 = r_q2 = r_q
    #Upper vertical positions
    upper_verticals = []
    for i in range(r_q + 1, n + 1):
        r_q1 += 1
        upper_verticals.append([r_q1, c_q])

    #lower vertical positions
    lower_verticals = []
    for j in range(r_q - 1, 0, -1):
        r_q2 -= 1
        lower_verticals.append([r_q2, c_q])
        
    lower_verticals = list(reversed(lower_verticals))
        
    return lower_verticals + upper_verticals
	
def horizontal(r_q, c_q, n):
    """Finds all possible horizontal movements"""
    c_q1 = c_q2 = c_q
    
    # left horozontal positions
    left_positions = []
    for i in range(c_q - 1, 0, -1):
        c_q1 -= 1
        left_positions.append([r_q, c_q1])

    left_positions = list(reversed(left_positions))

    # right horizontal positions
    right_positions = []
    for j in range(c_q + 1, n + 1):
        c_q2 += 1
        right_positions.append([r_q, c_q2])

    return left_positions + right_positions
	
def queensAttack(n, k, r_q, c_q, obstacles):
    """The main logic
       Combines all the positions possible by the queen then tries to filter out the places already occupied and obstructed by obstacles
    """
    if n < 2:
        return 0

    vertical_positions = vertical(r_q, c_q, n)
    horizontal_positions = horizontal(r_q, c_q, n)
    right_diagonal_pos = right_diagonal(r_q, c_q, n)
    left_diagonal_pos = left_diagonal(r_q, c_q, n)
    
    for i in obstacles:
        if i in vertical_positions:
            vertical_positions = vertical_positions[0 : vertical_positions.index(i) + 1]
        if i in horizontal_positions:
            horizontal_positions = horizontal_positions[0: horizontal_positions.index(i) + 1]
        if i in right_diagonal_pos:
            right_diagonal_pos = right_diagonal_pos[0: right_diagonal_pos.index(i) + 1]
        if i in left_diagonal_pos:
            left_diagonal_pos = left_diagonal_pos[0: left_diagonal_pos.index(i) + 1]
    
    queen_map = vertical_positions + horizontal_positions + right_diagonal_pos + left_diagonal_pos
    print(queen_map)
    return len(queen_map)

if __name__ == "__main__":
    queensAttack(8, 2, 5, 4, [[3,7], [5,1]])
