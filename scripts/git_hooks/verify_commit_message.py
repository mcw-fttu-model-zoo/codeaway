import sys
import re

PREFIX = "|".join(["#"])
REGEX = f"^({PREFIX})(\d+\:\ .)"

""" Format of the commit message should be as follows: """
MSG = "#<GIT ISSUE NUMBER> : <mandatory message>"

if __name__ == "__main__":
    argv = sys.argv
    argc = len(sys.argv)

    assert argc == 2, f"Two args expected"

    arg1 = argv[1]

    with open(arg1) as file:
        cmt_msg = file.read()

    res = re.search(REGEX, cmt_msg)

    if not res:
        print("\t --- Commit message ---: \n", cmt_msg)
        raise Exception(f"Expected format for Commit message: {MSG}")

    res_g = res.groups(default=tuple())

    if not res_g:
        print("\t --- Commit message ---: \n", cmt_msg)
        raise Exception("Commit message not validated")
