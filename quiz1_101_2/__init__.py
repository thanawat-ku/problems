import check50
from re import escape


@check50.check()
def exists():
    """sort_name.py exists"""
    check50.exists("sort_name.py")


@check50.check(exists)
def test_change():
    """list of student name"""
    output="List of sorted students\nRon\nPadma\nHermione\nHarry\nDraco"
    check50.run("python3 sort_name.py").stdin("Ron", prompt=True).stdin("Harry", prompt=True).stdin("Hermione", prompt=True).stdin("Draco", prompt=True).stdin("Padma", prompt=True).stdout(regex(output), output, regex=True).exit()

def regex(answer):
    """match case-sensitively with only whitespace on either side"""
    return rf'^\s*{answer}\s*$'
