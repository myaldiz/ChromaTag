import json

f = open("../Output/log.txt", "r")
data = dict()

for line in f:
    det_dict = dict()
    classes = list()
    corners = list()
    
    ln_sp = line.split()
    filename = ln_sp[1].split("/")[-1]
    t = ln_sp[2:]
    det = [t[i:i + 25] for i in range(0, len(t), 25)]
    for tag in det:
        classes.append(int(tag[-1]))
        c = [float(val) for val in tag[16:24]]
        corners.append([c[i:i + 2] for i in range(0, 8, 2)])
    det_dict["classes"] = classes
    det_dict["corners"] = corners   
    data[filename] = det_dict

with open("detections.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent = 4)