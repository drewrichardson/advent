import requests
import os

def main():
    SESSION = os.environ.get('SESSION')
    url = "https://adventofcode.com/2025/day/3/input"
    headers = {'Cookie': f"session={SESSION}"}
    
    r = requests.get(url, headers=headers)
    total_joltage = 0
    for bank in r.text.split():
        total_joltage += find_max(bank)
    print(total_joltage)

def find_max(bank):
    high_num = max(bank)
    high_num_second_digit = 0
    bank_length = len(bank)-1
    if bank.index(high_num) == bank_length:
        bank_list = list(bank)
        high_num_second_digit = bank_list.pop()
        high_num = max(bank_list)
        return int(high_num + high_num_second_digit)
    else:
        return int(high_num + max(bank[bank.index(high_num)+1:]))
                

if __name__ == "__main__":
    main()