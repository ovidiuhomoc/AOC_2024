import multiprocessing
from typing import Literal

import day17


class Computer:
    def __init__(self, registerA: int, registerB: int, registerC: int, program: list[int]):
        assert isinstance(registerA, int), "Register A must be an integer."
        assert isinstance(registerB, int), "Register B must be an integer."
        assert isinstance(registerC, int), "Register C must be an integer."
        assert isinstance(program, list), "Program must be a list."
        assert program, "Program must not be empty."

        self._registerA = registerA
        self._registerB = registerB
        self._registerC = registerC

        self.program = program
        self._instruction_pointer = 0
        self.output = []
        self.last_instructions: list[tuple[int, int]] = []

    @property
    def registerA(self):
        return self._registerA

    @registerA.setter
    def registerA(self, value):
        self._registerA = int(value)

    @property
    def registerB(self):
        return self._registerB

    @registerB.setter
    def registerB(self, value):
        self._registerB = int(value)

    @property
    def registerC(self):
        return self._registerC

    @registerC.setter
    def registerC(self, value):
        self._registerC = int(value)

    def advance_to_next_instruction(self):
        self._instruction_pointer += 2

    @property
    def instruction_pointer(self):
        return self._instruction_pointer

    @instruction_pointer.setter
    def instruction_pointer(self, value):
        self._instruction_pointer = int(value)

    def combo_operand(self, operand: int):
        match operand:
            case v if 0 <= v <= 3:
                return operand
            case 4:
                return self.registerA
            case 5:
                return self.registerB
            case 6:
                return self.registerC
            case 7:
                raise ValueError("Operand 7 is not allowed. This is not a valid program.")

    def literal_operand(self, operand: int):
        assert 0 <= operand <= 7, f"Operand must be between 0 and 7. {operand = }"
        return operand

    def exec_instr(self):
        instruction = self.program[self.instruction_pointer]
        assert 0 <= instruction <= 7, f"Instruction must be between 0 and 7. {instruction = } | {self.instruction_pointer = } | program = " + " ".join(map(str, self.program))

        operand1 = None
        match instruction:
            case 0:
                # adv instruction
                operand1 = self.combo_operand(self.program[self.instruction_pointer + 1])
                self.adv(operand1)
            case 1:
                # bxl instruction
                operand1 = self.literal_operand(self.program[self.instruction_pointer + 1])
                self.bxl(operand1)
            case 2:
                # bst instruction
                operand1 = self.combo_operand(self.program[self.instruction_pointer + 1])
                self.bst(operand1)
            case 3:
                # jnz instruction
                operand1 = self.literal_operand(self.program[self.instruction_pointer + 1])
                self.jnz(operand1)
            case 4:
                # bxc instruction
                operand1 = self.literal_operand(self.program[self.instruction_pointer + 1])
                self.bxc(operand1)
            case 5:
                # out instruction
                operand1 = self.combo_operand(self.program[self.instruction_pointer + 1])
                self.out(operand1)
            case 6:
                # bdv instruction
                operand1 = self.combo_operand(self.program[self.instruction_pointer + 1])
                self.bdv(operand1)
            case 7:
                # cdv instruction
                operand1 = self.combo_operand(self.program[self.instruction_pointer + 1])
                self.cdv(operand1)

        self.last_instructions.append((instruction, operand1))
        # keep only the last 3 instructions
        self.last_instructions[:] = self.last_instructions[-3:]

    def run_program(self) -> list:
        while self.instruction_pointer < len(self.program):
            self.exec_instr()

            if len(self.last_instructions) >= 3 and self.last_instructions[-1] == self.last_instructions[-2] == self.last_instructions[-3] and self.last_instructions[-1][0] == 3:
                print()
                print(f"last 3 instructions are same and are jnz. breaking the loop.")
                break
        return self.output

    def _dv(self, operand1, dv_type: Literal["A", "B", "C"]):
        numerator = self.registerA
        denominator = 2 ** operand1

        result = int(numerator / denominator)
        match dv_type:
            case "A":
                self.registerA = result
            case "B":
                self.registerB = result
            case "C":
                self.registerC = result

    def adv(self, operand1):
        self._dv(operand1, "A")
        self.advance_to_next_instruction()

    def bdv(self, operand1):
        self._dv(operand1, "B")
        self.advance_to_next_instruction()

    def cdv(self, operand1):
        self._dv(operand1, "C")
        self.advance_to_next_instruction()

    def bxl(self, operand1):
        self.registerB = self.registerB ^ operand1
        self.advance_to_next_instruction()

    def bst(self, operand1):
        self.registerB = operand1 % 8
        self.advance_to_next_instruction()

    def jnz(self, operand1):
        if self.registerA == 0:
            return

        self.instruction_pointer = operand1

    def bxc(self, operand1):
        self.registerB = self.registerB ^ self.registerC
        self.advance_to_next_instruction()

    def out(self, operand1):
        result = operand1 % 8
        if not self.output:
            # not printed anything before
            print(result, end="")
        else:
            print(f",{result}", end="")
        self.output.append(result)
        self.advance_to_next_instruction()

