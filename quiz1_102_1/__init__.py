import check50
from re import escape

@check50.check()
def exists():
    """censor.py exists"""
    check50.exists("censor.py")

@check50.check(exists)
def testBitch():
    """input of \"Hey, stop your bitching\" yields output of \"Censor sentence: Hey, stop your b***hing\""""
    check50.run("python3 censor.py").stdin("Hey, stop your bitching", prompt=True).stdout(regex("Censor sentence: Hey, stop your b\*\*\*hing"), "Censor sentence: Hey, stop your b\*\*\*.hing", regex=True).exit()

@check50.check(exists)
def testDamn():
    """input of \"Damn you\" yields output of \"Censor sentence: D**n you\""""
    check50.run("python3 censor.py").stdin("Damn you", prompt=True).stdout(regex("Censor sentence: D\*\*n you"), "Censor sentence: D\*\*n you", regex=True).exit()

@check50.check(exists)
def testAsshole():
    """input of \"What an asshole\" yields output of \"Censor sentence: What an a*****e\""""
    check50.run("python3 censor.py").stdin("What an asshole", prompt=True).stdout(regex("Censor sentence: What an a\*\*\*\*\*e"), "Censor sentence: What an a\*\*\*\*\*e", regex=True).exit()

@check50.check(exists)
def testShit():
    """input of \"Holy shit\" yields output of \"Censor sentence: Holy s**t\""""
    check50.run("python3 censor.py").stdin("Holy shit", prompt=True).stdout(regex("Censor sentence: Holy s\*\*t"), "Censor sentence: Holy s\*\*t", regex=True).exit()

@check50.check(exists)
def testFuck():
    """input of \"I fucking hate you\" yields output of \"Censor sentence: I f**king hate you\""""
    check50.run("python3 censor.py").stdin("I fucking hate you", prompt=True).stdout(regex("Censor sentence: I f\*\*king hate you"), "Censor sentence: I f\*\*king hate you", regex=True).exit()

@check50.check(exists)
def testMultiple():
    """input of \"Damn, you're shit out of luck!\" yields output of \"D**n, you're s**t out of luck!\""""
    check50.run("python3 censor.py").stdin("Damn, you're shit out of luck!", prompt=True).stdout(regex("Censor sentence: D\*\*n, you're s\*\*t out of luck!"), "Censor sentence: D\*\*n, you're s\*\*t out of luck!", regex=True).exit()

def regex(answer):
    """match case-sensitively with only whitespace on either side"""
    return fr'^.*{escape(answer)}\s*$'
