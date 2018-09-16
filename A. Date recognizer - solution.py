import re
a = input()
m = 0
res = re.split(r'\.', a)
if len(res) == 3:
    if 1 <= int(res[0]) <= 12:
        m = int(res[0])
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if 1 <= int(res[1]) <= 31 and (len(res[2]) == 2 or len(res[2]) == 4):
                print('yes')
            elif 1 <= int(res[2]) <= 31 and (len(res[1]) == 2 or len(res[1]) == 4):
                print('yes')
            else:
                print('no')
        elif m == 4 or m == 6 or m == 9 or m == 11:
            if 1 <= int(res[1]) <= 30 and (len(res[2]) == 2 or len(res[2]) == 4):
                print('yes')
            elif 1 <= int(res[2]) <= 30 and (len(res[1]) == 2 or len(res[1]) == 4):
                print('yes')
            else:
                print('no')
        elif m == 2:
            if 1 <= int(res[1]) <= 28 and (len(res[2]) == 2 or len(res[2]) == 4):
                print('yes')
            elif 1 <= int(res[2]) <= 28 and (len(res[1]) == 2 or len(res[1]) == 4):
                print('yes')
            else:
                print('no')        
    elif 1 <= int(res[1]) <= 12:
        m = int(res[1])
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if 1 <= int(res[0]) <= 31 and (len(res[2]) == 2 or len(res[2]) == 4):
                print('yes')
            elif 1 <= int(res[2]) <= 31 and (len(res[0]) == 2 or len(res[0]) == 4):
                print('yes')
            else:
                print('no')
        elif m == 4 or m == 6 or m == 9 or m == 11:
            if 1 <= int(res[0]) <= 30 and (len(res[2]) == 2 or len(res[2]) == 4):
                print('yes')
            elif 1 <= int(res[2]) <= 30 and (len(res[0]) == 2 or len(res[0]) == 4):
                print('yes')
            else:
                print('no')
        elif m == 2:
            if 1 <= int(res[0]) <= 28 and (len(res[2]) == 2 or len(res[2]) == 4):
                print('yes')
            elif 1 <= int(res[2]) <= 28 and (len(res[0]) == 2 or len(res[0]) == 4):
                print('yes')
            else:
                print('no')                
    elif 1 <= int(res[2]) <= 12:
        m = int(res[2])
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if 1 <= int(res[0]) <= 31 and (len(res[1]) == 2 or len(res[1]) == 4):
                print('yes')
            elif 1 <= int(res[1]) <= 31 and (len(res[0]) == 2 or len(res[0]) == 4):
                print('yes')
            else:
                print('no')
        elif m == 4 or m == 6 or m == 9 or m == 11:
            if 1 <= int(res[0]) <= 30 and (len(res[1]) == 2 or len(res[1]) == 4):
                print('yes')
            elif 1 <= int(res[1]) <= 30 and (len(res[0]) == 2 or len(res[0]) == 4):
                print('yes')
            else:
                print('no')
        elif m == 2:
            if 1 <= int(res[0]) <= 28 and (len(res[1]) == 2 or len(res[1]) == 4):
                print('yes')
            elif 1 <= int(res[1]) <= 28 and (len(res[0]) == 2 or len(res[0]) == 4):
                print('yes')
            else:
                print('no')         
    else:
        print('no')
    if m != 0:
        print('yes')
