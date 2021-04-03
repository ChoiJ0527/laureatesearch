import json

# load data
data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))

# open import file
out_file = open("laureates.import", "w") 

# add all laureates as separate json objects to outfile
for i in data["laureates"]:
    json_temp = json.dumps(i)
    print(json_temp, file = out_file)

out_file.close()