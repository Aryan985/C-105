import pandas as pd
import plotly.express as px
import math
import statistics

df = pd.read_csv("class1.csv")
graph = px.scatter(df,x="Student Number",y="Marks")

marks = df["Marks"]
mean = marks.mean(axis = 0)
print (mean) 

graph.update_layout(shapes=[dict(type="line",x0=0,x1=len(marks),y0=mean,y1=mean)])
graph.show()

sq = []
for i in marks:
    num = int(i)-mean
    num = num**2
    sq.append(num)

sum = 0
for i in sq:
    sum = sum+i

result = sum/(len(marks)-1)
std = math.sqrt(result)
print(std)

print(statistics.stdev(marks))
