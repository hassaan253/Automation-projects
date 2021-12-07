#Coin flip streak
import random
num_streaks = 0
heads_or_tails = [] #empty lsit to hold results
#experiment repeated 10,000 times
for experiment in range(1000):

    for j in range(100):
    #create a list of 100 'heads' or 'tails' at random
        x = random.randint(0,1) #choose 1 or 0 at random
        # 1 is heads and 0 is tails
        if (x == 0):
            heads_or_tails.append(0)
        else:
            heads_or_tails.append(1)
#check if there is a continous row of same results
    for i in range(len(heads_or_tails)):
        if (i < (len(heads_or_tails) - 6)):
            if (heads_or_tails[i] == heads_or_tails[i+1]):
                if (heads_or_tails[i+1] == heads_or_tails[i+2]):
                    if (heads_or_tails[i+2] == heads_or_tails[i+3]):
                        if (heads_or_tails[i+3] == heads_or_tails[i+4]):
                            if (heads_or_tails[i+6] == heads_or_tails[i+5]):
                                num_streaks += 1
                                #if 6 consecutive heads or tails found, break the loop
                                break

print(num_streaks)
#calculate percentage of times we got a streak of 6 consecutive heads or tails
print("Chance of streak: %s%%" %((num_streaks / 100)))
