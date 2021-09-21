import os
import subprocess
import time
import os
fa=0
co=0

x= os.system('zenity --info --title="rules for Quiz"  --text="->you have to choose between true or false \n->Time is 5 minute\n->you have to allow webcam \n->make sure that your face is visible" --no-wrap --ok-label="start" ')


a=os.system('zenity --question --title="Question 1" --text="The modulus operator(%) in java can be used only with variables of integer type." --no-wrap --ok-label="False" --cancel-label="True"')
if a == 256:
	fa+=1
	print("True")
	
else:
	print("False")
	co+=1

	

#time.sleep(1)
b=os.system('zenity --question --titlce="Question 2" --text="Declaration must appear at the start of the body of a java method." --no-wrap --ok-label="False" --cancel-label="True"')
if b == 256:
	fa+=1
	print("True")
else:
	co+=1
	print("False")
	
#time.sleep(1)
c=os.system('zenity --question --title="Question 3" --text="The Switch selection structure must end with the default case." --no-wrap --ok-label="False" --cancel-label="True"')
if c == 256:
	fa+=1
	print("True")
else:
	co+=1
	print("False")
#time.sleep(1)
d=os.system('zenity --question --title="Question 4" --text="Java is a object oriented programming language ."  --no-wrap --ok-label="False" --cancel-label="True"')

if d == 256:
	co+=1
	print("True")
else:
	fa+=1
	print("False")
#time.sleep(1)
e=os.system('zenity --question --title="Question 5" --text="Objects of a subclass can be assigned to a super class reference." --no-wrap --ok-label="False" --cancel-label="True"')
if e == 256:
	co+=1
	print("True")
else:
	fa+=1
	print("False")
#time.sleep(1)
f =os.system('zenity  --info --icon-name="emblem-default" --title="Finish" --text="Successfully submitted"')
time.sleep(1)

ans = os.system('zenity --info  --title="Result" --text="Correct answer = {} \n wrong answer= {}" --no-wrap'.format(co,fa))




