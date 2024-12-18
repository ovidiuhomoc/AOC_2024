import multiprocessing

from day17_main import hardcoded_program


def worker3_optimized(task_queue: multiprocessing.Queue, result_dict):
    while True:
        try:
            task: tuple = task_queue.get()

            if isinstance(task, tuple):
                seed, target = task

                for i in range(100):
                    if result_dict[target]:
                        # solution already found. Pick up the next task
                        break

                    regA = seed + i
                    output_to_check = hardcoded_program(regA)
                    if output_to_check == target:
                        result_dict[target] = regA
                        break
            if result_dict['solution']:
                break
        except Exception as e:
            print(f"Error in worker: {e = }")
            break


def part2():
    manager = multiprocessing.Manager()
    queue = manager.Queue()
    shared_dict = manager.dict()

    shared_dict['solution'] = None

    workers_number = 20
    workers = [multiprocessing.Process(target=worker3_optimized, args=[queue, shared_dict]) for i in range(workers_number)]
    for w in workers:
        w.start()

    target_output = [2, 4, 1, 7, 7, 5, 4, 1, 1, 4, 5, 5, 0, 3, 3, 0]
    target_pointer = 1

    regA = 1

    while target_pointer <= len(target_output):
        temp_out_target: tuple = tuple(target_output[:target_pointer])

        shared_dict[temp_out_target] = None
        while not shared_dict[temp_out_target]:
            queue.put((regA, temp_out_target))
            regA += 100

        regA = shared_dict[temp_out_target]
        print(f"Fount solution ({regA = }) for {temp_out_target = }")

        target_pointer += 1
        regA = int(oct(regA) + "0", 8)

    print(regA)
    shared_dict['solution'] = True


if __name__ == '__main__':
    part2()
