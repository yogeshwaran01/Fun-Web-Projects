input("enter any button to start check up!")
print("COVID-19 SYMPTOMS CHECKER")
name=str(input("enter your name:"))
age=int(input("enter your age:"))
s=["cough","fever","difficult to breath","none of the above"]
print("if you have any following symptoms")
for q in s:
    print(q)
a=input("enter the answer:")

sy=["diabetes","high blood pressure","lungs disorder","heart diseases","none of the above"]
print("if you have any following diseases:")
for e in sy:
    print(e)
an=input("enter your answer:")

sys=["yes","no"]
print("if you have travelled to any international countries in past 28-45 days")
for f in sys:
    print(f)
ans=input("enter your answer:")



if ({a,an,ans}=={s[3],sy[4],sys[1]}):
    print(name+",you are safe ; wear mask : stay safe")
elif({a,an,ans}=={s[0],sy[4],sys[1]} or
     {a,an,ans}=={s[1],sy[4],sys[1]} or
    {a,an,ans}=={s[2],sy[4],sys[1]} or
    {a,an,ans}=={s[3],sy[0],sys[1]} or
     {a,an,ans}=={s[3],sy[1],sys[1]} or
    {a,an,ans}=={s[3],sy[2],sys[1]} or
     {a,an,ans}=={s[3],sy[3],sys[1]} or
     {a,an,ans}=={s[3],sy[4],sys[0]} or
     {a,an,ans}=={s[3],sy[4],sys[1]}):
    print(name+",you may be infected.pls consult your family doctor")
else:
    print(name+", you are at high risk of covid-19;immediately take test")
