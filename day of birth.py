# Just for fun

# Input : birth date
# Output: day of the week you were born on !
 
# Input format : Month,Day,year
# Example: 3/15/2000
#       or 3,15,2000
#       or 3 15 2000

from datetime import date
import re
i=input()
r=re.search(r"(\d+).(\d+).(\d+)",i)
m=int(r.group(1))
d=int(r.group(2))
y=int(r.group(3))
dic={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
day=dic[date(y,m,d).weekday()]
print("You were born on",day,"!")
