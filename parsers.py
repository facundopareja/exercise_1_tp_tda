def parse_tasks_file(filename):
    required_tasks = {}
    with open(filename, "r") as file:
        for line in file:
            split_line = line.split(',')
            required_tasks[(int(split_line[0]), split_line[1])] = convert_to_int(split_line[2::])
    return required_tasks

def parse_earnings_file(filename):
    potential_earnings = {}
    with open(filename, "r") as file:
        for line in file:
            split_line = line.split(',')
            potential_earnings[int(split_line[0])] = convert_to_int(split_line[1::])
    return potential_earnings

def convert_to_int(elements_list):
    for i, item in enumerate(elements_list):
        elements_list[i] = int(item)
    return elements_list