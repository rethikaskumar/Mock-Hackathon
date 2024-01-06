
import json

f=open('C:\\21pt23\\Input data\\level1b.json')
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

#print(distances)


visited=[]

def MST(dist, start):
    #for(key, values) in dist.items():
        #print(key, values)
    visited.append(start)
    path=[start]
    n=''
    for (next, d) in dist[start].items():
        if next not in visited:
            n=next
            break
    if n!='':
        visited.append(n)
        path.extend(MST(dist, n))
    return path

output={}
output1={}

for vehicle in data['vehicles'].keys():
    output1[vehicle]={}
    visited.clear()
    rest=data['vehicles'][vehicle]['start_point']
    rdist={}
    for i in range(len(data['restaurants'][rest]["neighbourhood_distance"])):
        next='n'+str(i)
        rdist[next]=data['restaurants'][rest]["neighbourhood_distance"][i]
    rdist=dict(sorted(rdist.items(), key=lambda x:x[1]))
    capacity=0
    start=list(rdist.keys())[0]
    path=MST(distances, start)
    pathno=1
    output['path'+str(pathno)]=[]
    i=0
    while i<len(path):
        stop=path[i]
        if capacity+data['neighbourhoods'][stop]['order_quantity'] <= data['vehicles'][vehicle]['capacity']:
            capacity+=data['neighbourhoods'][stop]['order_quantity']
            output['path'+str(pathno)].append(stop)
            distances.pop(stop)
            for (key, value) in distances.items():
                value.pop(stop)
            rdist.pop(stop)
            i+=1
        else:
            print(pathno)
            output['path'+str(pathno)].insert(0, rest)
            output['path'+str(pathno)].append(rest)
            pathno+=1
            print(output)
            output['path'+str(pathno)]=[]
            i=0
            capacity=0
            #for (key, value) in distances.items():
                #print(key, value)
            start=list(rdist.keys())[0]
            visited.clear()
            path=MST(distances, start)
            #print(path)
    output['path'+str(pathno)].insert(0, rest)
    output['path'+str(pathno)].append(rest)
    output1[vehicle]=output

#for (key, value) in output.items():
    #print(key, value)

outfile=open('level1b\\level1b_output.json', "w")
json.dump(output1, outfile)

