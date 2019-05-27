def comma(list):
    ans = ""
    for item in range(len(list) - 2):
        ans += list[item] + ', '
    ans += list[-2] + ' and ' + list[-1]
    print(ans)

comma(['apple'])