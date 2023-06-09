#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

x = 0
n1 = 1
n2 = 1
answer = 0
nextn = 0

while nextn < 4000000:  
        nextn = n1 + n2  
        n1 = n2  
        n2 = nextn  
        if nextn % 2 == 0:
            answer = answer + nextn
print(answer)

    
    