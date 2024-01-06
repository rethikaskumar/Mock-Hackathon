import json

f=open('C:\\21pt23\\Input data\\level0.json')
data=json.load(f)

distances={}

for (neighbourhood, value) in data["neighbourhoods"].items():
    dist={}
    for i in range(len(value['distances'])):
        next='n'+str(i)
        dist[next]=value['distances'][i]
    distances[neighbourhood]=dist

for (key, value) in distances.items():
    sortedVal=dict(sorted(value.items(), key=lambda x:x[1]))
    distances.update({key: sortedVal})

output={}
visited=[]

for vehicle in data['vehicles'].keys():
    output[vehicle]={}
    visited.clear()
    rest=data['vehicles'][vehicle]['start_point']
    rdist={}
    for i in range(len(data['restaurants'][rest]["neighbourhood_distance"])):
        next='n'+str(i)
        rdist[next]=data['restaurants'][rest]["neighbourhood_distance"][i]
    rdist=dict(sorted(rdist.items(), key=lambda x:x[1]))
    start=list(rdist.keys())[0]