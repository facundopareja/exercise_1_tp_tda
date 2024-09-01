import sys
from parsers import parse_tasks_file, parse_earnings_file

BEST_RESULT = []
MAX_EARNINGS = 0

def calculate_earnings(tasks, earnings):
    total = 0
    for i, task in enumerate(tasks):
        total += earnings[task][i]
    return total

def available_tasks(tasks, required_tasks):
    for key, value in required_tasks.items():
        if key[0] not in tasks:
            for task in value:
                if task not in tasks:
                    return False
            return True
    return False


def required_tasks_done(tasks, task, required_tasks):
    for required_task in required_tasks[task]:
        if required_task not in tasks:
            return False
    return True


def calculate_earnings_for_task(task, earnings, week_number):
    return earnings[task[0]][week_number]


def backtrack(tasks, earnings, required_tasks, MAX_WEEKS):
    global MAX_EARNINGS, BEST_RESULT
    week_number = len(tasks)
    earnings_so_far = calculate_earnings(tasks, earnings)
    if week_number == MAX_WEEKS or not available_tasks(tasks, required_tasks):
        if earnings_so_far > MAX_EARNINGS:
            MAX_EARNINGS = earnings_so_far
            BEST_RESULT = tasks.copy()
    else:
        for task in required_tasks:
            if task[0] not in tasks and required_tasks_done(tasks, task, required_tasks):
                tasks.append(task[0])
                task_earnings = calculate_earnings_for_task(task, earnings, week_number)
                max_possible_earning = earnings_so_far + (MAX_WEEKS - week_number) * task_earnings
                if max_possible_earning > MAX_EARNINGS:
                    backtrack(tasks, earnings, required_tasks, MAX_WEEKS)
                tasks.pop()


def main():
    tasks = []
    required_tasks = parse_tasks_file(sys.argv[1])
    earnings = parse_earnings_file(sys.argv[2])
    MAX_WEEKS = 7
    backtrack(tasks, earnings, required_tasks, MAX_WEEKS)
    print(MAX_EARNINGS)
    print(BEST_RESULT)

main()