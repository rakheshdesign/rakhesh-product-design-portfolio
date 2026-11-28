import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sys
from pypdf import PdfReader,PdfWriter
from pypdf.generic import RectangleObject
for n in sys.argv[1:]:
    r=PdfReader(n+'.pdf'); w=PdfWriter()
    for p in r.pages:
        H=float(p.mediabox.height); W=595.5; Hc=842.25
        box=RectangleObject([0,0,W,Hc])
        p.mediabox=box; p.cropbox=box; p.trimbox=box; p.bleedbox=box; p.artbox=box
        w.add_page(p)
    w.write(n+'_c.pdf')
