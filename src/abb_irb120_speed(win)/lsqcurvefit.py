import numpy as np

def Circle_Fit(x,y):
    n=len(x)
    xx=x**2
    yy=y**2
    xy=x*y
    A=np.array([[sum(x),sum(y),n],[sum(xy),sum(yy),sum(y)],[sum(xx),sum(xy),sum(x)]])
    B=np.array([-sum(xx + yy),-sum(xx*y + yy*y),-sum(xx*x +xy*y)]).transpose();
    a=np.linalg.solve(A,B)
    xc=-.5*a[0]
    yc=-.5*a[1]
    r=np.sqrt((a[0]**2+a[1]**2)/4-a[2])
    xc = np.int(xc)
    yc = np.int(yc)
    r = np.int(r)
    # print('xc=%d,yc=%d,r=%d'%(xc,yc,r))
    return xc,yc,r
