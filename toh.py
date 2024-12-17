def move_disk(from_peg, to_peg):
    print(f"Move disk from {from_peg} to {to_peg}")

def solve_tower_of_hanoi(n, from_peg, aux_peg, to_peg):
    if n == 1:
        move_disk(from_peg, to_peg)
        return
    solve_tower_of_hanoi(n - 1, from_peg, to_peg, aux_peg)
    move_disk(from_peg, to_peg)
    solve_tower_of_hanoi(n - 1, aux_peg, from_peg, to_peg)

# Call the function to solve the Tower of Hanoi problem for 2 disks
solve_tower_of_hanoi(2, 'A', 'B', 'C')
