from advent_of_code.helper_files.io_operations import get_input


def day_3_main():
    joltage_banks = get_input(file_path = 'inputs/day_3_input.txt')
    joltages = []
    unsafe_joltages = []
    for bank in joltage_banks:
        joltages.append(get_highest_joltage(bank))
        unsafe_joltages.append(get_highest_joltage_and_ignore_all_safety_protocol(bank))
    sum_of_joltages = sum(joltages)
    sum_of_unsafe_joltages = sum(unsafe_joltages)
    print(f'Day 3 part one: {sum_of_joltages}')
    print(f'Day 3 part two: {sum_of_unsafe_joltages}')


def get_highest_joltage(bank: str) -> int:
    battery_joltages = [int(x) for x in bank]
    left_battery = max(battery_joltages[:len(battery_joltages) - 1])
    left_battery_index = battery_joltages.index(left_battery)
    right_battery = max(battery_joltages[left_battery_index + 1:])
    max_joltage = int(f'{left_battery}{right_battery}')
    return max_joltage

def get_highest_joltage_and_ignore_all_safety_protocol(bank: str) -> int:
    remaining_joltages = [int(x) for x in bank]
    activated_joltages = []
    prev_battery_index = -1
    for i in range(12):
        reserved_indicies = len(remaining_joltages) - (11 - i)
        available_joltages = remaining_joltages[:reserved_indicies]
        value = max(available_joltages),
        prev_battery_index = available_joltages.index(value[0])
        activated_joltages.append(value[0])
        remaining_joltages = remaining_joltages[prev_battery_index+1:]
    
    max_joltage = "".join(str(jolt) for jolt in activated_joltages)
    return int(max_joltage)