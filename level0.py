import json

f=open('Input data\\level0.json')
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

for start in distances.keys():
    output[start]={}
    visited.clear()
    path=MST(distances, start)
    path.insert(0, 'r0')
    path.append('r0')
    output[start]['path']=path

for(key, value) in output.items():
    print(key, value)

outfile=open('output0.json', "w")
json.dump(output, outfile, indent=5)


