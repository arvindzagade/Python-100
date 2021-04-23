       

import os

import json

count = 0

for root, dirs, files in os.walk("C:/Users//Downloads/Sample_2021-02-03/Sample_2021-02-03/BP/2018"):

    #print(root)

    for file in files:

        if file.endswith(".json"):

            json_file=os.path.join(root, file)

            print(json_file)

            if count == 0:

              with open(json_file,'r') as f:

                projectData = f.read()

                projectData= json.loads(projectData)

               
            if count == 1:

              with open(json_file,'r') as f:

                taskData = f.read()

                taskData= json.loads(taskData)

            if count == 2:

              with open(json_file,'r') as f:

                assetData = f.read()

                assetData= json.loads(assetData)

                
             if count > 2:

              with open(json_file ,'r') as f:

                EventData = f.read()

                EventData= json.loads(EventData)

                print("============================")


                FinalEventData = {}

                FinalEventData['event'] = EventData

                FinalData = {}

                for data in (projectData ,taskData , assetData, FinalEventData):

                  FinalData.update(data)

                  
                

                EventData = FinalData

                print(json.dumps(EventData))

 

              with open(json_file,"w") as f:

                json.dump(EventData, f)

                

            count = count+1  
