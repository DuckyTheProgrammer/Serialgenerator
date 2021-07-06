import random
import string
import itertools

string = string.ascii_letters.upper()
example = ['X','X','-','000','-','X','X']
num_list=[]
n=15
t=list(itertools.permutations('123456789', 3))
def main():
    chosen = random.choices(string) + random.choices(string) + random.choices(string)  + random.choices(string)
    print(chosen)
    for i in range(4):
        example[0] = chosen[0]
        example[1] = chosen[1]
        example[5] = chosen[2]
        example[6] = chosen[3]
    
    for i in range(n):
        idx=random.randint(1,len(t)-1)
        k=''.join(str(e) for e in t[idx])

    num_list.append(k)
    print(num_list)
    example[3] = num_list[0]


    made = ''.join(example)
    print(made)
    print('successfully created txt file')
    with open('serial.txt', 'a+') as f:
        f.write(made+'\n')
    
main()
    