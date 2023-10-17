
import flag


for i in range(len(flag)):
    print(ord(flag[i])^ord(flag[(i+1)%len(flag)]),end="\n")
'''54
0
48
54
23
18
29
24
35
46
49
38
73
69
42
42
6
22
58
47
9
38
39
72
66
15
46'''
