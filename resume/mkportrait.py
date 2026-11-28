"""Regenerates portrait_c2.jpg: Collaboration sign board moved behind the head.
Needs the original photo (COLLAB_PHOTO=path, kept privately) and cut_isnet-general-use.png made with rembg (model isnet-general-use)."""
import os
from PIL import Image, ImageFilter
src=Image.open(os.environ.get('COLLAB_PHOTO','Collaboration.jpeg')).convert('RGB')
cut=Image.open('cut_isnet-general-use.png')
a=cut.split()[3].filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
X0,Y0,S=1119,640,1000
bg=src.crop((X0,Y0,X0+S,Y0+S)).convert('RGBA')
board=src.crop((200,280,2040,578)); bw,bh=board.size
sc=0.72
board=board.resize((int(bw*sc),int(bh*sc)),Image.LANCZOS)
tcx=(806-200)*sc; tcy=(432-280)*sc
px=int(530-tcx); py=int(238-tcy)
sh=Image.new('L',bg.size,0); sh.paste(Image.new('L',board.size,110),(px+6,py+12)); sh=sh.filter(ImageFilter.GaussianBlur(14))
bg.paste((40,20,40,255),(0,0),sh); bg.paste(board.convert('RGBA'),(px,py))
person=src.copy().convert('RGBA'); person.putalpha(a)
bg.alpha_composite(person.crop((X0,Y0,X0+S,Y0+S)))
out=bg.convert('RGB').filter(ImageFilter.UnsharpMask(radius=1.2,percent=40,threshold=2))
out.save('portrait_c2.jpg',quality=96,subsampling=0); out.resize((500,500)).save('pc2.png')
