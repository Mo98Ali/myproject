from __init__ import *
from flask import render_template, flash, request,redirect
from forms import *
from datetime import datetime
from pack import *
import plotly
import plotly.express as px
import json
import pandas as pd
import numpy as np

@app.route("/")
def index():
    return render_template("firstPage.html", title = " CBT-I Website")

@app.route("/login",methods = ["POST","GET"])
def login():
      if request.method == "POST":
            log = Login(request.form)
            user = log.username.data
            pw = log.passwort.data
            user_pw = {"user":user,"passwort":pw}
            
            #try to find user and compare to tiped in username
            try:
                user == db.user.find_one({"user":user})["user"] and pw == db.user.find_one({"passwort":pw})["passwort"]
                #the username_g is global. Therefor the Data can be saved with the username. Better for searching in the db
            
            except:
                    raise Exception("Username or Password wrong. Pleas try again or register")
             
            else:
             global username_g
             username_g = user
             if db.user.find_one({"user":user},{"is_doc":"Yes"})["is_doc"] == "Yes":
                  flash("Logged in as Doctor: \n"+ username_g)
                  return redirect("/home_d")
           
                 
             else: 
                 return redirect("/home_p")      

                

      else:
            
            login1 = Login()
            return render_template("login.html",form = login1)

@app.route("/register",methods =["POST","GET"])
def register():
       if request.method == "POST":
            log = Login(request.form)
            user = log.username.data
            pw = log.passwort.data
            id = log.doc_id.data
            is_doc = log.is_doc.data

            user_pw = {"user":user,"passwort":pw,"is_doc":is_doc,"id":id}
            global username_g
            username_g = user

            try:
                #try to find user and compare to tiped in username
               user == db.user.find_one({"user":user})["user"]
            except:   

                if is_doc == "Yes":
                     #generate doc id
                     doc_id = np.random.randint(1000,9999)
                     user_pw = {"user":user,"passwort":pw,"is_doc":is_doc,"id":str(doc_id)}
                     db.user.insert_one(user_pw)
                     flash("Registration successfull"+user+str(doc_id))
                     return redirect("/home_d")
                
                #if user doesnt exist, append the user
                db.user.insert_one(user_pw)
                flash("Registration successfull"+user)
                return redirect("/PSQI_Form")
            else:
                #if the user is existing, try again
                flash("Username is not available ")
                return redirect("/register")
                 
       else:
            login1 = Login()
            return render_template("register.html",form = login1)
       

#Home route for Doctors
@app.route("/home_d",methods = ["POST","GET"])
def home_d():
     try:
        #search id of the logged in doctor
        id = db.user.find_one({"user":username_g})["id"]
        #get every patient with the doc id 
        i = 0
        flash("   Your Patients are: ")
        #search for every patient the doctor is connected to. And count it
        for user in db.user.find():
            if user["id"] == id and user["is_doc"] == "No":
             i+=1
             flash(user["user"]+",")  

        
        return render_template("home_doc.html", title = " CBT-I Website", form = form1)
     except:
        form1 = home()
        return render_template("home_doc.html", title = " CBT-I Website",form = form1)

