import csv


def read_csv(filepath):
    x=[]
    with open(filepath,newline="") as csv_file:
        reader=csv.reader(csv_file)
        for row in reader:
            x.append(row)

    return x 


def mean(x):
    return sum(x)/len(x)

def mean(y):
    return sum(y)/len(y)    


def calc_corr(x,y):
    x_mean=mean(x)
    y_mean=mean(y)

    
    numerator=0
    denominator=0
    sum_x=0
    sum_y=0
    
    for x_i,y_i in zip(x,y):
        numerator+=(x_i-x_mean)*(y_i-y_mean)
       
    for x_i in x:
        print(x_i)
        sum_x+=(x_i-x_mean)**2

    for y_i in y:
        sum_y+=(y_i-y_mean)**2    

    denominator=(sum_x*sum_y)**0.5 

    corr=numerator/denominator
        

    return corr

file_1="2011_winners_raw.csv"
file_2="2011_winners_raw.csv"
X=read_csv(file_1)
Y=read_csv(file_2)

compiled_X={}
compiled_Y={}

for x,y in zip(X,Y):
    HDI_x=x[0]
    coal_y=y[0]
    compiled_X[HDI_x]=x[4]
    compiled_Y[coal_y]=y[5]

compiled_HDI=[]    
compiled_coal=[]

years=sorted(list(compiled_X.keys()))
for year in years:
    if year in compiled_Y:
        compiled_HDI.append(float(compiled_X[year]))
        compiled_coal.append(float(compiled_Y[year]))

print(calc_corr(compiled_HDI,compiled_coal))        
