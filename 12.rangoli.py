def print_rangoli(size):
    # your code goes here
    smchr=97 # ASCII code for 'a'. for 'A' it is 65
    
    def print_line(i):
        t=[]
        for j in range(i,size): t.append( chr(smchr + j) )
        t = list(reversed(t)) + t[1:]
        centre, sides = "-".join(t), '--'*i
        print(sides+centre+sides)
        
    for i in reversed(range(size)): print_line(i)
    for i in range(1,size): print_line(i)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
