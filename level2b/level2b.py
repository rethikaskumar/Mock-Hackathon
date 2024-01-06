
import json

f=open('C:\\21pt23\\Input data\\level2b.json')
data=json.load(f)

distances={}

for (neighbourhood, value) in data["neighbourhoods"].items():
    dist={}
    for i in range(len(value['distances'])):
        next='n'+str(i)
        dist[next]=value['distances'][i]
    distances[neighbourhood]=dist

n=len(distances)

for (key, value) in distances.items():
    sortedVal=dict(sorted(value.items(), key=lambda x:x[1]))
    distances.update({key: sortedVal})

#for (key, value) in distances.items():
    #print(key, value)


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

vehicleCap={}
vehicleStart={}

for (vehicle, value) in data['vehicles'].items():
    vehicleCap[vehicle]=value['capacity']
    vehicleStart[vehicle]=value['start_point']

vehicleCap=dict(sorted(vehicleCap.items(), key=lambda x: x[1]))

capacity={}
for vehicle in vehicleCap:
     output1[vehicle]={}

pathno=1
rpoplist=[]
v=[]

while len(v)<n:
    for vehicle in vehicleCap.keys():
        visited.clear()
        rest=vehicleStart[vehicle]
        rdist={}
        for i in range(len(data['restaurants'][rest]["neighbourhood_distance"])):
            next='n'+str(i)
            rdist[next]=data['restaurants'][rest]["neighbourhood_distance"][i]
        rdist=dict(sorted(rdist.items(), key=lambda x:x[1]))
        for el in rpoplist:
            rdist.pop(el)
        print(rdist)
        if len(rdist)==0:
            break
        capacity[vehicle]=0
        start=list(rdist.keys())[0]
        path=MST(distances, start)
        print(path)
        if len(path)>1:
            output1[vehicle]['path'+str(pathno)]=[]
            i=0
            stop=path[i]
            while capacity[vehicle]+data['neighbourhoods'][stop]['order_quantity'] <= vehicleCap[vehicle]:
                #print(output1[vehicle]['path'+str(pathno)])
                capacity[vehicle]+=data['neighbourhoods'][stop]['order_quantity']
                output1[vehicle]['path'+str(pathno)].append(stop)
                v.append(stop)
                distances.pop(stop)
                for (key, value) in distances.items():
                    value.pop(stop)
                rdist.pop(stop)
                rpoplist.append(stop)
                if len(v)==n:
                    break
                i+=1
                stop=path[i]
        else:
            output1[vehicle]['path'+str(pathno)]=path
            v.append(start)
            if len(v)==n:
                break
            distances.pop(start)
            rdist.pop(start)
            rpoplist.append(start)
        #print(pathno)
        output1[vehicle]['path'+str(pathno)].insert(0, rest)
        output1[vehicle]['path'+str(pathno)].append(rest)
        print(output1[vehicle])
    pathno+=1

for (key, value) in output1.items():
    print(key, value)


outfile=open('level2b\\level2b_output.json', "w")
json.dump(output1, outfile)

