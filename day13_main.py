import day13
from day13 import MachineSetup


def day13_main(input: str | list[MachineSetup], part=1):
    machines: list[MachineSetup] = []

    a_cost = 3
    b_cost = 1

    if isinstance(input, str):
        for machine in input.split('\n\n'):
            machine_lines = machine.split('\n')

            move = list(map(int, [coord.split('+')[1] for coord in machine_lines[0].split('Button A:')[1].strip().split(', ')]))
            a_x, a_y = move[0], move[1]

            move = list(map(int, [coord.split('+')[1] for coord in machine_lines[1].split('Button B:')[1].strip().split(', ')]))
            b_x, b_y = move[0], move[1]

            prize = list(map(int, [coord.split('=')[1] for coord in machine_lines[2].split('Prize:')[1].strip().split(', ')]))
            prize_x, prize_y = (prize[0], prize[1]) if part == 1 else (prize[0] + 10000000000000, prize[1] + 10000000000000)

            machines.append(MachineSetup(P_x=prize_x,
                                         P_y=prize_y,
                                         a_x=a_x,
                                         a_y=a_y,
                                         b_x=b_x,
                                         b_y=b_y))
    elif isinstance(input, list):
        machines = input
    else:
        raise ValueError("Invalid input type")

    computed_total_cost = sum(machine.get_min_cost() for machine in machines)
    return computed_total_cost


if __name__ == '__main__':
    dinput = day13.demoinput
    input1 = day13.input1

    # print(f"{main(dinput, part=1) = }")
    # print(f"{day13_main(input1, part=1) = }")
    print(f"{day13_main(input1, part=2) = }")
