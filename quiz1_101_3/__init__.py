import check50
from re import escape


@check50.check()
def exists():
    """electricity.py exists"""
    check50.exists("electricity.py")


@check50.check(exists)
def test_0():
    """usage unit = 0"""
    input = "0"
    output = "Cost of electricity usage: 0 Baht"
    check50.run("python3 electricity.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_minus10():
    """usage unit = -100"""
    input = "-100"
    check50.run("python3 electricity.py").stdin(input, prompt=True).stdin(input, prompt=True).stdin(input, prompt=True).kill()


@check50.check(exists)
def test_50():
    """usage unit = 50"""
    input = "50"
    output = "Cost of electricity usage: 0 Baht"
    check50.run("python3 electricity.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_100():
    """usage unit = 100"""
    input = "100"
    output = "Cost of electricity usage: 0 Baht"
    check50.run("python3 electricity.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_300():
    """usage unit = 300"""
    input = "300"
    output = "Cost of electricity usage: 800 Baht"
    check50.run("python3 electricity.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_140():
    """usage unit = 140"""
    input = "140"
    output = "Cost of electricity usage: 160 Baht"
    check50.run("python3 electricity.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

def regex(answer):
    """match case-sensitively with only whitespace on either side"""
    return rf'^\s*{answer}\s*$'
