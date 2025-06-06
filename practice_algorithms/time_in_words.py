def timeInWords(h, m):
    hour_mapping ={ # Also to be use with single-digit mapping 0-9
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve"
    }
    
    tens_mapping = {
            11: "eleven minutes",
            12: "twelve minutes",
            13: "thirteen minutes",
            14: "fourteen minutes",
            15: "quarter",
            16: "sixteen minutes",
            17: "seventeen minutes",
            18: "eighteen minutes",
            19: "nineteen minutes"
         }
         
    hour = hour_mapping[h]
    
    if m > 0 and m <= 9:
        minutes_past = hour_mapping[m]
    elif m >= 10 and m < 30:
        ones = m % 10
        tens = m // 10
        if tens == 1:
            minutes_past = tens_mapping[m]
        elif tens == 2:
            ones_str = hour_mapping[ones]
            minutes_past = f"twenty {ones_str} minutes"
    elif m == 30:
        return f"half past {hour}"
        
    elif m > 30 and m < 60:
        rem = 60 - m
        if rem > 0 and rem <= 9:
            minutes_to = hour_mapping[rem]
        if rem >= 10 and rem <= 29:
            ones = rem % 10
            tens = rem // 10
            if tens == 1:
                minutes_to = tens_mapping[rem]
            elif tens == 2:
                ones_str = hour_mapping[ones]
                minutes_to = f"twenty {ones_str} minutes"
            
    if m == 0:
        minutes_string = "o' clock"
        return f"{hour} {minutes_string}"
    elif m > 0 and m <= 9:
        minutes_string = 'past'
        if m == 1:
            return f"{minutes_past} minute {minutes_string} {hour}"
        return f"{minutes_past} minutes {minutes_string} {hour}"
    elif m < 30:
        minutes_string = 'past'
        return f"{minutes_past} {minutes_string} {hour}"
    elif m > 30:
        h2 = h + 1
        hour = hour_mapping[h2]
        minutes_string = 'to'
        if 60 - m > 0 and 60 - m <= 9:
            return f"{minutes_to} minutes {minutes_string} {hour}"
        return f"{minutes_to} {minutes_string} {hour}"
