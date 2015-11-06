attributes=0
datapoints=0
with open('/home/aditya/Desktop/Aditya/ML/assignment4/MLAssignment4/data/voting_test.data', 'rb') as file, open('/home/aditya/Desktop/Aditya/ML/assignment4/MLAssignment4/data/ignore_test.data', 'wb') as output_file:
    for line in file:
        datapoints+=1
        line=line.rstrip()
        temp=line.split(",")
        attributes=len(temp)
        fileprint=1
        for i in temp:
            if(i=='?'):
                fileprint=0
                break
        if fileprint==1:
            output_file.write(line)
            output_file.write('\r\n')

sumarr=[0 for i in range(attributes)]

with open('/home/aditya/Desktop/voting_test.data', 'rb') as file:
    for line in file:
        line=line.rstrip()
        temp=line.split(",")
        for i in range(attributes):
            sumarr[i]=sumarr[i]+ord(temp[i])-48


for i in range(len(sumarr)):
    sumarr[i]=sumarr[i]/datapoints
    if(sumarr[i]>1):
        sumarr[i]=1



with open('/home/aditya/Desktop/Aditya/ML/assignment4/MLAssignment4/data/voting_test.data', 'rb') as file, open('/home/aditya/Desktop/Aditya/ML/assignment4/MLAssignment4/data/mean_test.data', 'wb') as output_file:
    for line in file:
        line=line.rstrip()
        temp=line.split(",")
        fileprint=1
        for i in range(len(temp)):
            if(temp[i]=='?'):
                temp[i]=str(sumarr[i])
        output_file.write(",".join(temp))
        output_file.write('\r\n')
