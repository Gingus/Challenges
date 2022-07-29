# tell the user the target time is 4 seconds
# ---Press Enter to begin ---
# ...Press Enter again after 4 seconds...
# tell player if too fast/slow or right on
# Elapsed time: 4.213 seconds
# (0.213 seconds too slow)
import time
import random

def waiting_game():
    target = random.randint(2,4)
    # INTRO = """This is the waiting game \n,
    #         The target is to stop the timer at {} second \n
    #         The timer starts and stops when you press enter
    #         """
    # print(INTRO)
    print("You'll have {0:3f} to start/stop!".format(target))
    input("\n ----Press Enter to Begin ---- ")
    start = time.perf_counter()
    
    input('\n ...Press Enter again after {} seconds... '.format(target))
    elapsed = time.perf_counter() - start
    
    print('\nElapsed time: {0:3f} seconds'.format(elapsed))
    if elapsed == target:
        print('Unbelievanble! Perfect Timing :D')
    elif elapsed < target:
        print('({0:3f} seconds too fast)'.format(target - elapsed))
    else:
        print('({0:3f} seconds too slow)'.format(elapsed - target))


