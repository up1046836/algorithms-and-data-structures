from task import Task

guard = Task('guard', 0, 0, 0, 0)

tasks = [
        Task('a', 1, 3, 5), 
        Task('b', 1, 2, 3),
        Task('c', 2, 3, 3)
]

def find_predecessors(tasks):
    number_of_tasks = len(tasks)
    tasks_sorted_by_finish = sorted(tasks + [guard], key=lambda task: task.finish)
    tasks_sorted_by_start = sorted(tasks + [guard], key=lambda task: task.start)
    merged = []

    i = j = number_of_tasks
    for n in range(2*number_of_tasks):
        if tasks_sorted_by_finish[i].finish > tasks_sorted_by_start[j].start:
            merged.append((tasks_sorted_by_finish[i], 'e'))
            i -= 1
        else:
            merged.append((tasks_sorted_by_start[j], 's'))
            j -= 1

    predecessor_index = 0
    for entry in reversed(merged):
        if entry[1] == 'e':
            predecessor_index += 1
        else:
            entry[0].predecessor_index = predecessor_index

    return tasks

def schedule(tasks):
    tasks_sorted_by_finish = sorted(tasks, key=lambda task: task.finish)
    max_benefit = [0]
    for index, task in enumerate(tasks_sorted_by_finish):
        include_task_benefit = task.value + max_benefit[task.predecessor_index]
        ignore_task_benefit = max_benefit[index]
        max_benefit.append(max(include_task_benefit, ignore_task_benefit))

    index = len(tasks)
    solution = []
    while index > 0:
        if max_benefit[index] > max_benefit[index-1]:
            task = tasks_sorted_by_finish[index-1]
            index = task.predecessor_index
            solution.append(task)
        else:
            index -= 1

    return list(reversed(solution))

find_predecessors(tasks)
solution = schedule(tasks)
print(solution)
