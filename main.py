def main():
    TAGS = {
        "": "p",
        "#": "h1",
        "##": "h2",
        "*": "li"
    }
    INSIDETAGS = {
        "li": False,
    }
    notefile = open("notes.md", "r")
    lines = notefile.readlines()
    body = []
    li = False
    for i in lines:
        s = []
        for ii in i:
            if ii in " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRQSTUVWXYZ0123456789":
                break
            else:
                s.append(ii)
        s = "".join(s)
        rest = i.replace(s, "")
        if TAGS[s] == "li":
            if li:
                body.append(f"<{TAGS[s]}>\n\t{rest}</{TAGS[s]}>\n")
            else:
                li = True
                body.append(f"<ul>\n<{TAGS[s]}>\n\t{rest}</{TAGS[s]}>\n")
        else:
            if li:
                li = False
                body.append(f"</ul>\n<{TAGS[s]}>\n\t{rest}</{TAGS[s]}>\n")
            else:
                body.append(f"<{TAGS[s]}>\n\t{rest}</{TAGS[s]}>\n")
    with open("newpage.html", "w") as f:
        with open("page.html", "r") as r:
            code = r.read().replace("PYTHON_CODE", "\n".join(body))
            f.write(code)




if __name__ == '__main__':
    main()
