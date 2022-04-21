def make_upper_case(s: str):
    s = s.split()
    for item in s:
        if item.lower():
            item.upper()
            
    return print(s)


make_upper_case('stop')
