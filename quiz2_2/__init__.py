import check50
from re import escape


@check50.check()
def exists():
    """score.py exists"""
    check50.exists("score.py")


@check50.check(exists)
def test_sakon():
    """input score"""
    input = "sakon nakhon"
    check50.run("python3 score.py").stdin("A", prompt=True).stdin("30", prompt=True).stdin("20", prompt=True).stdin("30", prompt=True) \
    .stdin("B", prompt=True).stdin("20", prompt=True).stdin("10", prompt=True).stdin("30", prompt=True) \
    .stdin("C", prompt=True).stdin("10", prompt=True).stdin("10", prompt=True).stdin("10", prompt=True) \
    .stdin("", prompt=True).stdin("0", prompt=True).stdin("0", prompt=True).stdin("0", prompt=True) \
    .exit()
