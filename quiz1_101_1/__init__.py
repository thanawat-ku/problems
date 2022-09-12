import check50

@check50.check()
def exists():
    """censor.py exists"""
    check50.exists("censor.py")

@check50.check(exists)
def testBitch():
    """input of \"Go to hell\" yields output of \"Censor sentence: Go to h**l\""""
    check50.run("python3 censor.py").stdin("Go to hell", prompt=True).stdout(regex("Censor sentence: Go to h\*\*l"), "Censor sentence: Go to h\*\*l", regex=True).exit()

@check50.check(exists)
def testDamn():
    """input of \"He was pissed last night\" yields output of \"Censor sentence: He was p**sed last night\""""
    check50.run("python3 censor.py").stdin("He was pissed last night", prompt=True).stdout(regex("Censor sentence: He was p\*\*sed last night"), "Censor sentence: He was p\*\*sed last night", regex=True).exit()

@check50.check(exists)
def testAsshole():
    """input of \"What a cock block\" yields output of \"Censor sentence: What a c**k block\""""
    check50.run("python3 censor.py").stdin("What a cock block", prompt=True).stdout(regex("Censor sentence: What a c\*\*k block"), "Censor sentence: What a c\*\*k block", regex=True).exit()

@check50.check(exists)
def testShit():
    """input of \"Yeah…he's a moron!\" yields output of \"Censor sentence: Yeah…he's a m***n!\""""
    check50.run("python3 censor.py").stdin("Yeah…he's a moron!", prompt=True).stdout(regex("Censor sentence: Yeah…he's a m\*\*\*n!"), "Censor sentence: Yeah…he's a m\*\*\*n!", regex=True).exit()

@check50.check(exists)
def testFuck():
    """input of \"He screamed like a girl when he saw that snake. What a pussy\" yields output of \"Censor sentence: He screamed like a girl when he saw that snake. What a p***y\""""
    check50.run("python3 censor.py").stdin("He screamed like a girl when he saw that snake. What a pussy", prompt=True).stdout(regex("Censor sentence: He screamed like a girl when he saw that snake. What a p\*\*\*y"), "Censor sentence: He screamed like a girl when he saw that snake. What a p\*\*\*y", regex=True).exit()

@check50.check(exists)
def testMultiple():
    """input of \"To hell with it! What a cock block!\" yields output of \"To h**l with it! What a c**k block!\""""
    check50.run("python3 censor.py").stdin("To hell with it! What a cock block!", prompt=True).stdout(regex("Censor sentence: To h\*\*l with it! What a c\*\*k block!"), "Censor sentence: To h\*\*l with it! What a c\*\*k block!", regex=True).exit()

def regex(answer):
    """match case-sensitively with only whitespace on either side"""
    return rf'^\s*{answer}\s*$'
