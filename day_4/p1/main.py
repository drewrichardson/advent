import requests
import os

def main():
    SESSION = os.environ.get('SESSION')
    url = "https://adventofcode.com/2025/day/4/input"
    headers = {'Cookie': f"session={SESSION}"}
    r = requests.get(url, headers=headers)

    twod_array = r.text.split()
    # use this map to set the key of a point in the twodarray with the values of its neighbors
    num_rolls_accessible = 0
    for row, r_val in enumerate(twod_array):
        for c, c_val in enumerate(r_val):
            if twod_array[row][c] == '@':
                # if were not on the complete top or bottom of the twodarray
                if row != 0 and row != len(twod_array) - 1:
                    # if were not on the outer sides of the twodarray
                    if c != 0 and c != len(r_val) - 1:
                        left = check_left(r_val, c)
                        right = check_right(r_val, c)
                        up = check_up(twod_array, row, c)
                        down = check_down(twod_array, row, c)
                        topleft = check_tl(twod_array, row, c)
                        topright = check_tr(twod_array, row, c)
                        botleft = check_bl(twod_array, row, c)
                        botright = check_br(twod_array, row, c)
                        accessible = check_is_accessible(left, right, up, down, topleft, topright, botleft, botright)
                        if accessible:
                            num_rolls_accessible += 1
                    elif c == len(r_val) - 1:
                        left = check_left(r_val, c)
                        up = check_up(twod_array, row, c)
                        down = check_down(twod_array, row, c)
                        topleft = check_tl(twod_array, row, c)
                        botleft = check_bl(twod_array, row, c)
                        accessible = check_is_accessible(left, up, down, topleft, botleft)
                        if accessible:
                            num_rolls_accessible += 1
                    elif c == 0:
                        right = check_right(r_val, c)
                        up = check_up(twod_array, row, c)
                        down = check_down(twod_array, row, c)
                        topright = check_tr(twod_array, row, c)
                        botright = check_br(twod_array, row, c)
                        accessible = check_is_accessible(right, up, down, topright, botright)
                        if accessible:
                            num_rolls_accessible += 1
                elif row == 0:
                    if c != 0 and c != len(r_val) - 1:
                        left = check_left(r_val, c)
                        right = check_right(r_val, c)
                        down = check_down(twod_array, row, c)
                        botleft = check_bl(twod_array, row, c)
                        botright = check_br(twod_array, row, c)
                        accessible = check_is_accessible(left, right, down, botleft, botright)
                        if accessible:
                            num_rolls_accessible += 1
                    elif c == 0:
                        right = check_right(r_val, c)
                        down = check_down(twod_array, row, c)
                        botright = check_br(twod_array, row, c)
                        accessible = check_is_accessible(right, down, botright)
                        if accessible:
                            num_rolls_accessible += 1
                    elif c == len(r_val) - 1:
                        left = check_left(r_val, c)
                        down = check_down(twod_array, row, c)
                        botleft = check_bl(twod_array, row, c)
                        accessible = check_is_accessible(left, down, botleft)
                        if accessible:
                            num_rolls_accessible += 1
                elif row == len(twod_array) - 1:
                    if c != 0 and c != len(r_val) - 1:
                        left = check_left(r_val, c)
                        right = check_right(r_val, c)
                        up = check_up(twod_array, row, c)
                        topleft = check_tl(twod_array, row, c)
                        topright = check_tr(twod_array, row, c)
                        accessible = check_is_accessible(left, right, up, topleft, topright)
                        if accessible:
                            num_rolls_accessible += 1
                    elif c == 0:
                        right = check_right(r_val, c)
                        up = check_up(twod_array, row, c)
                        topright = check_tr(twod_array, row, c)
                        accessible = check_is_accessible(right, up, topright)
                        if accessible:
                            num_rolls_accessible += 1
                    elif c == len(r_val) - 1:
                        left = check_left(r_val, c)
                        up = check_up(twod_array, row, c)
                        topleft = check_tl(twod_array, row, c)
                        accessible = check_is_accessible(left, up, topleft)
                        if accessible:
                            num_rolls_accessible += 1

    print(num_rolls_accessible)
def check_left(row, col):
    return row[col - 1]

def check_right(row, col):
    return row[col + 1]

def check_up(twod_arr, row, col):
    return twod_arr[row-1][col]

def check_down(twod_arr, row, col):
    return twod_arr[row+1][col]

def check_tl(twod_arr, row, col):
    return twod_arr[row-1][col-1]

def check_tr(twod_arr, row, col):
    return twod_arr[row-1][col+1]

def check_br(twod_arr, row, col):
    return twod_arr[row+1][col+1]

def check_bl(twod_arr, row, col):
    return twod_arr[row+1][col-1]

def check_is_accessible(*args):
    total_rolls = 0
    for arg in args:
        if arg == '@':
            total_rolls  += 1
    return total_rolls < 4

if __name__ == "__main__":
    main()