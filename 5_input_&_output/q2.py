# waf that replace all occurance of java to python in above file 
with open("practice.txt","r") as f:
    data=f.read()

    new_data=data.replace("java","python")
    print(new_data)

    with open("practice.txt","w")as f:
        f.write(new_data)