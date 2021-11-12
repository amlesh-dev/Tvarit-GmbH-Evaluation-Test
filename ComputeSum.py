def computeSum(args):
    if(len(args)<3):
        return "Exactly 3 numbers are required"

    a, b, c = ([None if type(v) is str else v for v in args])
    if(not a or not b or not c):
        return "All inputs must be numeric"
    else:    
        s = a+b+c
        if(a>=13 and a<=19 and a!=15 and a!=16):
            s-=a
        if(b>=13 and b<=19 and b!=15 and b!=16):
            s-=b
        if(c>=13 and c<=19 and c!=15 and c!=16):
            s-=c

        return s
  


