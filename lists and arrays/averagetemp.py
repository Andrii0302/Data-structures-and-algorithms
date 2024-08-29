days=int(input("Enter num of days: "))
iter=0
s=[]
while True:
    if iter==days: break
    a=int(input(f'Enter a temperature for day {iter+1}: '))
    s.append(a)
    iter+=1
avg=sum(s)/len(s)
print(f'The avg temp is {avg}')
for i in range(len(s)):
    if s[i] > avg:
        print(f"Day's {i+1} temp is above average: {s[i]}")

    
