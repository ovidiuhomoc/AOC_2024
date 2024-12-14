import random

from day13 import MachineSetup
from day13_main import day13_main


def test1(count: int):
    max_gen = 1000

    for i in range(count):
        a_count = random.randint(1, max_gen)
        b_count = random.randint(1, max_gen)

        a_x = random.randint(1, max_gen)
        a_y = random.randint(1, max_gen)
        b_x = random.randint(1, max_gen)
        b_y = random.randint(1, max_gen)

        prize_x = (a_count * a_x) + (b_count * b_x)
        prize_y = (a_count * a_y) + (b_count * b_y)

        machine = MachineSetup(P_x=prize_x,
                               P_y=prize_y,
                               a_x=a_x,
                               a_y=a_y,
                               b_x=b_x,
                               b_y=b_y,
                               test_injected_a_count=a_count,
                               test_injected_b_count=b_count)

        result = machine.get_a_b_press_count()
        if result is None:
            print(f"Test failed for {machine} with a_count={a_count}, b_count={b_count}. \n{machine = }")
            raise Exception("No solution")
        if not isinstance(result, tuple):
            print(f"Test failed for {machine} with a_count={a_count}, b_count={b_count}. \n{machine = }")
            raise Exception("Invalid return type")
        a_computed_count, b_computed_count = machine.get_a_b_press_count()
        assert a_computed_count == a_count and b_computed_count == b_count, f"Test failed for {machine} with a_count={a_count}, b_count={b_count}, a_computed_count={a_computed_count}, b_computed_count={b_computed_count}. \n{machine = }"
        print(f"Test {i} passed")


def test2(count: int):
    max_gen = 1000

    for i in range(count):
        machines = []
        expected_total_cost = 0
        machines_count = 0

        for machine_index in range(random.randint(1, 500)):
            a_count = random.randint(1, max_gen)
            b_count = random.randint(1, max_gen)

            a_x = random.randint(1, max_gen)
            a_y = random.randint(1, max_gen)
            b_x = random.randint(1, max_gen)
            b_y = random.randint(1, max_gen)

            prize_x = (a_count * a_x) + (b_count * b_x)
            prize_y = (a_count * a_y) + (b_count * b_y)

            machine = MachineSetup(P_x=prize_x,
                                   P_y=prize_y,
                                   a_x=a_x,
                                   a_y=a_y,
                                   b_x=b_x,
                                   b_y=b_y,
                                   test_injected_a_count=a_count,
                                   test_injected_b_count=b_count)

            machines.append(machine)
            expected_total_cost += (a_count * 3) + (b_count * 1)
            machines_count += 1

        computed_total_cost = day13_main(machines, part=1)
        assert computed_total_cost == expected_total_cost, f"Test failed expected_total_cost={expected_total_cost}, computed_total_cost={computed_total_cost}. {machines_count = } \n{machines = }"
        print(f"Test {i} passed")

if __name__ == '__main__':
    test1(count=500000)
    # test2(count=1000)
