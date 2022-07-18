import check50


@check50.check()
def exists():
    """input.py exists"""
    check50.exists("input.py")

@check50.check(exists)
def testhello():
    """input of hello yields output of hello"""
    check50.run("python3 input.py").stdin("hello", prompt=False).stdout("hello").exit()

@check50.check(exists)
def testcs50():
    """input of This is cpe113 yields output of this is cs50"""
    check50.run("python3 input.py").stdin("This is cpe113", prompt=False).stdout("This is cpe113").exit()

@check50.check(exists)
def testnumber():
    """input of 50 yields output of 50"""
    check50.run("python3 input.py").stdin("50", prompt=False).stdout("50").exit()
