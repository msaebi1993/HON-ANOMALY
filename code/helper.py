#import concurrent.futures
import main
import time

    
def helper(arg,MaxOrder,MinSupport):
    fn = arg
    freq_prob='/freqs'
    fnout=None
    rnout=None
    Rules=None
    Network=None
    fnout = '/'.join(fn.split('/')[:2]) +freq_prob+ '/network-portugal-maxorder-'+ str(MaxOrder) +'/' + fn.split('/')[-1]
    rnout='/'.join(fn.split('/')[:2]) +freq_prob+'/rules-portugal-maxorder-'+ str(MaxOrder) +'/' + fn.split('/')[-1]
    
    
    print(fn, fnout)
    t1=time.time()
    main.BuildHONfreq(fn, fnout,rnout,MaxOrder,MinSupport)

    t2=time.time()
    print("Running time: ",str(t2-t1))