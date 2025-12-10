import requests
import os

class Turn:
    def __init__(self, direction, count, full_turns):
        self.direction = direction
        self.count = int(count)
        self.full_turns = full_turns

class Dial:
    total_zerod_turns = 0
    def __init__(self, position=50):
        self.position = position
    
    def increment_zerod_turns(self, by_n=1):
        self.total_zerod_turns += by_n

def main():
    SESSION = os.environ.get('SESSION') 
    url = "https://adventofcode.com/2025/day/1/input"
    headers = {'Cookie': f"session={SESSION}"}
    r = requests.get(url, headers=headers)
    
    clean_text = r.text.replace(',', ' ')
    turn_list = clean_text.split()
    
    dial = Dial()
    
    for raw_turn in turn_list:
        turn_info = parse_turn(raw_turn)
        do_turn(turn_info, dial)
        
    print(dial.total_zerod_turns)

def parse_turn(turn):
    turn = turn.strip(',') 
    full_turns = int(int(turn[1:])/100)
    direction = turn[0]
    count = (int(turn[1:]) % 100) 
    return Turn(direction, count, full_turns)

def do_turn(turn, dial):
    if turn.full_turns > 0:
        dial.increment_zerod_turns(turn.full_turns)
        
    if turn.count == 0:
        if dial.position == 0:
            dial.increment_zerod_turns(1)
        return

    start_pos = dial.position
    
    if turn.direction == 'R':
        raw_pos = start_pos + turn.count

        if raw_pos > 100:
            dial.increment_zerod_turns(1)
            
        new_pos = raw_pos % 100
        dial.position = new_pos
        
        if new_pos == 0:
            dial.increment_zerod_turns(1)

    elif turn.direction == 'L':
        raw_pos = start_pos - turn.count
        
        if raw_pos < 0 and start_pos > 0:
            dial.increment_zerod_turns(1)
            
        if raw_pos < 0:
            new_pos = 100 + raw_pos
        else:
            new_pos = raw_pos
            
        dial.position = new_pos
        
        if new_pos == 0:
            dial.increment_zerod_turns(1)

if __name__ == "__main__":
    main()