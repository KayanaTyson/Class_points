#This contains the point function
def points(a,b,c):
    if a[0]==b[0]:
        y=2
    elif a[1]==b[1]:
        y=1
    else:
        slope=b[1]-a[1]/(b[0]-a[0])
        y=(slope*(c-b[0]))+b[1]
    return y
