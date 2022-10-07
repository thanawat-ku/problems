import check50
from re import escape, sub

"""
setup
"""


@check50.check()
def exists():
    """numb3rs.py exists"""
    check50.exists("numb3rs.py")
    check50.include("testing.py")

"""
numb3rs.py checks
"""

@check50.check(exists)
def test_correct_ipv4_localhost():
    """numb3rs.py prints True for 127.0.0.1"""
    input = "127.0.0.1"
    output = "True"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_correct_ipv4_broadcast():
    """numb3rs.py prints True for 255.255.255.255"""
    input = "255.255.255.255"
    output = "True"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_correct_ipv4_harvard():
    """numb3rs.py prints True for 140.247.235.144"""
    input = "140.247.235.144"
    output = "True"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_incorrect_out_of_range():
    """numb3rs.py prints False for 256.255.255.255"""
    input = "256.255.255.255"
    output = "False"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_incorrect_out_of_range2():
    """numb3rs.py prints False for 64.128.256.512"""
    input = "64.128.256.512"
    output = "False"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_incorrect_ipv6():
    """numb3rs.py prints False for 2001:0db8:85a3:0000:0000:8a2e:0370:7334"""
    input = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    output = "False"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_non_ip():
    """numb3rs.py prints False for cat"""
    input = "cat"
    output = "False"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)



"""
Helpers
"""

def regex(text):
    """match case-insensitively, allowing for only whitespace on either side"""
    return fr'^(?i)\s*{escape(text)}\s*$'
