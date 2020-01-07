import Clustering
import sys
import os
from statistics import *
'''
if distance < 0.50:
    return True
else:
    return False    
'''
if __name__ == '__main__':
    c = Clustering.Clustering()
    #studentFilename ='C:/Users/MALAVIKA P PILLAI/Documents/Studies/EDM/students/'+str(sys.argv[1])
    #get student file
    #g = open(studentFilename,'r')
    g = open("datasetHistorical_only_retention.txt",'r')
    lines = g.readlines()
    prev = ""
    distance = {}
    lines_stud = []
    for line in lines:
        words = line.split("|")
        if words[0] == "g":
                         
            if prev == "":
                prev = words[2].replace(".","").replace("\n",'')
            else:
                currFileName = prev + "_LongestPathsGraph.txt"
                f = open(currFileName,'r')
                lines_curr = f.readlines()
                value = c.find_distance(lines_curr,lines_stud)
                f.close()
                if prev not in distance:
                    distance[prev]=[]
                distance[prev].append(value)  
                prev = words[2].replace(".","").replace("\n",'')  
            lines_stud = []
        lines_stud.append(line)
    g.close()
    #entering the thresholds in the respective longest path files
   
    for curr in distance:
        f = open(str(curr)+"_LongestPathsGraph.txt",'a')
        #assuming the threshold to be the average of the value
        f.write("Threshold:"+str(mean(distance[curr])))
        #print(mean(distance[curr]))
    #print (distance)
        f.close()
    
    #pass the merged longest paths file to clustering        