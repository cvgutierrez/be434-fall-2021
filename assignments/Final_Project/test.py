import os
from subprocess import getstatusoutput, getoutput

ENG = './inputs/english_inputs.txt'
PRO = './project.py'
# --------------------------------------------------
def run(args, expected_file):
    """ Run test """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    rv, out = getstatusoutput(f'{PRO} {" ".join(args)}')
    assert rv == 0
    assert out.strip() == expected

# --------------------------------------------------
def run_outfile(args, expected_file):
    """ Run test """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    outfile = random_string()
    try:
        rv, out = getstatusoutput(f'{PRO} -o {outfile} {" ".join(args)}')
        assert rv == 0
        assert out.strip() == ""
        assert os.path.isfile(outfile)
        assert open(outfile).read().rstrip() == expected
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)

# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRO)

# --------------------------------------------------
def test_stops_with_no_file_or_string():
    """ Program exists """

    run([], "There was nothing to translate. Please try again and input either a file or string.")

# --------------------------------------------------
def test_english_to_spanish():
    """ Program exists """

    run(['english', 'spanish', ENG],'./expected/expected_spanish.txt')

# --------------------------------------------------
def test_english_to_german():
    """ Program exists """

    run(['english', 'german', ENG],'./expected/expected_german.txt')