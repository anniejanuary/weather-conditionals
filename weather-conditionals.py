temp_input=float(input("Enter the outdoor temperature: "))

if temp_input<15:
    movies=bool(input("The weather is bad. Do you want to go to the movies? Enter: True/False:"))
    if movies==True:
        print("We're going to the movies")
    if movies==False:
        print("We're staying home")
if temp_input>=15:
    print("Let's go for a walk, the weather's nice")
    
