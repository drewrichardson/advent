import requests
import os

def main():
    total = 0
    SESSION = os.environ.get('SESSION')
    url = "https://adventofcode.com/2025/day/2/input"
    headers = {'Cookie': f"session={SESSION}"}
    
    r = requests.get(url, headers=headers)
    
    ranges = r.text.strip().split(',')
    
    for range_str in ranges:
        if not range_str.strip(): continue # Skip empty strings
        
        parsed_range = parse_range(range_str)
        summed_repeats = sum_repeats(parsed_range) 
        total += summed_repeats
        
    print(f"Total Sum: {total}")

def parse_range(range_to_parse):
    parts = range_to_parse.strip().split("-")
    return [int(parts[0]), int(parts[1])]

def sum_repeats(parsed_range):
    start = parsed_range[0]
    end = parsed_range[1]
    
    return sum_invalid_upto(end) - sum_invalid_upto(start - 1)


def sum_invalid_upto(limit):
    if limit < 11: return 0
    
    s_limit = str(limit)
    length = len(s_limit)
    total_sum = 0
    
    for l in range(2, length):
        total_sum += sum_invalid_for_fixed_length(l)
        
    total_sum += sum_invalid_limited(s_limit)
    
    return total_sum

def sum_invalid_for_fixed_length(L):
    divisors = [d for d in range(1, L) if L % d == 0]
    
    sum_roots_by_period = {}
    current_length_total_id_sum = 0
    
    for d in sorted(divisors):
        min_root = 10**(d-1)
        max_root = (10**d) - 1
        raw_sum = sum_arithmetic(min_root, max_root)
        
        primitive_root_sum = raw_sum
        for smaller_d in sum_roots_by_period:
            if d % smaller_d == 0:
                scale_mult = get_repetition_multiplier(smaller_d, d)
                overlap_sum = sum_roots_by_period[smaller_d] * scale_mult
                primitive_root_sum -= overlap_sum
        
        sum_roots_by_period[d] = primitive_root_sum
        
        final_mult = get_repetition_multiplier(d, L)
        current_length_total_id_sum += primitive_root_sum * final_mult
        
    return current_length_total_id_sum

def sum_invalid_limited(s_limit):
    L = len(s_limit)
    limit_val = int(s_limit)
    divisors = [d for d in range(1, L) if L % d == 0]
    
    sum_roots_by_period = {}
    total_found_sum = 0
    
    for d in sorted(divisors):
        prefix_str = s_limit[:d]
        prefix_val = int(prefix_str)
        start_val = 10**(d-1)
        
        raw_sum = sum_arithmetic(start_val, prefix_val - 1)
        
        repeated_val = int(prefix_str * (L // d))
        if repeated_val <= limit_val:
            raw_sum += prefix_val
            
        primitive_root_sum = raw_sum
        for smaller_d in sum_roots_by_period:
            if d % smaller_d == 0:
                scale_mult = get_repetition_multiplier(smaller_d, d)
                overlap_sum = sum_roots_by_period[smaller_d] * scale_mult
                primitive_root_sum -= overlap_sum
        
        sum_roots_by_period[d] = primitive_root_sum
        
        final_mult = get_repetition_multiplier(d, L)
        total_found_sum += primitive_root_sum * final_mult
        
    return total_found_sum

def sum_arithmetic(start, end):
    if start > end: return 0
    count = end - start + 1
    return (count * (start + end)) // 2

def get_repetition_multiplier(chunk_len, total_len):
    return (10**total_len - 1) // (10**chunk_len - 1)

if __name__ == "__main__":
    main()