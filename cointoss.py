import random
def coinToss():

    head_count = 0
    tail_count = 0

    print "Starting the program..."
    for toss_count in range(1, 5001):
        print toss_count
        toss = round(random.random())
        if toss == 0:
            head_count += 1
            result = 'head'

        else:
            tail_count += 1
            result = 'tail'

        #print "Attempt #" , toss_count , ": Throwin a coin...It's a",result," !...Got " , head_count , "head(s) so far and " , tail_count , "tail(s) so far"
        print "Attempt #{}: Throwing a coin... it's a {}! ...Got {} heads so far and {} tails so far".format(toss_count, result, head_count, tail_count)
    
    print "Ending the program, thank you! "
coinToss()


