#This contains the point function
def points(a,b,c):
    slope=b[1]-a[1]/(b[0]-a[0])
    y=(slope*(c-b[0]))+b[1]
    return y
