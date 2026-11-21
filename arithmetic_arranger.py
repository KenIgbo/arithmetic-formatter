def arithmetic_arranger(list_nums, boo = None):
    b = None
    m = []
    p = []

    if len(list_nums)>5:
        return('Error: Too many problems.')

    for s in list_nums:
        if '*' in s or '/' in s:
            return("Error: Operator must be '+' or '-'.")

        a = s[:s.index(' ')]
        if a.isdigit() is False:
            return('Error: Numbers must only contain digits.')
        if len(a)>4:
            return('Error: Numbers cannot be more than four digits.') 

        if '+' in s:
            b = s[s.index('+')+2:]
            if b.isdigit() is False:
                return('Error: Numbers must only contain digits.')
            if len(b)>4:
                return('Error: Numbers cannot be more than four digits.')

        if '-' in s:
            b = s[s.index('-')+2:]
            if b.isdigit() is False:
                return('Error: Numbers must only contain digits.')
            if len(b)>4:
                return('Error: Numbers cannot be more than four digits.')

        if len(a)>=len(b) and '+' in s:
            m.append('{:{width}}'.format(int(a), width = len(a)+2))
            p.append('{:{width}}'.format(int(a), width = len(a)+2))
            m.append('+'+'{:{width}}'.format(int(b), width = len(a)+1))
            p.append('+'+'{:{width}}'.format(int(b), width = len(a)+1))
            m.append('-'*(len(a)+2))
            p.append('-'*(len(a)+2))
            m.append('{:{width}}'.format((int(a)+int(b)), width = len(a)+2))

        if len(a)>=len(b) and '-' in s:
            m.append('{:{width}}'.format(int(a), width = len(a)+2))
            p.append('{:{width}}'.format(int(a), width = len(a)+2))
            m.append('-'+'{:{width}}'.format(int(b), width = len(a)+1))
            p.append('-'+'{:{width}}'.format(int(b), width = len(a)+1))
            m.append('-'*(len(a)+2))
            p.append('-'*(len(a)+2))
            m.append('{:{width}}'.format((int(a)-int(b)), width = len(a)+2))

        if len(b)>len(a) and '+' in s:
            m.append('{:{width}}'.format(int(a), width = len(b)+2))
            p.append('{:{width}}'.format(int(a), width = len(b)+2))
            m.append('+'+'{:{width}}'.format(int(b), width = len(b)+1))
            p.append('+'+'{:{width}}'.format(int(b), width = len(b)+1))
            m.append('-'*(len(b)+2))
            p.append('-'*(len(b)+2))
            m.append('{:{width}}'.format((int(a)+int(b)), width = len(b)+2))

        if len(b)>len(a) and '-' in s:
            m.append('{:{width}}'.format(int(a), width = len(b)+2))
            p.append('{:{width}}'.format(int(a), width = len(b)+2))
            m.append('-'+'{:{width}}'.format(int(b), width = len(b)+1))
            p.append('-'+'{:{width}}'.format(int(b), width = len(b)+1))
            m.append('-'*(len(b)+2))
            p.append('-'*(len(b)+2))
            m.append('{:{width}}'.format((int(a)-int(b)), width = len(b)+2))

    if boo is True:
        w = m[0]
        x = m[1]
        y = m[2]
        z = m[3]
        for i in range(4,len(m),4):
            w = w+(' '*4) + m[i]
        for i in range(5,len(m),4):
            x = x+(' '*4) + m[i]
        for i in range(6,len(m),4):
            y = y+(' '*4) + m[i]
        for i in range(7,len(m),4):
            z = z+(' '*4) + m[i]
        return(w + '\n' + x + '\n' + y + '\n' + z)

    else:
        x = p[0]
        y = p[1]
        z = p[2]
        for i in range(3,len(p),3):
            x = x+(' '*4) + p[i]
        for i in range(4,len(p),3):
            y = y+(' '*4) + p[i]
        for i in range(5,len(p),3):
            z = z+(' '*4) + p[i]
        return(x + '\n' + y + '\n' + z)
        
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
