s = open('24/2025/77/69932.txt').readline().replace('**', '* *').replace('**', '* *').replace('--', '- -').replace('--','- -').replace('-*', '- *').replace('*-', '* -').split()
a = [x.strip('-').strip('*').rstrip('*').rstrip('-') for x in s if all(y not in x for y in ('-0', '0-', '*0', '0*'))]




m=max(a, key=len)

print(len(m))

print(m)
