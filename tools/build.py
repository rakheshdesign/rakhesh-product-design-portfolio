"""Usage: python3 tools/build.py [--write]
Reads source/*.dc.html (or $PORTFOLIO_SRC), shows which live pages would change; --write rewrites them.
Run tools/lint.py first."""
import sys,re,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from export import *
def blobmap_for(n):
    m=open(SRC+n+'.dc.html').read(); lp=open(outpath(n)).read()
    mp={}; ks={}
    for x in re.finditer(r'/img/([0-9a-f]{12})\.webp(.{0,90})',lp,re.S): ks.setdefault(x.group(2),set()).add('/img/'+x.group(1)+'.webp')
    for x in re.finditer(r'/_blob/([0-9a-f]{32})(.{0,90})',m,re.S):
        c=ks.get(x.group(2))
        if c and len(c)==1: mp[x.group(1)]=list(c)[0]
    ka={}
    for x in re.finditer(r'(?:src|"cover": )"?/img/([0-9a-f]{12})\.webp"?,? ?(?:alt=|"coverAlt": )"([^"]*)"',lp): ka.setdefault(x.group(2),set()).add('/img/'+x.group(1)+'.webp')
    for x in re.finditer(r'(?:src="|"cover": ")/_blob/([0-9a-f]{32})"[, ]+(?:alt=|"coverAlt": )"([^"]*)"',m):
        c=ka.get(x.group(2))
        if c and len(c)==1: mp[x.group(1)]=list(c)[0]
    return mp
def seqmap(n):
    m=open(SRC+n+'.dc.html').read(); lp=open(outpath(n)).read()
    return re.findall(r'/_blob/([0-9a-f]{32})',m), re.findall(r'(/img/[0-9a-f]{12}\.webp)',lp)
for n in [k for k in ROUTE if os.path.exists(SRC+k+'.dc.html')]:
    bm=blobmap_for(n)
    if n=='Work':
        b,i=seqmap(n); bm.update(dict(zip(b,i)))
    out=export(n,outpath(n),write_img=True,blobmap=bm)
    live=open(outpath(n)).read()
    print(n,'IDENTICAL' if out==live else 'CHANGED')
    if '--write' in sys.argv and out!=live: open(outpath(n),'w').write(out)
