import sys
input = sys.stdin.readline


def move_fireballs(fireballs, grid_size):
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    new_positions = [[[] for _ in range(grid_size)] for _ in range(grid_size)]

    for fireball in fireballs:
        row, col, mass, speed, direction = fireball
        new_row = (row + speed * directions[direction][0]) % grid_size
        new_col = (col + speed * directions[direction][1]) % grid_size
        new_positions[new_row][new_col].append([mass, speed, direction])

    return new_positions

def process_collisions(positions, grid_size):
    new_fireballs = []
    for row in range(grid_size):
        for col in range(grid_size):
            if len(positions[row][col]) > 1:
                total_mass, total_speed, odd_count, even_count = 0, 0, 0, 0
                fireball_count = len(positions[row][col])

                for mass, speed, direction in positions[row][col]:
                    total_mass += mass
                    total_speed += speed
                    if direction % 2 == 0:
                        even_count += 1
                    else:
                        odd_count += 1

                new_mass = total_mass // 5
                if new_mass > 0:
                    new_speed = total_speed // fireball_count
                    new_directions = [0, 2, 4, 6] if odd_count == 0 or even_count == 0 else [1, 3, 5, 7]
                    for direction in new_directions:
                        new_fireballs.append([row, col, new_mass, new_speed, direction])

            elif len(positions[row][col]) == 1:
                new_fireballs.append([row, col] + positions[row][col][0])

    return new_fireballs

def simulate_fireballs(grid_size, initial_fireballs, iterations):
    fireballs = initial_fireballs

    for _ in range(iterations):
        new_positions = move_fireballs(fireballs, grid_size)
        fireballs = process_collisions(new_positions, grid_size)

    return sum(fireball[2] for fireball in fireballs)

grid_size, fireball_count, iterations = map(int, input().split())
initial_fireballs = []

for _ in range(fireball_count):
    row, col, mass, speed, direction = map(int, input().split())
    initial_fireballs.append([row-1, col-1, mass, speed, direction])

result = simulate_fireballs(grid_size, initial_fireballs, iterations)
print(result)
