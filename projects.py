
import json
import numpy as np

names = []
managers = []
watchers = []
priorities = []
prior_dict = {}

with open('source_file_2.json') as json_file:
    data = json.load(json_file)
    
    for element in data:
        names.append(element['name'])
        managers.append(element['managers'])
        watchers.append(element['watchers'])
        priorities.append(element['priority'])
        prior_dict[element['name']] = float(element['priority'])

managers_unique = []
for project in managers:
    for man in project:
        if man not in managers_unique:
            managers_unique.append(man)
            
watchers_unique = []
for project in watchers:
    for watch in project:
        if watch not in watchers_unique:
            watchers_unique.append(watch)
            
managers_dict = {man: [] for man in managers_unique}
watchers_dict = {watch: [] for watch in watchers_unique}

for i in range(len(names)):
    this_managers = managers[i]
    for man in this_managers:
        ind = 0
        for proj in managers_dict[man]:
            if prior_dict[proj] <= priorities[i]:
                ind += 1
        managers_dict[man].insert(ind, names[i])
        
    this_watchers = watchers[i]
    for watch in this_watchers:
        ind = 0
        for proj in watchers_dict[watch]:
            if prior_dict[proj] <= priorities[i]:
                ind += 1
        watchers_dict[watch].insert(ind, names[i])
        
with open('managers.json', 'w') as outfile:
    out = json.dumps(managers_dict, indent=4)
    print('MANAGERS:')
    print(out)
    json.dump(out, outfile)     
    
with open('watchers.json', 'w') as outfile:
    out = json.dumps(watchers_dict, indent=4)
    print('WATCHERS:')
    print(out)
    json.dump(out, outfile)  
        