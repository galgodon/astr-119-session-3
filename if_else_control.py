#!/usr/bin/env python3

def flow_control(k):                # define a function with input k
    # check if k is 0, 1,or neither and create a string 's' accordingly
    if (k==0):
        s = 'Variable k = %d equals 0.' % k      # %d means print k in base 10 (as an integer) 
        
    elif(k==1):
        s = 'Variable k = %d equals 1.' % k
        
    else:
        s = 'Variable k = %d does not equal 0 or 1.' % k
        
    print(s)                        # print s
    
def main():
    for i in range(3):              # loop i through values 0,1,2
        flow_control(i)             # run the flow_control function at each i
if __name__ == '__main__':          # run the main function
    main()