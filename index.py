from matplotlib import pyplot as plt
from scipy import stats
import json
f = open('./students_marks.json')


items = json.load(f)




for student in items['students']:
    Y= student['grades']
    X = []
    n = 0
    for i in student['grades']:
        X.insert(n,n)
        n+=1
    slope, intercept, r, p, std_err = stats.linregress(X,Y)
    def myFunc(x):
        prediction = slope*x + intercept
        if prediction > 5.0:
            prediction = 5.0
        
        return prediction
    mymodel = list(map(myFunc, X))
    fourth = myFunc(3)
        
    print(student['name']+' will get '+ str(fourth) + ' points out of 5.0 in the next exam')

    plt.scatter(X,Y)
    plt.figure(student['name'])
    plt.plot(X, mymodel)
    
plt.show()


