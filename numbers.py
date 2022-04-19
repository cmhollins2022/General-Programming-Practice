def sum_mix(arr):
    new_list = []
    for x in arr:
        if type(x) == str:
            converted_x = int(x)
            new_list.append(converted_x)
        elif type(x) == int:
            new_list.append(x)
            continue

    return print(sum(new_list))


sum_mix(['2', 3, 4, 5])
