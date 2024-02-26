U='Authorization'
T=False
Q='Invalid server ID.'
N=Exception
K=str
I=True
G=int
F=input
E=''
D=range
A=print
import discord as R,colorama as V,string as B,requests as J,random as C,asyncio,sys as O,time as P,pyfiglet as W,faker
from discord.ext.commands.core import bot_has_permissions
from colorama import Fore as L,Back,Style
from discord.ext import commands as X
from faker import Faker
S=R.Intents.all()
S.dm_messages=I
H=X.Bot(command_prefix='!',self_bot=I,intents=S)
V.init(autoreset=I)
def Y():A(L.RED+'\n\n\n╔═════════════════════════════╗                                   ░█░█░█▀█░▀█▀░█▀▄░                                     ╔═════════════════════════════╗\n║            @v4z0            ║                                   ░▀▄▀░█░█░░█░░█░█░                                     ║           .gg/pop           ║\n╚═════════════════════════════╝                                   ░░▀░░▀▀▀░▀▀▀░▀▀░░ v2                                  ╚═════════════════════════════╝\n╔═════════════════════════════╦═════════════════════════════════════════════════════════════════════════════════════════╦═════════════════════════════╗\n║ [ + ] Other                 ║                                   [ + ] Generators                                      ║ [ + ] Checkers              ║\n╠═════════════════════════════╬═════════════════════════════╦═════════════════════════════╦═════════════════════════════╬═════════════════════════════╣\n╠═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╣\n║ [ 1 ] Stressers             ║ [ 2 ] Nitro Generator       ║ [ 3 ] Walmart Gift Gen      ║ [ 4 ] Username Gen          ║ [ 5 ] Nitro Code Checker    ║\n╠═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╣\n║ [ 6 ] Databases             ║ [ 7 ] Token Generator       ║ [ 8 ] Amazon Gift Gen       ║ [ 9 ] CC Gen                ║ [ 10 ] Token Checker        ║\n╠═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╣\n║ [ 11 ] Grabbers             ║ [ 12 ] Phone # Gen          ║ [ 13 ] Roblox Gift Gen      ║ [ 14 ] Ascii Text Gen       ║ [ 15 ] IP Checker           ║\n╠═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╣\n║ [ 16 ] Useful Links         ║ [ 17 ] IP Gen               ║ [ 18 ] Xbox Gift Gen        ║ [ 19 ] Identity Gen         ║ [ 20 ] Amazon Checker       ║\n╠═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╣\n╠═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╬═════════════════════════════╣\n║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║ [ 22 ] Credits              ║ [ 23 ] Help                 ║ [ 24 ] Exit                 ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║\n╚═════════════════════════════╩═════════════════════════════╩═════════════════════════════╩═════════════════════════════╩═════════════════════════════╝\n\n'+L.RESET)
def Z(num_cards):
  A=[]
  for J in D(num_cards):B=' '.join([E.join([K(C.randint(0,9))for A in D(4)])for A in D(4)]);F=K(C.randint(100,999));G=K(C.randint(1,12));H=K(C.randint(24,32));I=f"Card Number: {B} CVV: {F} Expiration: {G}/{H}";A.append(I)
  return A
def a():A=F('Enter the text to convert to ASCII art: ');B=W.figlet_format(A);return B
def b(num_letters):return E.join(C.choice(B.ascii_lowercase)for A in D(num_letters))
def c():D=Faker('en_US');F=D.name();G=D.address().replace('\n',', ');H=D.date_of_birth(minimum_age=18,maximum_age=90);I=E.join(C.choices(B.digits,k=3));J=E.join(C.choices(B.digits,k=2));K=E.join(C.choices(B.digits,k=4));L=f"{I}-{J}-{K}";A('Name:',F);A('Address:',G);A('Date of Birth:',H);A('SSN:',L)
def r(token,server_id):
  async def C(guild):
    B=guild
    for E in B.roles:
      try:await E.delete()
      except N as C:A(f"Failed to delete role {E.name}\n{C}")
    A(f"All roles in server {B.name} have been deleted.")
    for F in B.channels:
      try:await F.delete();P.sleep(5)
      except N as C:A(f"Failed to delete channel {F.name}\n{C}")
    A(f"All channels in server {B.name} have been deleted.")
    try:
      G=B.create_text_channel('void');A(f"Created channel {G.name} in server {B.name}.")
      for H in D(5):G.send('@everyone');P.sleep(1)
      A('Sent messages in the channel')
    except R.Forbidden as C:
      if C.code==429:A('Rate limited: Please slow down.');return
      A(f"Failed to create channel or send message: {C}")
  @H.event
  async def B():
    B=H.get_guild(G(server_id))
    if B:await C(B)
    else:A(Q)
  H.run(token)