@app.route("/search",methods = ["POST","GET"])
def search_patient():
        #doctor gets a StringField to write a Patients name    
        if request.method == "POST":
            form1 = home(request.form)
            name = form1.name.data
            doc = form1.document.data
            l = []
            try:
                 if db.SleepDiary_m.find_one({"user":name}) == None:
                    raise Exception()
            except:
                flash("User not found! Or Patient has no Sleep Diarys/PSQI ")
                return redirect("/search")

            else:
                 if doc == "SleepDiary_m":
                    anz = db.SleepDiary_m.count_documents({"user":name})
                    for i in range(0,anz):
                        flash("Date: "+str(db.SleepDiary_m.find({"user":name})[i]["Date"]["Day "])+"."+str(db.SleepDiary_m.find({"user":name})[i]["Date"]["Month "])+"."+str(db.SleepDiary_m.find({"user":name})[i]["Date"]["Year "]))
                        flash("Sleepy/AwakeFeeling "+db.SleepDiary_m.find({"user":name})[i]["Sleepy/AwakeFeeling"])
                        flash("Mood "+db.SleepDiary_m.find({"user":name})[i]["Mood"])
                        flash("TimeLightOff[Time] "+db.SleepDiary_m.find({"user":name})[i]["TimeLightOff[Time]"])
                        flash("LightOff2Sleep[Min] "+db.SleepDiary_m.find({"user":name})[i]["LightOff2Sleep[Min]"])
                        flash("HowOftenAwakeNight "+db.SleepDiary_m.find({"user":name})[i]["HowOftenAwakeNight"])
                        flash("HowLongTotal[Min] "+db.SleepDiary_m.find({"user":name})[i]["HowLongTotal[Min]"])
                        flash("WakeUpTime[Time] "+db.SleepDiary_m.find({"user":name})[i]["WakeUpTime[Time]"])
                        flash("TotalSleepTime[Hours:Min] "+db.SleepDiary_m.find({"user":name})[i]["TotalSleepTime[Hours:Min]"])
                        flash("RiseTime[Time] "+db.SleepDiary_m.find({"user":name})[i]["RiseTime[Time]"])
                        flash("SleepDrugName "+db.SleepDiary_m.find({"user":name})[i]["SleepDrugName"])
                        flash("DrugDosis "+db.SleepDiary_m.find({"user":name})[i]["DrugDosis"])
                        flash("DrugTime[Time] "+db.SleepDiary_m.find({"user":name})[i]["DrugTime[Time]"])
                 if doc == "SleepDiary_e":
                    anz = db.SleepDiary_e.count_documents({"user":name})
                    for i in range(0,anz):
                        flash("Date: "+str(db.SleepDiary_e.find({"user":name})[i]["Date"]["Day "])+"."+str(db.SleepDiary_e.find({"user":name})[i]["Date"]["Month "])+"."+str(db.SleepDiary_e.find({"user":name})[i]["Date"]["Year "]))
                        flash("Mood "+db.SleepDiary_e.find({"user":name})[i]["Mood"])
                        flash("DailyTasks "+db.SleepDiary_e.find({"user":name})[i]["DailyTasks"])
                        flash("SleepAtDay[Time] "+db.SleepDiary_e.find({"user":name})[i]["SleepAtDay[Time]"])
                        flash("SleepAtDay[min] "+db.SleepDiary_e.find({"user":name})[i]["SleepAtDay[min]"])
                        flash("AlcConsumption[HowManyGlases] "+db.SleepDiary_e.find({"user":name})[i]["AlcConsumption[HowManyGlases]"])
                        flash("KindOfAlc "+db.SleepDiary_e.find({"user":name})[i]["KindOfAlc"])
                        flash("SpecialIncidents "+db.SleepDiary_e.find({"user":name})[i]["SpecialIncidents"])

                     
                 if  doc == "PSQI":
                     anz = db.SleepDiary_m.count_documents({"user":name})
                     i = 0
                     flash("Name: "+db.PSQI.find_one({"Name":name})["Name"])
                     flash("Surename "+db.PSQI.find_one({"Name":name})["Surename"])
                     flash("Age "+db.PSQI.find_one({"Name":name})["Age"])
                     flash("Weight "+db.PSQI.find_one({"Name":name})["Weight"])
                     flash("Gender "+db.PSQI.find_one({"Name":name})["Gender"])
                     flash("WorkingSituation "+db.PSQI.find_one({"Name":name})["WorkingSiuation"])
                     flash("BedTime4Weeks "+db.PSQI.find_one({"Name":name})["BedTime4Weeks"])
                     flash("Time2Sleep[min] "+db.PSQI.find_one({"Name":name})["Time2Sleep[min]"])
                     flash("RiseTime4Weeks "+db.PSQI.find_one({"Name":name})["RiseTime4Weeks"])
                     flash("EffecSleeptime4Weeks[hours] "+db.PSQI.find_one({"Name":name})["EffecSleeptime4Weeks[hours]"])
                     flash("a_30toSleep "+db.PSQI.find_one({"Name":name})["a_30toSleep"])
                     flash("b_wakeups "+db.PSQI.find_one({"Name":name})["b_wakeups"])
                     flash("Toilet: "+db.PSQI.find_one({"Name":name})["Toilet"])
                     flash("BreathingProblems "+db.PSQI.find_one({"Name":name})["BreathingProblems"])
                     flash("CoughSnore "+db.PSQI.find_one({"Name":name})["CoughSnore"])
                     flash("toCold "+db.PSQI.find_one({"Name":name})["cold"])
                     flash("toWarm "+db.PSQI.find_one({"Name":name})["toWarm"])
                     flash("BadDreams "+db.PSQI.find_one({"Name":name})["BadDreams"])
                     flash("Pain "+db.PSQI.find_one({"Name":name})["Pain"])
                     flash("OtherReasons "+db.PSQI.find_one({"Name":name})["OtherReasons"])
                     flash("OtherFreq "+db.PSQI.find_one({"Name":name})["OtherFreq"])
                     flash("SleepQulity4Weeks "+db.PSQI.find_one({"Name":name})["SleepQulity4Weeks"])
                     flash("Drugs "+db.PSQI.find_one({"Name":name})["Drugs"])
                     flash("FallInToSleepAtDay "+db.PSQI.find_one({"Name":name})["FallInToSleepAtDay"])
                     flash("NotEnoughEnergy "+db.PSQI.find_one({"Name":name})["NotEnoughEnergy"])
                     flash("SleepAlone "+db.PSQI.find_one({"Name":name})["SleepAlone"])
                     flash("a_LoudSnoring "+db.PSQI.find_one({"Name":name})["a_LoudSnoring"])
                     flash("b_StopBreathing "+db.PSQI.find_one({"Name":name})["b_StopBreathing"])
                     flash("c_LegMoving "+db.PSQI.find_one({"Name":name})["c_LegMoving"])
                     flash("d_ConfusionPeriodsAtNight "+db.PSQI.find_one({"Name":name})["d_ConfusionPeriodsAtNight"])
                     flash("e_OtherFormsOfRestlessness "+db.PSQI.find_one({"Name":name})["e_OtherFormsOfRestlessness"])

                 
                 return redirect("/search")  

           
        else:
            form2 = home()
            return render_template("search.html", form = form2)


