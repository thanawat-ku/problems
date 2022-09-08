import check50
from re import escape


@check50.check()
def exists():
    """water.py exists"""
    check50.exists("water.py")


@check50.check(exists)
def test_0():
    """usage unit = 0"""
    input = "0"
    output = "Cost of water usage: 0 Baht"
    check50.run("python3 water.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_minus10():
    """usage unit = -10"""
    input = "-10"
    check50.run("python3 water.py").stdin(input, prompt=True).stdin(input, prompt=True).stdin(input, prompt=True).kill()


@check50.check(exists)
def test_5():
    """usage unit = 5"""
    input = "5"
    output = "Cost of water usage: 0 Baht"
    check50.run("python3 water.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_50():
    """usage unit = 50"""
    input = "50"
    output = "Cost of water usage: 400 Baht"
    check50.run("python3 water.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(answer):
    """match case-insensitively with only whitespace on either side"""
    return rf'(?i)^\s*{answer}\s*$'