else:
    res = re.split(r'\/', a)
    if len(res) == 3:
        if 1 <= int(res[0]) <= 12:
            m = int(res[0])
            if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                if 1 <= int(res[1]) <= 31 and (len(res[2]) == 2 or len(res[2]) == 4):
                    print('yes')
                elif 1 <= int(res[2]) <= 31 and (len(res[1]) == 2 or len(res[1]) == 4):
                    print('yes')
                else:
                    print('no')
            elif m == 4 or m == 6 or m == 9 or m == 11:
                if 1 <= int(res[1]) <= 30 and (len(res[2]) == 2 or len(res[2]) == 4):
                    print('yes')
                elif 1 <= int(res[2]) <= 30 and (len(res[1]) == 2 or len(res[1]) == 4):
                    print('yes')
                else:
                    print('no')
            elif m == 2:
                if 1 <= int(res[1]) <= 28 and (len(res[2]) == 2 or len(res[2]) == 4):
                    print('yes')
                elif 1 <= int(res[2]) <= 28 and (len(res[1]) == 2 or len(res[1]) == 4):
                    print('yes')
                else:
                    print('no')        
        elif 1 <= int(res[1]) <= 12:
            m = int(res[1])
            if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                if 1 <= int(res[0]) <= 31 and (len(res[2]) == 2 or len(res[2]) == 4):
                    print('yes')
                elif 1 <= int(res[2]) <= 31 and (len(res[0]) == 2 or len(res[0]) == 4):
                    print('yes')
                else:
                    print('no')
            elif m == 4 or m == 6 or m == 9 or m == 11:
                if 1 <= int(res[0]) <= 30 and (len(res[2]) == 2 or len(res[2]) == 4):
                    print('yes')
                elif 1 <= int(res[2]) <= 30 and (len(res[0]) == 2 or len(res[0]) == 4):
                    print('yes')
                else:
                    print('no')
            elif m == 2:
                if 1 <= int(res[0]) <= 28 and (len(res[2]) == 2 or len(res[2]) == 4):
                    print('yes')
                elif 1 <= int(res[2]) <= 28 and (len(res[0]) == 2 or len(res[0]) == 4):
                    print('yes')
                else:
                    print('no')                
        elif 1 <= int(res[2]) <= 12:
            m = int(res[2])
            if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                if 1 <= int(res[0]) <= 31 and (len(res[1]) == 2 or len(res[1]) == 4):
                    print('yes')
                elif 1 <= int(res[1]) <= 31 and (len(res[0]) == 2 or len(res[0]) == 4):
                    print('yes')
                else:
                    print('no')
            elif m == 4 or m == 6 or m == 9 or m == 11:
                if 1 <= int(res[0]) <= 30 and (len(res[1]) == 2 or len(res[1]) == 4):
                    print('yes')
                elif 1 <= int(res[1]) <= 30 and (len(res[0]) == 2 or len(res[0]) == 4):
                    print('yes')
                else:
                    print('no')
            elif m == 2:
                if 1 <= int(res[0]) <= 28 and (len(res[1]) == 2 or len(res[1]) == 4):
                    print('yes')
                elif 1 <= int(res[1]) <= 28 and (len(res[0]) == 2 or len(res[0]) == 4):
                    print('yes')
                else:
                    print('no')         
        else:
            print('no')
        if m != 0:
            print('yes')
    else:
        res = re.split(r'\\', a)
        if len(res) == 3:
            if 1 <= int(res[0]) <= 12:
                m = int(res[0])
                if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                    if 1 <= int(res[1]) <= 31 and (len(res[2]) == 2 or len(res[2]) == 4):
                        print('yes')
                    elif 1 <= int(res[2]) <= 31 and (len(res[1]) == 2 or len(res[1]) == 4):
                        print('yes')
                    else:
                        print('no')
                elif m == 4 or m == 6 or m == 9 or m == 11:
                    if 1 <= int(res[1]) <= 30 and (len(res[2]) == 2 or len(res[2]) == 4):
                        print('yes')
                    elif 1 <= int(res[2]) <= 30 and (len(res[1]) == 2 or len(res[1]) == 4):
                        print('yes')
                    else:
                        print('no')
                elif m == 2:
                    if 1 <= int(res[1]) <= 28 and (len(res[2]) == 2 or len(res[2]) == 4):
                        print('yes')
                    elif 1 <= int(res[2]) <= 28 and (len(res[1]) == 2 or len(res[1]) == 4):
                        print('yes')
                    else:
                        print('no')        
            elif 1 <= int(res[1]) <= 12:
                m = int(res[1])
                if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                    if 1 <= int(res[0]) <= 31 and (len(res[2]) == 2 or len(res[2]) == 4):
                        print('yes')
                    elif 1 <= int(res[2]) <= 31 and (len(res[0]) == 2 or len(res[0]) == 4):
                        print('yes')
                    else:
                        print('no')
                elif m == 4 or m == 6 or m == 9 or m == 11:
                    if 1 <= int(res[0]) <= 30 and (len(res[2]) == 2 or len(res[2]) == 4):
                        print('yes')
                    elif 1 <= int(res[2]) <= 30 and (len(res[0]) == 2 or len(res[0]) == 4):
                        print('yes')
                    else:
                        print('no')
                elif m == 2:
                    if 1 <= int(res[0]) <= 28 and (len(res[2]) == 2 or len(res[2]) == 4):
                        print('yes')
                    elif 1 <= int(res[2]) <= 28 and (len(res[0]) == 2 or len(res[0]) == 4):
                        print('yes')
                    else:
                        print('no')                
            elif 1 <= int(res[2]) <= 12:
                m = int(res[2])
                if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                    if 1 <= int(res[0]) <= 31 and (len(res[1]) == 2 or len(res[1]) == 4):
                        print('yes')
                    elif 1 <= int(res[1]) <= 31 and (len(res[0]) == 2 or len(res[0]) == 4):
                        print('yes')
                    else:
                        print('no')
                elif m == 4 or m == 6 or m == 9 or m == 11:
                    if 1 <= int(res[0]) <= 30 and (len(res[1]) == 2 or len(res[1]) == 4):
                        print('yes')
                    elif 1 <= int(res[1]) <= 30 and (len(res[0]) == 2 or len(res[0]) == 4):
                        print('yes')
                    else:
                        print('no')
                elif m == 2:
                    if 1 <= int(res[0]) <= 28 and (len(res[1]) == 2 or len(res[1]) == 4):
                        print('yes')
                    elif 1 <= int(res[1]) <= 28 and (len(res[0]) == 2 or len(res[0]) == 4):
                        print('yes')
                    else:
                        print('no')         
            else:
                print('no')
            if m != 0:
                print('yes')
        else:
            res = re.split(r' ', a)
            if len(res) == 3:
                if 1 <= int(res[0]) <= 12:
                    m = int(res[0])
                    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                        if 1 <= int(res[1]) <= 31 and (len(res[2]) == 2 or len(res[2]) == 4):
                            print('yes')
                        elif 1 <= int(res[2]) <= 31 and (len(res[1]) == 2 or len(res[1]) == 4):
                            print('yes')
                        else:
                            print('no')
                    elif m == 4 or m == 6 or m == 9 or m == 11:
                        if 1 <= int(res[1]) <= 30 and (len(res[2]) == 2 or len(res[2]) == 4):
                            print('yes')
                        elif 1 <= int(res[2]) <= 30 and (len(res[1]) == 2 or len(res[1]) == 4):
                            print('yes')
                        else:
                            print('no')
                    elif m == 2:
                        if 1 <= int(res[1]) <= 28 and (len(res[2]) == 2 or len(res[2]) == 4):
                            print('yes')
                        elif 1 <= int(res[2]) <= 28 and (len(res[1]) == 2 or len(res[1]) == 4):
                            print('yes')
                        else:
                            print('no')        
                elif 1 <= int(res[1]) <= 12:
                    m = int(res[1])
                    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                        if 1 <= int(res[0]) <= 31 and (len(res[2]) == 2 or len(res[2]) == 4):
                            print('yes')
                        elif 1 <= int(res[2]) <= 31 and (len(res[0]) == 2 or len(res[0]) == 4):
                            print('yes')
                        else:
                            print('no')
                    elif m == 4 or m == 6 or m == 9 or m == 11:
                        if 1 <= int(res[0]) <= 30 and (len(res[2]) == 2 or len(res[2]) == 4):
                            print('yes')
                        elif 1 <= int(res[2]) <= 30 and (len(res[0]) == 2 or len(res[0]) == 4):
                            print('yes')
                        else:
                            print('no')
                    elif m == 2:
                        if 1 <= int(res[0]) <= 28 and (len(res[2]) == 2 or len(res[2]) == 4):
                            print('yes')
                        elif 1 <= int(res[2]) <= 28 and (len(res[0]) == 2 or len(res[0]) == 4):
                            print('yes')
                        else:
                            print('no')                
                elif 1 <= int(res[2]) <= 12:
                    m = int(res[2])
                    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                        if 1 <= int(res[0]) <= 31 and (len(res[1]) == 2 or len(res[1]) == 4):
                            print('yes')
                        elif 1 <= int(res[1]) <= 31 and (len(res[0]) == 2 or len(res[0]) == 4):
                            print('yes')
                        else:
                            print('no')
                    elif m == 4 or m == 6 or m == 9 or m == 11:
                        if 1 <= int(res[0]) <= 30 and (len(res[1]) == 2 or len(res[1]) == 4):
                            print('yes')
                        elif 1 <= int(res[1]) <= 30 and (len(res[0]) == 2 or len(res[0]) == 4):
                            print('yes')
                        else:
                            print('no')
                    elif m == 2:
                        if 1 <= int(res[0]) <= 28 and (len(res[1]) == 2 or len(res[1]) == 4):
                            print('yes')
                        elif 1 <= int(res[1]) <= 28 and (len(res[0]) == 2 or len(res[0]) == 4):
                            print('yes')
                        else:
                            print('no')         
                else:
                    print('no')
                if m != 0:
                    print('yes')
            else:
                res = re.split(r'-', a)
                if len(res) == 3:
                    if 1 <= int(res[0]) <= 12:
                        m = int(res[0])
                        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                            if 1 <= int(res[1]) <= 31 and (len(res[2]) == 2 or len(res[2]) == 4):
                                print('yes')
                            elif 1 <= int(res[2]) <= 31 and (len(res[1]) == 2 or len(res[1]) == 4):
                                print('yes')
                            else:
                                print('no')
                        elif m == 4 or m == 6 or m == 9 or m == 11:
                            if 1 <= int(res[1]) <= 30 and (len(res[2]) == 2 or len(res[2]) == 4):
                                print('yes')
                            elif 1 <= int(res[2]) <= 30 and (len(res[1]) == 2 or len(res[1]) == 4):
                                print('yes')
                            else:
                                print('no')
                        elif m == 2:
                            if 1 <= int(res[1]) <= 28 and (len(res[2]) == 2 or len(res[2]) == 4):
                                print('yes')
                            elif 1 <= int(res[2]) <= 28 and (len(res[1]) == 2 or len(res[1]) == 4):
                                print('yes')
                            else:
                                print('no')        
                    elif 1 <= int(res[1]) <= 12:
                        m = int(res[1])
                        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                            if 1 <= int(res[0]) <= 31 and (len(res[2]) == 2 or len(res[2]) == 4):
                                print('yes')
                            elif 1 <= int(res[2]) <= 31 and (len(res[0]) == 2 or len(res[0]) == 4):
                                print('yes')
                            else:
                                print('no')
                        elif m == 4 or m == 6 or m == 9 or m == 11:
                            if 1 <= int(res[0]) <= 30 and (len(res[2]) == 2 or len(res[2]) == 4):
                                print('yes')
                            elif 1 <= int(res[2]) <= 30 and (len(res[0]) == 2 or len(res[0]) == 4):
                                print('yes')
                            else:
                                print('no')
                        elif m == 2:
                            if 1 <= int(res[0]) <= 28 and (len(res[2]) == 2 or len(res[2]) == 4):
                                print('yes')
                            elif 1 <= int(res[2]) <= 28 and (len(res[0]) == 2 or len(res[0]) == 4):
                                print('yes')
                            else:
                                print('no')                
                    elif 1 <= int(res[2]) <= 12:
                        m = int(res[2])
                        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                            if 1 <= int(res[0]) <= 31 and (len(res[1]) == 2 or len(res[1]) == 4):
                                print('yes')
                            elif 1 <= int(res[1]) <= 31 and (len(res[0]) == 2 or len(res[0]) == 4):
                                print('yes')
                            else:
                                print('no')
                        elif m == 4 or m == 6 or m == 9 or m == 11:
                            if 1 <= int(res[0]) <= 30 and (len(res[1]) == 2 or len(res[1]) == 4):
                                print('yes')
                            elif 1 <= int(res[1]) <= 30 and (len(res[0]) == 2 or len(res[0]) == 4):
                                print('yes')
                            else:
                                print('no')
                        elif m == 2:
                            if 1 <= int(res[0]) <= 28 and (len(res[1]) == 2 or len(res[1]) == 4):
                                print('yes')
                            elif 1 <= int(res[1]) <= 28 and (len(res[0]) == 2 or len(res[0]) == 4):
                                print('yes')
                            else:
                                print('no')         
                    else:
                        print('no')
                    if m != 0:
                        print('yes')
                else:
                    print('no')
#Used '.', '/', '\', ' ', '-' as possible separators. Checked if there are 3 separated numbers and if any of them can be a month, then cheked if one of the rest can be a date of the given month, considering there are always 28 days in February. Then checked, if the last number has 2 or 4 digits and therefore can be a year. 
