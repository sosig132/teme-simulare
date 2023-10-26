from random import sample, randint

#first method(bad)

print("Starting...")

prisoners = sample(range(1, 101), 100)



done = 0

print("Calculating...")

def first_method():
    global done
    drawers = [0]+sample(range(1, 101), 100)

    prisoners_found=0
    for prisoner in prisoners:
        set_of_chosen_drawers = set()
        check_if_prisoner_found=0
        for _ in range(51):
            x=0
            while x in set_of_chosen_drawers:
                x = randint(1,100)
            if(x == prisoner):
                check_if_prisoner_found=1
                prisoners_found+=1
                break
                
            else:
                set_of_chosen_drawers.add(x)

        #if(check_if_prisoner_found==1):
    
    done+=1
    if(done%100==0):
        print(f"Done {done} iterations")

    return prisoners_found



def second_method():    
    global done
    drawers = [0]+sample(range(1, 101), 100)

    prisoners_found=0
    for prisoner in prisoners:
        x=prisoner
        for _ in range(50):
            if drawers[x]==prisoner:
                prisoners_found+=1
                break
            else:
                x=drawers[x]
                
    
    done+=1
    if(done%1000==0):
        print(f"Done {done} iterations")

    print("YES: ",prisoners_found) if prisoners_found>80 else None
    return prisoners_found 

yes=0

for i in range(10000):
    if second_method()==100:
        print(f"Yes on iteration: {i}")
        yes+=1

print(yes)   