def d():A=E.join(C.choices(B.ascii_uppercase+B.digits,k=10));return f"{A}"
def e(code):
  A='application/json';B='https://www.amazon.com/asv/reload/order';C={'Content-Type':A,'Accept':A,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'};D={'asin':'REPLACE_WITH_ASIN','gcClaimCode':code,'gcId':'REPLACE_WITH_GC_ID','orderId':'REPLACE_WITH_ORDER_ID','reason':'Reload','reloadAmount':0,'sessionId':'REPLACE_WITH_SESSION_ID','totalAmount':0,'userId':'REPLACE_WITH_USER_ID'};E=J.post(B,headers=C,json=D)
  if E.status_code==200:return I
  else:return T
def f():A=E.join(C.choices(B.ascii_uppercase+B.digits,k=5));D=E.join(C.choices(B.ascii_uppercase+B.digits,k=5));F=E.join(C.choices(B.ascii_uppercase+B.digits,k=5));G=E.join(C.choices(B.ascii_uppercase+B.digits,k=5));H=E.join(C.choices(B.ascii_uppercase+B.digits,k=5));I=f"{A}-{D}-{F}-{G}-{H}";return f"{I}"
def g(length=16):A=B.ascii_letters+B.digits;F=E.join(C.choice(A)for B in D(length));return F
def h():
  I=F('How many codes do you want to generate? : ');H=B.digits
  for L in D(G(I)):J=E.join(C.choice(H)for A in D(16));K=E.join(C.choice(H)for A in D(4));A(f"Code: {J} | Pin: {K}")
def s(token,server_id):
  @H.event
  async def B():
    B=H.get_guild(G(server_id))
    if B:
      for C in B.channels:
        try:await C.delete()
        except N as D:A(f"Failed to delete channel {C.name}\n{D}")
      A(f"All channels in server {B.name} have been deleted.")
    else:A(Q)
  H.run(token)
def t(token,server_id):
  @H.event
  async def B():
    B=H.get_guild(G(server_id))
    if B:
      for C in B.roles:
        try:await C.delete()
        except N as D:A(f"Failed to delete role {C.name}\n{D}")
      A(f"All roles in server {B.name} have been deleted.")
    else:A(Q)
  H.run(token)
def M(text,delay=.1):
  for A in text:O.stdout.write(A);O.stdout.flush();P.sleep(delay)
  O.stdout.write('\n')
def i(code):
  A={U:'Bot MTIwMjY4MTE3MjU5ODE5NDMxNg.GRmnRi.FiiJEafZJ9moxkAK2_hRYBQjL-qfuaYeVjPZmA'};B=J.post(f"https://discord.com/api/v9/entitlements/gift-codes/{code}/redeem",headers=A)
  if B.status_code==200:return I
  else:return T
def j(ip):
  A=J.get(f"https://ipinfo.io/{ip}/json?token=0894eed8043489")
  if A.status_code==200:return A.json()
  else:return
def k():
  A=[]
  for B in D(4):A.append(K(C.randint(0,255)))
  return'.'.join(A)
def l():A=E.join(C.choice(B.ascii_letters+B.digits)for A in D(59));return f"Mj{A}.{C.choice(['a','o'])}_Yg"
def m():A='-'.join(E.join(C.choices(B.ascii_uppercase+B.digits,k=5))for A in D(3));return A
def u():
  A=F('Enter the webhook URL: ');B=F('Enter the message to spam: ');C=G(F('Enter the number of times to spam the message (max 5): '))
  for H in D(min(C,5)):E={'content':B};J.post(A,json=E)
def n():A('Help Menu:\n[ 1 ] Sressers - List of IP Stressers\n[ 2 ] Nitro Gen - Nitro Code Gen\n[ 3 ] Walmart Gift Gen - Gen Walmart Gift Codes\n[ 4 ] Username Gen - Gen a username of specified length\n[ 5 ] Nitro Code Checker - Check if a nitro code is valid\n[ 6 ] Databases - List of Database searchers and Forums\n[ 7 ] Token Generator - Gen A DCord Token\n[ 8 ] Amazon Gift Gen - Generate Amazon Gift Cards\n[ 9 ] CC Gen - Generate a CC\n[ 10 ] Token Checker - Check if a Token is valid\n[ 11 ] Grabbers - List of IP Grabbers\n[ 12 ] Phone # Gen - Gen Phone Number\n[ 13 ] Roblox Gift Gen - Gen Roblox Gift Card\n[ 14 ] Ascii Text Gen - Type text and get ascii\n[ 15 ] IP Checker - IP Lookup\n[ 16 ] Useful Links - List of useful links\n[ 17 ] IP Gen - Gen an IP\n[ 18 ] Xbox Gift Gen - Gen Xbox Gift Cards\n[ 19 ] Identity Gen - Generate Fake ID\n[ 20 ] Amazon Checker - Check Amazon Codes\n\n[ 22 ] Credits - Credits \n[ 23 ] Help - This Menu\n[ 24 ] Exit - Exit the program\n    ')
def o(num_numbers=1):
  A=[]
  for I in D(num_numbers):F=E.join(C.choices(B.digits,k=3));G=E.join(C.choices(B.digits,k=3));H=E.join(C.choices(B.digits,k=4));A.append(f"({F}) {G}-{H}")
  return A
def p(token):
  A={U:token};B=J.post('https://discord.com/api/v7/users/@me',headers=A)
  if B.status_code==200:return'Token is valid!'
  else:return'Token is invalid.'
def q():
  E='N/A';Y()
  while I:
    B=F(L.BLUE+'\nEnter an option: '+L.RESET)
    if B=='1':M('\nStressers:\n\nstresse.ru\nstresser.st\nnightmarestresser.net\n')
    elif B=='6':M('\nDatabases / Forums:\n\ncrackingforums.is\ncracked.to\ncracking.org\nxss.is\n\n')
    elif B=='11':M('\nList of useful grabbers:\n\ngrabify.link\niplogger.org\n\n')
    elif B=='16':M('\nUseful links and what they do:\n\nDiscord Servers:\n\nother tools:\nhttps://discord.gg/eintim\ncracked tools:\nhttps://discord.gg/crak2\ncom server:\nhttps://discord.gg/pop\n\nOther Tools:\nhttps://illegal-services.github.io/Illegal_Services/\nhttps://github.com/Xen000000/Lime-Multi-Tool\n\n')
    elif B=='2':
      N=G(F('How many codes do you want to generate? '))
      for J in D(N):H=g();A(f"Code | https://discord.gift/{H}")
    elif B=='5':
      H=F('Enter a Nitro code to check: ')
      if i(H):A('Code is valid!')
      else:A('Code is invalid!')
    elif B=='15':
      O=F('Enter an IP address to lookup: ');C=j(O)
      if C:A(f"IP Address: {C.get('ip',E)}");A(f"City: {C.get('city',E)}");A(f"Region: {C.get('region',E)}");A(f"Country: {C.get('country',E)}");A(f"Loc: {C.get('loc',E)}");A(f"Org: {C.get('org',E)}");A(f"Postal: {C.get('postal',E)}");A(f"Timezone: {C.get('timezone',E)}")
      else:A('Error: Unable to retrieve information for {ip}.')
    elif B=='17':P=k();A(f"Random IP Address: {P}")
    elif B=='24':A('Exiting...');break
    elif B=='7':
      Q=G(F('How many tokens do you want to generate? '))
      for J in D(Q):K=l();A(f"Token: {K}")
    elif B=='8':
      R=G(F('How many gift card codes do you want to generate? '))
      for J in D(R):S=m();A(f"Amazon Gift Card Code: {S}")
    elif B=='23':n()
    elif B=='12':
      T=G(F('How many phone numbers do you want to generate? '));U=o(T)
      for V in U:A(f"Generated Phone Number: {V}")
    elif B=='10':K=F('Enter the token to check: ');A(p(K))
    elif B=='3':h()
    elif B=='13':
      W=G(F('Enter the number of Roblox gift card codes to generate: '))
      for J in D(W):X=d();A('Roblox Gift Card Code:',X)
    elif B=='20':
      H=F('Enter the Amazon gift card code to check: ')
      if e(H):A('Gift card is Invalid.')
    elif B=='18':
      q=G(F('Enter the number of Xbox gift card codes to generate: '))
      for J in D(q):r=f();A('Xbox Gift Card Code:',r)
    elif B=='4':s=G(F('How many letters do you want in the username? '));A(b(s))
    elif B=='9':
      t=G(F('Enter the number of credit cards to generate: '));u=Z(t)
      for v in u:A(v)
    elif B=='14':A(a())
    elif B=='19':c()
    else:A('Invalid option. Please try again.')
if __name__=='__main__':q()