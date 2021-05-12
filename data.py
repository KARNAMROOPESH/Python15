from os import name
import pandas as pd
import statistics
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

dataframe = pd.read_csv('./studentMarks.csv')
data = dataframe['Math_score'].tolist()
popmean = statistics.mean(data)
popstdev = statistics.stdev(data)
print('The Population mean is : ' , popmean )
print( 'The Population stdev is : ' , popstdev)

def ex():
    samplelist = []
    for i in range(100):
        index = random.randint(0,len(data)-1)
        value = data[index]
        samplelist.append(value)
    samplemean = statistics.mean(samplelist)
    return samplemean

samplemeandis = []

for i in range(1000):
    samplemean = ex()
    samplemeandis.append(samplemean)

mean = statistics.mean(samplemeandis)
sd = statistics.stdev(samplemeandis)

print('The Sampling mean distribution mean is : ' , mean)
print('The Sampling mean distribution stdev is : ' , sd)

fstart , fend = mean-sd , mean+sd 
sstart , send = mean-(2*sd) , mean+(2*sd)
tstart , tend = mean-(3*sd),mean+(3*sd)

fig = ff.create_distplot([samplemeandis] , ["Sampling Mean Distribution"] , show_hist= False)
fig.add_trace(go.Scatter(x = [mean , mean] , y = [ 0 , 0.2] , mode = "lines" , name = "MEAN"))
fig.add_trace(go.Scatter(x = [fstart , fstart] , y = [ 0 , 0.2] , mode = "lines" , name = "FIRST STDEV START"))
fig.add_trace(go.Scatter(x = [fend , fend] , y = [ 0 , 0.2] , mode = "lines" , name = "FIRST STDEV END"))
fig.add_trace(go.Scatter(x = [sstart , sstart] , y = [ 0 , 0.2] , mode = "lines" , name = "SECOND STDEV START"))
fig.add_trace(go.Scatter(x = [send , send] , y = [ 0 , 0.2] , mode = "lines" , name = "SECOND STDEV END"))
fig.add_trace(go.Scatter(x = [tstart , tstart] , y = [ 0 , 0.2] , mode = "lines" , name = "THIRD STDEV START"))
fig.add_trace(go.Scatter(x = [tend , tend] , y = [ 0 , 0.2] , mode = "lines" , name = "THIRD STDEV END"))

# studying effect of intervention 1 
df1 = pd.read_csv('./data1.csv')
d1 = df1['Math_score'].tolist()
mean1 = statistics.mean(d1)
print('The mean of intervention 1 is : ' , mean1)
zscore1 = ( mean1 - mean )/sd
print( ' The ZSCORE of intervention 1 is :' , zscore1)
fig.add_trace(go.Scatter(x = [mean1 , mean1] , y = [ 0 , 0.2] , mode = "lines" , name = "MEAN OF INTERVENTION 1"))


# studying effect of intervention 2
df2 = pd.read_csv('./data2.csv')
d2 = df2['Math_score'].tolist()
mean2 = statistics.mean(d2)
print('The mean of intervention 2 is : ' , mean2)
zscore2 = ( mean2 - mean)/sd
print( ' The ZSCORE of intervention 2 is :' , zscore2)
fig.add_trace(go.Scatter(x = [mean2 , mean2] , y = [ 0 , 0.2] , mode = "lines" , name = "MEAN OF INTERVENTION 2"))

# studying effect of intervention 3 
df3 = pd.read_csv('./data3.csv')
d3 = df3['Math_score'].tolist()
mean3 = statistics.mean(d3)
print('The mean of intervention 3 is : ' , mean3)
zscore3 = (mean3 - mean)/sd
print( ' The ZSCORE of intervention 3 is :' , zscore3)
fig.add_trace(go.Scatter(x = [mean3 , mean3] , y = [ 0 , 0.2] , mode = "lines" , name = "MEAN OF INTERVENTION 3"))

'''
fig.show()'''