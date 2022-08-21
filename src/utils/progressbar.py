import sys
import utils.misc as msg

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    """
    Custom progress bar.
     Arguments:
        `it` Number of items
         `prefix` Informative message near bar
        `size` The size of th bar
         `out` Output 
    """
    count = len(it)
    try:
        def show(j):
            x = int(size*j/count)
            print("{}[{}{}] {}/{}".format(prefix, msg.LOAD*x, msg.DOT*(size-x), j, count), # █
                   end='\r', file=out, flush=True)
    except Exception:
        pass
    show(0)
    try:
        for i, item in enumerate(it):
            yield item
            show(i+1)
    except Exception:
        pass
    print( flush=True, file=out)


#for i in progressbar(range(15), "Computing: ", 40):
#   time.sleep(0.1) # any code you need