import check50
from re import escape


@check50.check()
def exists():
    """weather.py exists"""
    check50.exists("weather.py")


@check50.check(exists)
def test_sakon():
    """weather of sakon"""
    input = "sakon nakhon"
    output = "lat = 17.3333"
    check50.run("python3 weather.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_bangkok():
    """weather of bangkok"""
    input = "lat = 13.75, lon = 100.5197"
    check50.run("python3 weather.py").stdin(input, prompt=True).stdin(input, prompt=True).stdin(input, prompt=True).kill()


def regex(answer):
    """match case-insensitively with only whitespace on either side"""
    return rf'^{answer}.*'
