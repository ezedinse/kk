import asyncio
import os
import json
cookie="SRCHUSR=DOB=20240127&T=1706946333000;_Rwho=u=d;GC=g2XO9FeW68xH3R2R2MsJSS3ougavNL-qtkRNIhHit95bYojwphDhuuIe1k8iypuHOfeiBfNDrR3Hi-bUnoNfFQ;SRCHHPGUSR=SRCHLANG=en&PV=6.1.0&IG=8FB61D2D252A43B8A55D6DF53AE9EB56&BRW=W&BRH=S&CW=1358&CH=655&SCW=1343&SCH=3153&DPR=1.0&UTC=180&DM=0&CIBV=1.1536.2&EXLTT=2&PRVCW=1358&PRVCH=655&HV=1706947373;ANON=A=CF14E7795DE5F91C83BFB560FFFFFFFF;_clsk=15ah7x7%7C1706947796927%7C4%7C1%7Cu.clarity.ms%2Fcollect;_SS=SID=11D351CD658C6620306F45D7647067A2&R=54&RB=54&GB=0&RG=0&RP=51&PC=U531;ipv6=hit=1706950931002&t=4;_U=1-d3OYvTCwetPRJA57SK5kjH8Tlr8uyULPU2eWzRJ1f6-n98ddmOUUcM-0tiwADxKVPWAcVW2_B6SwFq0lbMiDQWS5fnYRU3CwSgGRp1TPW9bDhlj5EPrHK36kVht4CDyBCGHeMJlc-6XH6SI34ue1VEVMMflq_ItnxZrEqPukXaCMjejQw8DzNQ0IPwaoGLSW7XL3jcJOlWWqUY_IWUwXg;SRCHD=AF=NOFORM;_RwBf=mta=0&rc=54&rb=54&gb=0&rg=0&pc=51&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=2&l=2024-02-03T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=0001-01-01T16:00:00.0000000-08:00&o=0&p=BINGCOPILOTWAITLIST&c=MR000T&t=8516&s=2023-05-05T15:29:38.2271701+00:00&ts=2024-02-03T08:02:13.9500619+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=0&lka=0&lkt=0&aad=0&TH=&e=wneWW4uiC8uGs0Q_I6G7nqapbtHqGpKKXH-tNPFqnZMluDiq0Z61qii_pC3PZThVH7a272c1lI0pU0M0RAL7WQ&A=&rwflt=0001-01-01T16:00:00.0000000-08:00;_EDGE_S=SID=11D351CD658C6620306F45D7647067A2;MUIDB=2AE42A744DF167AC3FA23E674C7366AF;USRLOC=HS=1&ELOC=LAT=9.020730018615723|LON=38.72129821777344|N=Addis%20Ababa%2C%20Addis%20Ababa|ELT=4|;_clck=18qe2yy%7C2%7Cfiy%7C0%7C1494;EDGSRCHHPGUSR=CIBV=1.1525.2;MUID=2AE42A744DF167AC3FA23E674C7366AF;SRCHS=PC=U531;SRCHUID=V=2&GUID=EE7966B4116D45A290802A08FB54B9D1&dmnchg=1;WLS=C=e33af3b4d93551b9&N=ezedin"
from sydney import SydneyClient
pre="""You are An IQ Quiz Answering bot. you answer only the specific answer. there is no explanation for the answer
#Rulls
-- give only the specific answer 
-- no further explanation
-- not making statement or sentence
-- only the specific answer like calculator 
-- the answer have to be so accurate and because the answer is needed for giving the right answer for the students who take the exam please be acurate as much as possible
-- the answer have to be so accurate and because the answer is needed for giving the right answer for the students who take the exam please be acurate as much as possible
-- if the answer is number like 2: 11 stop adding the phrase the answer is 2: 11
-- all the question's asked are only on two forms the ferist one is chose the second is Arange
--the chose qn is like "what is 5+6. 0:12 1:11 2:7 3:6" and include the index number before :
-- the arrange qn is like "Arrange the following on descending order 0:2 1:3 2:1 3:5"
-- the answer for the chose qn must be like '1:11' 
-- the answer for the arrange qn must be like '3,1,2,0'
-- you have to use the above rules"""
os.environ["BING_COOKIES"]=cookie
async def main() -> None:
    async with SydneyClient(style='precise') as sydney:
        async for response in sydney.ask_stream(pre):
            print(response, end="", flush=True)
        while True:
            prompt = input("You: ")

            if prompt == "!reset":
                await sydney.reset_conversation()
                continue
            elif prompt == "!exit":
                break

            print("Sydney: ", end="", flush=True)
            response = await sydney.ask(prompt)
            print(response)
            # async for response in sydney.ask_stream(prompt):
            #     print(response, end="", flush=True)
            print("\n")


if __name__ == "__main__":
    asyncio.run(main())
