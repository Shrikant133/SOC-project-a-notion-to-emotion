    

prev_inst, instruction="", ""
while True:
    instruction= input().lower()
    if instruction== "help":
        print('''
Write 'Start' to start the car
Write 'Stop' to stop the car
Write 'Quit' to exit
        ''')
    if instruction=="start" and prev_inst!= "start":
        print("Car Started.....:}")
    elif instruction=="start" and prev_inst=="start":
        print("Car is already started>>>>")
        
    if instruction=="stop" and prev_inst!= "start" and prev_inst!= "stop":
        print("Start the Car bruv")
    elif instruction=="stop" and prev_inst!="stop":
        print("Car is Stopped")
    elif instruction=="stop" and prev_inst=="stop":
        print("Car is Stopped Already bruv !!")
        prev_inst= ""
                
    if instruction.lower()=="quit":
        print("I Quit!!!")
        break
    elif instruction!= "start" and instruction!="stop" and instruction!= "help" and instruction!= "quit" :
        print ("you need some serious help!!!!")
        
    prev_inst= instruction