#Home route for Patient
@app.route("/home_p")
def home_p():
   #Show the interesting values Sleepefficiency and Sleep endurance
   try:
    df = []
    #get the user data from user
    flash("Logged in as: "+username_g)
    #find user that is logged in
    user_data =  db.SleepDiary_m.find({"user":username_g})
    anz = db.SleepDiary_m.count_documents({"user":username_g})

   #read every data from username
    for i in range(0,anz):
            #read every mood data out of user data 
            for mood in user_data[i]["Mood"]:
                 df.insert(i,int(mood))
  

    fig = px.line(x=[range(0,anz)],y=df)
    fig.update_layout(
            title = "Mood over the Time",
            xaxis_title = "Days",
            yaxis_title = "Mood",
            legend_title = "Mood",
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("view_SleepDiary.html", title = " CBT-I Website", graphJSON = graphJSON)

   except:
        #new registered user, has a empty Diary. Exception handling. return blank homescreen
        return render_template("view_SleepDiary.html", title = " CBT-I Website",)


#this home route checks with home the user needs. Doc page or Patient page
@app.route("/home")
def home_decide():
 try: 
     if db.user.find_one({"user":username_g,"is_doc":"Yes"})["is_doc"] == "Yes":
        return redirect("/home_d")
    
 except:
     return redirect("/home_p")



#Route to add a Sleep Diary
@app.route("/add_SleepDiary", methods =["POST","GET"])
def add_SleepDiary():

    morning = True
    if datetime.now().hour > 17 and datetime.now().hour < 4:
        #call the evening diary
        morning = False
        if request.method == "POST":
            form1 = Sleepdiary(request.form)
            SleepDiary_mood = form1.mood.data
            SleepDiary_DailyTasks = form1.dailyTasks.data
            SleepDiary_SleepAtDay = form1.sleepAtDay.data
            SleepDiary_SleepAD_min = form1.sleepAtDay_min.data
            SleepDiary_AlcCons = form1.alcConsumption.data
            SleepDiary_KindOfAlc = form1.kindOfAlc.data
            SleepDiary_Feeling = form1.Feeling.data
            SleepDiary_Time2Bed = form1.Time2Bed.data
            form1 = Login(request.form)
            user = username_g
            date = {"Day ":datetime.now().day,"Month ":datetime.now().month,"Year ":datetime.now().year}
            l = [user,date,SleepDiary_mood,SleepDiary_DailyTasks,SleepDiary_SleepAtDay,SleepDiary_SleepAD_min,
                 SleepDiary_AlcCons,SleepDiary_KindOfAlc,SleepDiary_Feeling,SleepDiary_Time2Bed]
            
            #dict to json
            json_Dat = packen(l,morning)


            #only dict can be uploaded
            data = json.loads(json_Dat)
            db.SleepDiary_e.insert_one(data)

            #if mood is not as good as wanted, redirect to help pages
            if int(SleepDiary_mood) >= 3 and int(SleepDiary_mood) <= 4:
                return redirect("/breathing")
            elif int(SleepDiary_mood) >= 5 and int(SleepDiary_mood) <= 6:
                return redirect("/PMR")


            flash("SD_e successfully added")
            return redirect("/home_p")
        else:
            form1 = Sleepdiary()
            return render_template("add_SleepDiary_e.html", form = form1)
    
    elif  request.method == "POST":
            morning = True
           
            form1 = Sleepdiary(request.form)
            SleepDiary_saf = form1.sleepy_AwFeeling.data
            SleepDiary_mood = form1.mood.data
            SleepDiary_Tlo = form1.timeLightOff.data
            SleepDiary_lo2f = form1.timeLightOff2S.data
            SleepDiary_hoan = form1.howoAwN.data
            SleepDiary_Hlt = form1.howLongTotal.data
            SleepDiary_Wut = form1.wakeUpTime.data
            SleepDiary_Tst = form1.totalSleepTime.data
            SleepDiary_rT = form1.riseTime.data
            SleepDiary_Sdn = form1.sleepDrugName.data
            SleepDiary_Dd = form1.drugDosis.data
            SleepDiary_Dt = form1.drugTime.data
            form1 = Login(request.form)
            user = username_g
            
            date = {"Day ":datetime.now().day,"Month ":datetime.now().month,"Year ":datetime.now().year}
        
            print(username_g)
            l = [user,date,SleepDiary_saf,SleepDiary_mood,SleepDiary_Tlo,SleepDiary_lo2f,SleepDiary_hoan,SleepDiary_Hlt,
                 SleepDiary_Wut,SleepDiary_Tst,SleepDiary_rT,SleepDiary_Sdn,SleepDiary_Dd,SleepDiary_Dt]
            
            #test is the name of the collection /database folder
            #dict to json
            json_Dat = packen(l,morning)
        
            #only dict can be uploaded
            data = json.loads(json_Dat)
            db.SleepDiary_m.insert_one(data)
            print(username_g)
            flash("SleepDiary successfully added", "sucess")
            return redirect("/home_p")
    else:
        form1 = Sleepdiary()
        return render_template("add_SleepDiary_m.html", form = form1) 

#Route for the PSQI Form
@app.route("/PSQI_Form",methods=["POST","GET"])
def PSQI_Form():
    
    if request.method == "POST":
        
          form2 = PSQI_Forms(request.form)
          name = form2.name.data
          surename = form2.surename.data
          age = form2.age.data
          weight = form2.weight.data
          gender = form2.gender.data
          wS = form2.workingSit.data
          BT4W = form2.BedTime4Weeks.data
          T2S = form2.Time2Sleep.data
          RT4W = form2.RiseTime4Weeks.data
          ES = form2.EffecSleept.data
          a_30toS = form2.a_30toSleep.data
          b_w = form2.b_wakeups.data
          Toilet = form2.Toilet.data
          BP = form2.BreathingProbs.data
          CS = form2.CoughSnore.data
          toCold = form2.cold.data
          toWarm = form2.toWarm.data
          BadDreams = form2.BadDreams.data
          Pain = form2.Pain.data
          otherR = form2.OtherReasons.data
          otherF = form2.OtherFreq.data
          sQ4W = form2.sleepQual4Weeks.data
          Drugs = form2.Drugs.data
          FITSAD = form2.FallInToSleepAtDay.data
          NEE = form2.NotEnoughE.data
          SA = form2.SleepAlone.data
          lS = form2.a_LoudSnoring.data
          SB = form2.b_StopBreathing.data
          LM = form2.c_LegMoving.data
          CPAN = form2.d_ConfPerAtN.data
          oFR = form2.e_otherFormsoRsls.data
          form2 = Login(request.form)
          user = username_g
          l = [user,name,surename,age,weight,gender,wS,BT4W,T2S,RT4W,ES,a_30toS,b_w,Toilet,BP,CS,toCold,toWarm,
               BadDreams,Pain,otherR,otherF,sQ4W,Drugs,FITSAD,NEE,SA,lS,SB,LM,CPAN,oFR]
          jsonDat = PSQI_packen(l)
          data = json.loads(jsonDat)
          db.PSQI.insert_one(data)
          flash("PSQI successfully added")
          return redirect("/home_p")

        #if sleep alone is false, every question after that is zero or empty
          
    else:
        form2 = PSQI_Forms()
        return render_template("add_PSQIForm.html",form = form2)  


#route to add a doctor to a patient  
@app.route("/add_Doc",methods = ["POST","GET"])          
def add_Doc():
     #user can manually write the doctor-id
     if request.method == "POST":
        doc_id = Login(request.form)
        id = doc_id.doc_id.data
        try:
            db.user.find_one({"id":id})
            db.user.update_one({"user":username_g},{"$set":{"id":id}})
            flash("Doctor updated: "+"Dr. "+db.user.find_one({"id":id,"is_doc":"Yes"})["user"])
            return redirect("/home_p")
        
        except:
            flash("Doctor isnt in the Database!")
            return redirect("/home_p")
       
     else:
        form = Login()
        return render_template("add_Doc.html",form =form)  

#route to logout the user
@app.route("/logout")
def logout():
    username_g = " " # lösche den Nutzer aus dem Laufzeitspeicher
    return redirect("/")

#Page for User requested exercise help
@app.route("/breathingexc")
def breathing():
    return render_template("breathingexc.html")

#Page for User requested exercise help
@app.route("/PMR_exc")
def PMR():
    return render_template("PMR_exc.html")

#Bibliothek for knowledge of CBT-I and more
@app.route("/bib")
def bib():
    return render_template("UsefullToKnow.html")

#help route for the mood request in the sleep diary route
@app.route("/breathing")
def helproute_b():
    return render_template("/breathing.html")

#help route for the mood request in the sleep diary route
@app.route("/PMR")
def helproute_p():
    return render_template("/PMR.html")



@app.route("/write_msg",methods =["POST","GET"])
def write_msg():
    if request.method == "POST":
        form1 = msg()
        message = form1.message.data
        user = form1.name.data
        date = {"Day ":datetime.now().day,"Month ":datetime.now().month,"Year ":datetime.now().year}

        try:
            if db.user.find_one({"user":user}) == None:
                raise Exception()
        except:
            flash("User doesnt exist!")
            
            return redirect("/home_d")
        
        else:
            db.msg.insert_one({"Date":date,"user":username_g,"msg":message,"receiver":user})
           
            return redirect("/home_d")

    else:
        form1 = msg()
        return render_template("send_msg.html",form = form1)
    



@app.route("/receive_msg")
def receive_msg():
    anz = db.msg.count_documents({"receiver":username_g})
    
    for i in range(0,anz):
     flash(db.msg.find({"receiver":username_g})[i]["msg"])
     

    return render_template("receive_msg.html")



