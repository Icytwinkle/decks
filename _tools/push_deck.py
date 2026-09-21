import base64,json,os,sys,secrets,urllib.request
GH=os.environ['GH']; path_pdf, slugbase, fname = sys.argv[1], sys.argv[2], sys.argv[3]
slug=f"{slugbase}-{secrets.token_hex(4)}"
url=f"https://api.github.com/repos/Icytwinkle/decks/contents/{slug}/{fname}"
body=json.dumps({"message":f"Add {slugbase} deck","content":base64.b64encode(open(path_pdf,'rb').read()).decode()}).encode()
req=urllib.request.Request(url,data=body,method='PUT',headers={'Authorization':f'Bearer {GH}','Accept':'application/vnd.github+json','Content-Type':'application/json'})
urllib.request.urlopen(req).read()
print(f"https://icytwinkle.github.io/decks/{slug}/{fname}")
