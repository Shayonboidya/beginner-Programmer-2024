light_on = False

while True:
    user_input = input('> ').lower()
    if 'on' in user_input:
        if light_on:
            print("ligh is alrady turned on mode.")
        else:
            light_on = True
            print("light turned on mode.")
    elif 'off' in user_input:
        if not light_on:
            print("light is alrady off mode.")
        else:
            light_on = False
            print("light turned off mode.")
    
    elif 'sleep' in user_input:
        break
    
    elif 'help' in user_input:
        print('''on-light is turned on mode
off-light is turned off
sleep-exit program''')    
         