# brute force seems not to work well in this way.
def worker(task_queue, result_dict, registerB: int, registerC: int, program: list[int], original_program: tuple, worker_id: int):
    while True:
        try:
            registerA_seed: int | None | str = task_queue.get()

            if registerA_seed == "STOP":
                break

            if isinstance(registerA_seed, int):
                print(f"(W{worker_id}) Check seed {registerA_seed}")

                threebitty = Computer(registerA=registerA_seed,
                                      registerB=registerB,
                                      registerC=registerC,
                                      program=program)
                program_output = tuple(threebitty.run_program())

                if program_output == original_program:
                    result_dict['solution'] = registerA_seed

            if result_dict['solution']:
                break
        except Exception as e:
            print(f"Error in worker: {e = }")
            break

# trying to hardcode the program at bitwise ops level. If this is too computationally expensive, will need to reverse the ops, start from the last one and find the way to the first one. Not recursive, but iterative.
def worker2_hardcoded_program(task_queue, result_dict, worker_id: int):
    while True:
        try:
            registerA_seed: int | None | str = task_queue.get()

            if registerA_seed == "STOP":
                break

            if isinstance(registerA_seed, int):
                hardcoded_original_program = (2, 4, 1, 7, 7, 5, 4, 1, 1, 4, 5, 5, 0, 3, 3, 0)

                for i in range(50):
                    regA = registerA_seed + i
                    output_to_check = hardcoded_program(regA)
                    if output_to_check == hardcoded_original_program:
                        result_dict['solution'] = registerA_seed + i
                        break
            if result_dict['solution']:
                break
        except Exception as e:
            print(f"Error in worker: {e = }")
            break


def hardcoded_program(regA) -> tuple[int, ...]:
    regB = 0
    regC = 0

    out = []
    while regA:
        # op. 0  -> bst 2 4
        regB = regA & 7

        # op. 1  -> bxl 1 7
        regB = regB ^ 7

        # op. 2  -> cdv 7 5
        regC = regA >> regB

        # op. 3  -> bxc 4 1
        regB = regB ^ regC

        # op. 4  -> bxl 1 4
        regB = regB ^ 4

        # op. 5  -> out 5 5
        out.append(regB & 7)

        # op. 6  -> adv 0 3
        regA = regA >> 3

    return tuple(out)


def main(input, part):
    registers_str = input.split('\n\n')[0].strip()
    registers: list[int] = []
    for line in registers_str.splitlines():
        value = int(line.split(': ')[1].strip())
        registers.append(value)

    program_str = input.split('\n\n')[1].strip()
    program: list[int] = list(map(int, program_str.split('Program: ')[1].strip().split(',')))

    if part == 1:
        threebitty = Computer(registerA=registers[0],
                              registerB=registers[1],
                              registerC=registers[2],
                              program=program)

        output: list = threebitty.run_program()

        print("Resulted output = ", ','.join(map(str, output)))
    else:
        original_program: tuple[int, ...] = tuple(i for i in program)
        program_output: tuple[int, ...] = tuple()

        registerA_seed = 351545604

        manager = multiprocessing.Manager()
        queue = manager.Queue()
        shared_dict = manager.dict()

        shared_dict['solution'] = None

        workers_number = 20
        workers = [multiprocessing.Process(target=worker2_hardcoded_program, args=[queue, shared_dict, i]) for i in range(workers_number)]
        for w in workers:
            w.start()

        while not shared_dict['solution']:
            queue.put(registerA_seed)
            registerA_seed += 50

        print(f"============================= {shared_dict['solution'] = } =============================")


if __name__ == '__main__':
    dinput = day17.demoinput
    dinput2 = day17.demoinput2
    dinput3 = day17.demoinput3
    dinput4 = day17.demoinput4
    dinput5 = day17.demoinput5
    dinput6 = day17.demoinput6
    dinput7 = day17.demoinput7
    input1 = day17.input1

    # main(dinput, part=1)
    # print()
    # print()
    # main(dinput2, part=1)
    # print()
    # print()
    # main(dinput3, part=1)
    # print()
    # print()
    # main(dinput4, part=1)
    # print()
    # print()
    # main(dinput5, part=1)
    # print()
    # print()
    # main(dinput6, part=1)
    # print()
    # print()
    # main(input1, part=1)
    # main(dinput7, part=2)
    main(input1, part=2)
