def subSample(x,y):
    import numpy as np

    x_subset = []
    y_subset = []

    counter0 = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    counter7 = 0
    counter8 = 0
    counter9 = 0

    for i in range(len(y)):
        if (y[i]==0 and counter0<3000):
            counter0 = counter0 + 1
            x_subset.append(x[i])
            y_subset.append(y[i])
        elif (y[i]==1 and counter1<3000):
            counter1 = counter1 + 1
            x_subset.append(x[i])
            y_subset.append(y[i])
        elif (y[i]==2 and counter2<3000):
            counter2 = counter2 + 1
            x_subset.append(x[i])
            y_subset.append(y[i])
        elif (y[i]==3 and counter3<3000):
            counter3 = counter3 + 1
            x_subset.append(x[i])
            y_subset.append(y[i])
        elif (y[i]==4 and counter4<3000):
            counter4 = counter4 + 1
            x_subset.append(x[i])
            y_subset.append(y[i])
        elif (y[i]==5 and counter5<3000):
            counter5 = counter5 + 1
            x_subset.append(x[i])
            y_subset.append(y[i])
        elif (y[i]==6 and counter6<3000):
            counter6 = counter6 + 1
            x_subset.append(x[i])
            y_subset.append(y[i])
        elif (y[i]==7 and counter7<3000):
            counter7 = counter7 + 1
            x_subset.append(x[i])
            y_subset.append(y[i])
        elif (y[i]==8 and counter8<3000):
            counter8 = counter8 + 1
            x_subset.append(x[i])
            y_subset.append(y[i])
        elif (y[i]==9 and counter9<3000):
            counter9 = counter9 + 1
            x_subset.append(x[i])
            y_subset.append(y[i])
    return np.array(x_subset), np.array(y_subset)
