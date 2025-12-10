import requests
import os

class Turn:
    def __init__(self, direction, count):
        self.direction = direction
        self.count = int(count)

class Dial:
    total_zerod_turns = 0
    def __init__(self, position=50):
        self.position = position
    
    def increment_zerod_turns(self):
        self.total_zerod_turns += 1
        

def main():
    SESSION = os.environ.get('SESSION') 
    url = "https://adventofcode.com/2025/day/1/input"
    headers = {'Cookie': f"session={SESSION}"}
    r = requests.get(url, headers=headers)
    turn_list = r.text.split()
    dial = Dial()
    short_turn_list = turn_list[:50]
    for raw_turn in turn_list:
        turn_info = parse_turn(raw_turn)
        do_turn(turn_info, dial)
    print(dial.total_zerod_turns)
        

def parse_turn(turn):
    direction = turn[0]
    count = (int(turn[1:]) % 100) 
    return Turn(direction, count)


def do_turn(turn, dial):
    print(f"{turn.direction}, {int(turn.count)}, on curr position {dial.position}")

    if turn.direction == 'L':
        new_pos = dial.position - turn.count
        if new_pos == 0:
            dial.increment_zerod_turns()
            dial.position = 0
            return
        if new_pos < 0:
            dial.position = (100 + new_pos)
            return
        dial.position = new_pos
    if turn.direction == 'R':
        new_pos = (dial.position + turn.count) % 100
        if new_pos == 0:
            dial.increment_zerod_turns()
            dial.position = 0
            return
        if new_pos > 99:
            dial.position = (0 + new_pos)
            return
        dial.position = new_pos        


if __name__ == "__main__":
    main()
