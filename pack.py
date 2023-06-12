import json
import os

def packen(list,morning):
    Path ="C:/AppWeb/UserData/"
    file_Path = os.path.join(Path,"User_sleepdiary_m.json") #Path for saving UserData
    
    if morning == True:
        patData = {"user":"","Date":"","Sleepy/AwakeFeeling":0, "Mood":0, "TimeLightOff[Time]":"","LightOff2Sleep[Min]": 0,
                   "HowOftenAwakeNight":0,"HowLongTotal[Min]":0,"WakeUpTime[Time]":"","TotalSleepTime[Hours:Min]":"",
                   "RiseTime[Time]":"","SleepDrugName":"","DrugDosis":"","DrugTime[Time]":""
                   }  # Dictionary with keys but empty values
        i=0
        for key in patData.keys():
            patData[key] = list[i]
            i+=1
        
        patJSON = json.dumps(patData)                        # Convert dict in to a JSON-string (serialisation)

        with open(file_Path,"w") as write_file:
            json.dump(patJSON,write_file)
        return patJSON                                       #return converted JSON String
   
    elif morning == False:
        patData = {"user":"","Date":"","Mood":0,"DailyTasks":0,"SleepAtDay[Time]":"","SleepAtDay[min]":0,
                   "AlcConsumption[HowManyGlases]":0,"KindOfAlc":"","Feeling":"","Time2Bed":""}
        i=0
        for key in patData.keys():
            patData[key] = list[i]
            i+=1
        
        patJSON = json.dumps(patData)
        with open(file_Path,"w") as write_file:
            json.dump(patJSON,write_file)
        return patJSON

def PSQI_packen(list):
    Path ="C:/AppWeb/UserData/"
    file_Path = os.path.join(Path,"User_PSQI.json") #Path for saving UserData
    patData = {"username":"","Name": "", "Surename": "", "Age": 0, "Weight": 0, "Gender": "", "WorkingSiuation": "",
             "BedTime4Weeks": "", "Time2Sleep[min]": 0, "RiseTime4Weeks": "", "EffecSleeptime4Weeks[hours]": 0,
             "a_30toSleep": 0, "b_wakeups": 0, "Toilet": 0, "BreathingProblems": 0, "CoughSnore": 0, "cold": 0,
             "toWarm": 0,"BadDreams": 0, "Pain": 0, "OtherReasons": "", "OtherFreq": 0,
             "SleepQulity4Weeks": 0,"Drugs": 0,"FallInToSleepAtDay": 0,"NotEnoughEnergy": 0,
             "SleepAlone": "","a_LoudSnoring":0, "b_StopBreathing":0, "c_LegMoving":0, 
             "d_ConfusionPeriodsAtNight":0, "e_OtherFormsOfRestlessness": 0 }    
    i=0
    for key in patData.keys():
        patData[key] = list[i]
        i+=1


    patJSON = json.dumps(patData)                        # Convert dict in to a JSON-string (serialisation)

    with open(file_Path,"w") as write_file:
        json.dump(patJSON,write_file)
        return patJSON                                       #return converted JSON String