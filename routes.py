"""Find shortest paths in a weighted, directed graph."""
import argparse
import heapq
import json
import math


def validate(edges):
    if not isinstance(edges,list):
        raise ValueError("edges must be a list")
    graph={}
    for edge in edges:
        source,destination,cost=edge["from"],edge["to"],edge["cost"]
        if not isinstance(source,str) or not source or not isinstance(destination,str) or not destination:
            raise ValueError("invalid node")
        if isinstance(cost,bool) or not isinstance(cost,(int,float)) or not math.isfinite(cost) or cost<0:
            raise ValueError("edge cost must be finite and nonnegative")
        graph.setdefault(source,[]).append((destination,cost))
        graph.setdefault(destination,[])
    return graph


def shortest_path(edges,start,goal):
    graph=validate(edges)
    if start not in graph or goal not in graph:
        raise ValueError("unknown start or destination")
    distances={start:0}
    previous={}
    queue=[(0,start)]
    while queue:
        distance,node=heapq.heappop(queue)
        if distance!=distances[node]:
            continue
        if node==goal:
            path=[goal]
            while path[-1]!=start:
                path.append(previous[path[-1]])
            return {"path":list(reversed(path)),"cost":round(distance,5)}
        for neighbor,cost in graph[node]:
            candidate=distance+cost
            if candidate<distances.get(neighbor,math.inf):
                distances[neighbor]=candidate
                previous[neighbor]=node
                heapq.heappush(queue,(candidate,neighbor))
    return {"path":None,"cost":None}


def main():
    parser=argparse.ArgumentParser(description="Compute shortest route on a directed graph")
    parser.add_argument("graph_file")
    parser.add_argument("start")
    parser.add_argument("destination")
    args=parser.parse_args()
    with open(args.graph_file,encoding="utf-8") as file:
        data=json.load(file)
    print(json.dumps(shortest_path(data["edges"],args.start,args.destination),indent=2))


if __name__=="__main__":
    main()
