
print('\x1B[38;2;0;255;0m')
print(f"{"|"}{'-'*43}{"|"} ", end = '')
print('\x1B[38;2;255;255;0m')
print(f"| {'A':^2}  {'B':^3}  {'A&B':^3} {'A|B':^5} {'~A':^5} {'~B':^5} {'A>>B':^5} {'A<<B':^5}|", end = '')
print('\x1B[38;2;0;255;0m')
print(f"{"|"}{'-'*43}{"|"} ", end = '')
for a in range(0,2):
    for b in range(0,2):
        print('\x1B[38;2;255;0;0m')
        print(f"|{a:^3}  {b:^3}   {a&b:^2} {a|b:^5} {~a:^4} {~b:^6} {a>>b:^4} {a<<b:^6}|", end = '')
        print('\x1B[38;2;0;0;255m')
        print('|' + '_' * 43 +   "|", end = '')
