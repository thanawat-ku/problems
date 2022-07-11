import check50

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.py")

@check50.check(exists)
def testhello():
    """output of hello, world"""
    check50.run("python3 hello.py").stdout("hello, world").exit()
