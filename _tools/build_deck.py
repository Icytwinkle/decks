import sys, cairosvg
from PIL import Image
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
import pypdfium2 as pdfium
svg, name, out = sys.argv[1], sys.argv[2], sys.argv[3]
H = float(sys.argv[4]) if len(sys.argv)>4 else 46.0
cairosvg.svg2png(url=svg, write_to='/tmp/_l.png', output_width=2000)
im=Image.open('/tmp/_l.png').convert('RGBA'); im=im.crop(im.getbbox()); im.save('/tmp/_l.png')
lw,lh=im.size; W=H*lw/lh
if W>150: W=150; H=W*lh/lw
cx, cy = 157.5, 340.0
c=canvas.Canvas('/tmp/_ov.pdf',pagesize=(720,405))
c.drawImage('/tmp/_l.png',cx,405-(cy+H/2),width=W,height=H,mask='auto'); c.showPage(); c.save()
r=PdfReader('master_clean.pdf'); ov=PdfReader('/tmp/_ov.pdf').pages[0]; w=PdfWriter()
for i,p in enumerate(r.pages):
    if i==0: p.merge_page(ov)
    w.add_page(p)
w.add_metadata({'/Title':f'Twinkle x {name}'}); w.write(out)
pdfium.PdfDocument(out)[0].render(scale=1).to_pil().crop((0,280,720,405)).save(out+'.png')
print('ok',W,H)
