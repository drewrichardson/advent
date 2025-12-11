import requests
import os

def main():
    SESSION = os.environ.get('SESSION')
    url = "https://adventofcode.com/2025/day/3/input"
    headers = {'Cookie': f"session={SESSION}"}
    
    r = requests.get(url, headers=headers)
    total_joltage = 0
    # find_max(r.text.split()[0])
    for bank in r.text.split():
        total = find_max(bank)
        print(total)
        total_joltage += total

    print(total_joltage)
### we now need to find the max of with 12 digits instead of two, 
### there is probably a mathy or graph way to handle this, but I'm
### instead going to do a max, and if it's 12 away from the end,
### we'll use it. Else will continue working backwards while keeping the highest
### 
# 5373475263753258336423442254746263332334232217334431337464342726873125223932312363675175435324343745


def find_max(bank):
    joltage = ""
    high_num = 0
    high_num_index = 0
    temp_bank = ""
    while len(joltage) < 12:
        high_num = max(bank)
        high_num_index = bank.find(high_num)
        if temp_bank:
            bank += temp_bank
            temp_bank = ""
        if len(bank) - high_num_index >= 12 - len(joltage):
            joltage += high_num
            bank = bank[high_num_index+1:]
        else:
            temp_bank = bank[high_num_index:]
            bank = bank[:high_num_index]
    return int(joltage)

if __name__ == "__main__":
    main()