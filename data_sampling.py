import pandas as pd
import statistics
import  csv
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go
# reading the file
df = pd.read_csv("data_temp.csv")
data = df["temp"].tolist()
# finding mean
population_mean = statistics.mean(data)
std_dev = statistics.stdev(data)
# print(std_dev, population_mean)
# fig = ff.create_distplot([data],["temp"],show_hist=False)
# fig.show()

# dataset = []
# for i in range(0,100):
#     randomIndex = random.randint(0,len(data))
#     value =data[randomIndex]
#     dataset.append(value)

# dataset_mean = statistics.mean(dataset)
# dataset_std_dev = statistics.stdev(dataset)
# print(dataset_mean, dataset_std_dev)

def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data))
        value = data[randomIndex]
        dataset.append(value)

    dataset_mean = statistics.mean(dataset)

    return dataset_mean

def showFigure(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    # fig = fig.add_trace(go.scatter(x=[mean_list,mean_list], y =[0,1], mode ="lines"))
    fig.show()
   

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = randomSetOfMean(100)
        mean_list.append(set_of_mean)
    showFigure(mean_list)
    population_mean = statistics.mean(data)
    sampling_mean = statistics.mean(mean_list)
    print(population_mean,sampling_mean)
setup()









