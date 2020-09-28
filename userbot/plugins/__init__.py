from userbot import topfunc
from userbot.utils import admin_cmd
from userbot.uniborgConfig import Config


idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isherokuokay = Config.HEROKU_APP_NAME
gdriveisshit = Config.G_DRIVE_AUTH_TOKEN_DATA
sadlifebro = Config.BOTLOG_CHATID
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
datas = topfunc.dbchecker
currentversion = "3.0"

if issudousing:
    amiusingsudo = "Active ✅"
else:
    amiusingsudo = "Inactive ❌"

if islogokay:
    logchat = "Connected ✅"
else:
    logchat = "Dis-Connected ❌"

if isherokuokay:
    riplife = "Connected ✅"
else:
    riplife = "Not Connected ❌"

if gdriveisshit:
    wearenoob = "Active ✅"
else:
    wearenoob = "Inactive"

if sadlifebro:
    okpro = "Connected ✅"
else:
    okpro = "Dis-Connected ❌"

if rmbg:
    gendu = "Added ✅"
else:
    gendu = "Not Added ❌"

if wttrapi:
    starknoobs = "Added ✅"
else:
    starknoobs = "Not Added ❌"

if hmmok:
    meiko = "Added ✅"
else:
    meiko = "Not Added ❌"

inlinestats = (f"SHOWING FRIDAY STATS"
               f"VERSION = {currentversion} \n"
               f"DATABASE = {datas} \n"
               f"SUDO = {amiusingsudo} \n"
               f"LOG-CHAT = {logchat} \n"
               f"HEROKU = {riplife} \n"
               f"G-DRIVE = {wearenoob} \n"
               f"BOTLOG = {okpro} \n"
               f"WEATHER = {starknoobs} \n"
               f"LYDIA = {meiko} \n"
               f"RMBG = {gendu}")
