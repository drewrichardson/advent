import requests
import os


def main():
    total = 0
    SESSION = os.environ.get('SESSION') 
    url = "https://adventofcode.com/2025/day/2/input"
    headers = {'Cookie': f"session={SESSION}"}
    r = requests.get(url, headers=headers)
    for range in r.text.split(','):
        parsed_range = parse_range(range)
        summed_repeats = sum_repeats(parsed_range) 
        total += summed_repeats
    print(total)


def parse_range(range_to_parse):
    parsed_range = range_to_parse.split("-")
    return parsed_range


def sum_repeats(parsed_range):
    sum_of_repeats = 0
    for num in range(int(parsed_range[0]), int(parsed_range[1])):
        str_num = str(num)
        if len(str_num) % 2 == 0:
            if str_num[0:int(len(str_num)/2)] == str_num[int(len(str_num)/2):]:
                sum_of_repeats += int(str_num)
    return sum_of_repeats


if __name__ == "__main__":
    main()