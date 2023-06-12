from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired

#Todo is a class for managing the Buttons, question fields and questions
#in this class has to be defined "what the function of a specific new web input is,
# like new questions and their answer field"


class Sleepdiary(FlaskForm):
   # name = StringField("Wie lange haben Sie heute geschlafen? (in Stunden)", validators=[DataRequired()])
   # Frage = StringField("Haben Sie Alkohol vor dem Schlafen getrunken? ", validators=[DataRequired()])
   # description = TextAreaField("Description",validators=[DataRequired()])
   # completed = SelectField("Completed",choices=[("False","False"),("True","True")],
    validators = ([DataRequired()])
    submit = SubmitField("Submit")
#now there are the Questions for the sleep diary at Evening
    mood = StringField("How is your Mood?",validators=[DataRequired()])
    dailyTasks = StringField("What are your daily tasks?",validators=[DataRequired()])
    sleepAtDay = StringField("How many hour did you sleep during the day?",validators=[DataRequired()])
    #was ist mit min gemeint? und wieso doppelt?
    sleepAtDay_min = StringField("How many hour did you sleep during the day[Time]?",validators=[DataRequired()])
    alcConsumption = StringField("Did you drink alcohol before sleeping [How Many Glasses]",validators=[DataRequired()])
    kindOfAlc = StringField("What kind of Alcohol?",validators=[DataRequired()])
    Feeling = StringField("How are your Feelings?",validators=[DataRequired()])
    Time2Bed = StringField("When did you get to bed?[Time]",validators=[DataRequired()])
#Questions for the morning
    sleepy_AwFeeling = StringField("How are you after sleep?",validators=[DataRequired()])
    timeLightOff = StringField("When did you shut off your light[Time]?",validators=[DataRequired()])
    timeLightOff2S = StringField("After shut off the light, how long does it need to sleep[Time]?",validators=[DataRequired()])
    howoAwN = StringField("How often did you wake up during night?",validators=[DataRequired()])
    howLongTotal = StringField("How long have you sleept[Time]?",validators=[DataRequired()])
    wakeUpTime = StringField("When did you wake up[Time]?",validators=[DataRequired()])
    totalSleepTime = StringField("Whats your total sleep amount last night[Time]?",validators=[DataRequired()])
    riseTime = StringField("When did you leave bed [Time]?",validators=[DataRequired()])
    sleepDrugName = StringField("Which sleep drug do you use?",validators=[DataRequired()])
    drugDosis = StringField("How much of the sleep drug do you use?",validators=[DataRequired()])
    drugTime = StringField("When did you take the sleep drug?",validators=[DataRequired()])

class PSQI_Forms(FlaskForm):
    name = StringField("Name:",validators=[DataRequired()])
    surename = StringField("Surename:",validators=[DataRequired()])
    age = StringField("Age:",validators=[DataRequired()])
    weight = StringField("Weight [Kg]",validators=[DataRequired()])
    gender = SelectField("Select your biological gender",choices = [("Female","Female"),("Male","Male")])
    workingSit = StringField("How is your working situation?",validators=[DataRequired()])
    BedTime4Weeks = StringField("When do you go to Bed in the last 4 Weeks?",validators=[DataRequired()])
    Time2Sleep = StringField("When is your sleeping time?[min]",validators=[DataRequired()])
    RiseTime4Weeks = StringField("When do you get up from bed in the last 4 Weeks?",validators=[DataRequired()])
    EffecSleept = StringField("Estimate your effective sleep time?[hours]",validators=[DataRequired()])
    a_30toSleep = StringField("in the last four weeks how often do you stay awake for more than 30 minutes?",validators=[DataRequired()]) 
    b_wakeups = StringField("in the last four weeks how often do you wake up during the night?",validators=[DataRequired()])
    Toilet = StringField("How often do you go to the toilet during night?",validators=[DataRequired()])
    BreathingProbs = StringField("Do you have breath issues during night?",validators=[DataRequired()])
    CoughSnore = StringField("Do you snore?",validators=[DataRequired()])
    cold = StringField("Is it to cold to sleep?",validators=[DataRequired()])
    toWarm = StringField("Is it to warm to sleep?",validators=[DataRequired()])
    BadDreams = StringField("Do you have bad dreams?",validators=[DataRequired()])
    Pain = StringField("Do you have pain during night?",validators=[DataRequired()])
    OtherReasons = StringField("Are there other reasons for sleepnes?",validators=[DataRequired()])
    OtherFreq = StringField("How often do the other Reasons happen?",validators=[DataRequired()])
    OtherDescription = StringField("Are there other descriptions?",validators=[DataRequired()])
    
    sleepQual4Weeks = StringField("How is your sleepquality during the last 4 Weeks?",validators=[DataRequired()])
    Drugs = StringField("Do you consume Drugs for sleeping ???",validators=[DataRequired()])
    stayAwake = StringField("How long do you stay awake?",validators=[DataRequired()])
    FallInToSleepAtDay = StringField("Do you sleep over the day (naps)?",validators=[DataRequired()])
    NotEnoughE = StringField("Are you on low Energy over the day?",validators=[DataRequired()])
    SleepAlone = SelectField("Do you sleep alone",choices = [("Yes","Yes"),("No","No")])
    #only used if Sleep alone is false 
    #Flat mate or partner
    a_LoudSnoring = StringField("Is he/she snoring loud?",validators=[DataRequired()])
    b_StopBreathing = StringField("Does he/she stop breathing during sleep?",validators=[DataRequired()])
    c_LegMoving = StringField("Does he/she move his/her legs during sleep?",validators=[DataRequired()])
    d_ConfPerAtN = StringField("Are there Confusion Periods at night?",validators=[DataRequired()])
    e_otherFormsoRsls = StringField("Are there other Forms of Restlessnes?",validators=[DataRequired()])
    submit = SubmitField("Submit")

class Login(FlaskForm):
     username = StringField("Username",validators=[DataRequired()])
     passwort = StringField("Passwort",validators=[DataRequired()])
     doc_id = StringField("Doctor-ID")
     submit = SubmitField("Submit")
     is_doc = SelectField("clinical use?", choices = [("Yes","Yes"),("No","No")])
     user_patient= StringField("Username of patient", validators=[DataRequired()])


class home(FlaskForm):
     name = StringField("Name of your Patient", validators=[DataRequired()])
     document = SelectField("Select the Document of your Patient?", choices = [("SleepDiary_m","SleepDiary_m"),("SleepDiary_e","SleepDiary_e"),("PSQI","PSQI")])
     submit = SubmitField("Submit")
                          
class msg(FlaskForm):
     message = TextAreaField("Message for your Patient",validators=[DataRequired()])
     name = StringField("Name of your Patient, to send the Message",validators=[DataRequired()])
     submit = SubmitField("Send")