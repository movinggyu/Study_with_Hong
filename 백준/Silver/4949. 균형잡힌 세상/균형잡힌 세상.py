import sys
sts = sys.stdin.readline()
while sts!=".":
    gwalho = []
    for i in sts:
        if i == '(':
            gwalho.append('(')
        elif i == ')':
            if not gwalho:
                gwalho.append(')')
                break
            else:
                gwalho.pop() if gwalho[-1]=='(' else gwalho.append(')')
        elif i == '[':
            gwalho.append('[')
        elif i == ']':
            if not gwalho:
                gwalho.append(']')
                break
            else:
                gwalho.pop() if gwalho[-1]=='[' else gwalho.append(']')
    print("no" if gwalho else "yes")
    sts = sys.stdin.readline().rstrip()
