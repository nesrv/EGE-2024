for x in range(397438, 443520 + 1):
    dividers = set()
    for d in range(2,x//2+1, 2):
        if x % d == 0:
            dividers.add(d)           
    len_dividers =  len(dividers)       
    if len_dividers >=142:
        print(len_dividers, max(dividers))


"""
143 201600
143 205920
143 207900
143 211680
143 214200
143 218400
167 221760

"""
