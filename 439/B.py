n = int(input())

def happy_num(num, last_resu=0, numbs_seen=[]):
    result = 0
    numbs_seen.append(last_resu)
    num_list = [int(numb) for numb in str(num)]
    for numb in num_list:
        result += numb**2

    if result == 1:
        return "Yes"
    elif result in numbs_seen:
        return "No"
    else:
        return happy_num(result, result, numbs_seen)

print(happy_num(n))
