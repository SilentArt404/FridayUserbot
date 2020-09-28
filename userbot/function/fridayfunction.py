# Copyright (C) By @StarkGang And @ZeltraxRockz
# Powered By @Nemo_Projects
# CREDIT - DATABASE CHECHER
# UniBorg Telegram Userbot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
#  @UniBorg (C) By @Spechide


import random
import string


# String Finder
def stark_finder(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


# Id Generator
def id_generator(size=64, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def dbchecker():
    is_database_working = False
    output = "No DATABASE Found !"
    if not Var.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION
    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output
