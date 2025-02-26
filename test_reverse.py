import reverse


def test_reverse_text():
    if reverse.reverse_text("hello") == "olleh":
        print(" is OK")
    else:
        print(" is Fail")

    if reverse.reverse_text("Python") == "nohtyP":
        print(" is OK")
    else:
        print(" is Fail")

    if reverse.reverse_text("989843") == "348989":
        print(" is OK")
    else:
        print(" is Fail")

    if reverse.reverse_text(" -") == " -":
        print(" is OK")
    else:
        print(" is Fail")

test_reverse_text()
