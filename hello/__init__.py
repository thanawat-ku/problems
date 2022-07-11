import check50

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.py")

@check50.check(exists)
def testhello():
    """output of hello"""
    check50.run("python3 heelo.py").stdout("hello").exit()
