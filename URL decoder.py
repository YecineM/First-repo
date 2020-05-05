#decode a hex url:
#even for complex encodings (encoded encoded URLs)

import re
url=input('write URL to decode')

url=url.replace("%25","%")  #first step, in case we have encoded encoded URL which means encoded "%"

ls=re.findall(r"(?:%[\dABCDEF]{2})+",url)
ls=[sub.split("%")[1:] for sub in ls]
ls=[[int(i,16) for i in lls] for lls in ls]
ls=[bytes(n) for n in ls]
for b in ls:
    url=re.sub(r"(%[\dABCDEF]{2})+",b.decode("utf8"),url, count=1)
print(url)
input("""Now you can copy your URL.
Press some key (followed by Enter) to exit""")
