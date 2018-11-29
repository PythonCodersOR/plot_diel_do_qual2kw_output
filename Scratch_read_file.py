# do one thing and do it well
# read output file and return contents
# as a string list with rows the lines of the output files

def getoutfile(str_file):
    with open(str_file) as f:
        str_out = f.read().splitlines()
    return str_out

