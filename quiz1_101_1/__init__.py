import check50

@check50.check()
def exists():
    """censor.py exists"""
    check50.exists("censor.py")

@check50.check(exists)
def testBitch():
    """input of \"Hey, stop your bitching\" yields output of \"Censor sentence: Hey, stop your b***hing\""""
    output = check50.run("python3 censor.py").stdin("Hey, stop your bitching", prompt=False).stdout("Censor sentence: Hey, stop your b***hing").exit()

@check50.check(exists)
def testDamn():
    """input of \"Damn you\" yields output of \"Censor sentence: D**n you\""""
    output = check50.run("python3 censor.py").stdin("Damn you", prompt=False).stdout("Censor sentence: D**n you").exit()

@check50.check(exists)
def testAsshole():
    """input of \"What an asshole\" yields output of \"Censor sentence: What an a*****e\""""
    output = check50.run("python3 censor.py").stdin("What an asshole", prompt=False).stdout("Censor sentence: What an a*****e").exit()

@check50.check(exists)
def testShit():
    """input of \"Holy shit\" yields output of \"Censor sentence: Holy s**t\""""
    output = check50.run("python3 censor.py").stdin("Holy shit", prompt=False).stdout("Censor sentence: Holy s**t").exit()

@check50.check(exists)
def testShit():
    """input of \"I fucking hate you\" yields output of \"Censor sentence: I f**king hate you\""""
    output = check50.run("python3 censor.py").stdin("I fucking hate you", prompt=False).stdout("Censor sentence: I f**king hate you").exit()

@check50.check(exists)
def testMultiple():
    """input of \"Damn, you're shit out of luck!\" yields output of \"D**n, you're s**t out of luck!\""""
    output = check50.run("python3 censor.py").stdin("Damn, you're shit out of luck!", prompt=False).stdout("Censor sentence: Damn, you're shit out of luck!").exit()
