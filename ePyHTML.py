"""
MADE BY MCTVR
MIT LICENSE
GITHUB ONLY
OPEN SOURCED
WILL UPDATE FREQUENTLY
V 0.3
"""
import re
from os import path

def startHTML(name_of_file, extension="", title="", css_path=""):
    if extension == "":
        name_of_file = str(name_of_file + ".html")
    elif "html" in extension:
        name_of_file = str(name_of_file + ".html")
    elif "php" in extension:
        name_of_file = str(name_of_file + ".php")
    else:
        print("ePyHTML only supports html and php extensions!")

    global html
    if path.isfile(name_of_file):
        print("File exists, ePyHTML will edit it for appending")
        html = open(name_of_file, "a")
    elif path.isfile(name_of_file) == False:
        html = open(name_of_file, "x")
    else:
        return print("Error While Creating File, Please Try Again!")

    if css_path != "":
        regex = r'^(.+)\/([^\/]+)$'
        path_re = re.search(regex, css_path)
        if "match" in str(path_re):
            return html.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel='stylesheet' href='{css_path}'>
</head>
<body>\n""")
        else:
            return html.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>\n""")

    elif css_path == "":
        return html.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>\n""")

def heading1(text, classname = "", id = "", center = 0):
    if center == 0:
        if text == "":
            return print("Please Enter Text!")

        #if stmt for class, id without href
        if classname != "" and id != "": #classname y and id y
            return html.write(f"<h1 class='{classname}' id='{id}'>{text}</h1>\n")

        elif classname != "" and id == "": #classname y
            return html.write(f"<h1 class='{classname}'>{text}</h1>\n")

        elif id != "" and classname == "": #id y
            return html.write(f"<h1 id='{id}>{text}</h1>\n")

        elif id == "" and classname == "": #id n
            return html.write(f"<h1>{text}</h1>\n")
    elif center == 1:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<center><h1 class='{classname}' id='{id}'>{text}</h1></center>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<center><h1 class='{classname}'>{text}</h1></center>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<center><h1 id='{id}>{text}</h1></center>\n")

        elif id == "" and classname == "":  # id n
            return html.write(f"<center><h1>{text}</h1></center>\n")
    else:
        print("Invalid Center Alignment Parameter!")

def heading2(text, classname = "", id = "", center=0):
    if center == 0:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<h2 class='{classname}' id='{id}'>{text}</h2>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<h2 class='{classname}'>{text}</h2>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<h2 id='{id}>{text}</h2>\n")

        elif id == "" and classname == "":  # id n
            return html.write(f"<h2>{text}</h2>\n")
    elif center == 1:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<center><h2 class='{classname}' id='{id}'>{text}</h2></center>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<center><h2 class='{classname}'>{text}</h2></center>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<center><h2 id='{id}>{text}</h2></center>\n")

        elif id == "" and classname == "":  # id n
            return html.write(f"<center><h3>{text}</h3></center>\n")
    else:
        print("Invalid Center Alignment Parameter!")

def heading3(text, classname = "", id = "", center = 0):
    if center == 0:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<h3 class='{classname}' id='{id}'>{text}</h3>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<h3 class='{classname}'>{text}</h3>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<h3 id='{id}>{text}</h3>\n")
        elif id == "" and classname == "":  # id n
            return html.write(f"<h3>{text}</h3>\n")
    elif center == 1:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<center><h3 class='{classname}' id='{id}'>{text}</h3></center>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<center><h3 class='{classname}'>{text}</h3></center>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<center><h3 id='{id}>{text}</h3></center>\n")

        elif id == "" and classname == "":  # id n
            return html.write(f"<center><h3>{text}</h3></center>\n")
    else:
        print("Invalid Center Alignment Parameter!")

def heading4(text, classname = "", id = "", center = 0):
    if center == 0:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<h4 class='{classname}' id='{id}'>{text}</h4>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<h4 class='{classname}'>{text}</h4>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<h4 id='{id}>{text}</h4>\n")

        elif id == "" and classname == "":  # id n
            return html.write(f"<h4>{text}</h4>\n")
    elif center == 1:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<center><h4 class='{classname}' id='{id}'>{text}</h4></center>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<center><h4 class='{classname}'>{text}</h4></center>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<center><h4 id='{id}>{text}</h4></center>\n")

        elif id == "" and classname == "": # id n
            return html.write(f"<center><h4>{text}</h4></center>\n")
    else:
        print("Invalid Center Alignment Parameter!")

def heading5(text, classname = "", id = "", center = 0):
    if center == 0:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<h5 class='{classname}' id='{id}'>{text}</h5>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<h5 class='{classname}'>{text}</h5>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<h5 id='{id}>{text}</h5>\n")

        elif id == "" and classname == "":  # id n
            return html.write(f"<h5>{text}</h5>\n")
    elif center == 1:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<center><h5 class='{classname}' id='{id}'>{text}</h5></center>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<center><h5 class='{classname}'>{text}</h5></center>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<center><h5 id='{id}>{text}</h5></center>\n")

        elif id == "" and classname == "":  # id n
            return html.write(f"<center><h5>{text}</h5></center>\n")
    else:
        print("Invalid Center Alignment Parameter!")

def heading6(text, classname = "", id = "", center = 0):
    if center == 0:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<h6 class='{classname}' id='{id}'>{text}</h6>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<h6 class='{classname}'>{text}</h6>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<h6 id='{id}>{text}</h6>\n")

        elif id == "" and classname == "":  # id n
            return html.write(f"<h6>{text}</h6>\n")
    elif center == 1:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<center><h6 class='{classname}' id='{id}'>{text}</h6></center>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<center><h6 class='{classname}'>{text}</h6></center>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<center><h6 id='{id}>{text}</h6></center>\n")

        elif id == "" and classname == "":  # id y
            return html.write(f"<h6>{text}</h6>\n")
    else:
        print("Invalid Center Alignment Parameter!")

def url(text, classname="", id = "", url = "", center=0):
    # if stmt for class, id and href (doing)
    global url_regex
    url_regex = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    if center == 0:
        if classname != "" and id != "" and url != "": #all
            url_ok = str(re.search(url_regex, url))
            if url_ok == None:
                print("\nThis is not a Proper URL, Please Try Again.")
                print('If you want to enter a Unix local path, enter it like this: ')
                print('./example.html or ../folder/example.png \n')
            elif "match" in url_ok:
                if "://" not in url:
                    url_a = "http://" + url
                    return html.write(f"<a class='{classname}' id='{id}' href='{url_a}'>{text}</a>\n")
                else:
                    return html.write(f"<a class='{classname}' id='{id}' href='{url}'>{text}</a>\n")

        elif classname != "" and id == "" and url != "": #classname y and url y
            url_ok = str(re.search(url_regex, url))
            if url_ok == None:
                print("\nThis is not a Proper URL, Please Try Again.")
                print('If you want to enter a Unix local path, enter it like this: ')
                print('./example.html or ../folder/example.png \n')
            elif "match" in url_ok:
                if "://" not in url:
                    url_a = "http://" + url
                    return html.write(f"<a class='{classname}' href='{url_a}'>{text}</a>\n")
                else:
                    return html.write(f"<a class='{classname}' href='{url}'>{text}</a>\n")

        elif classname == "" and id != "" and url != "": #id y and url y
            url_ok = str(re.search(url_regex, url))
            if url_ok == None:
                print("\nThis is not a Proper URL, Please Try Again.")
                print('If you want to enter a Unix local path, enter it like this: ')
                print('./example.html or ../folder/example.png \n')
            elif "match" in url_ok:
                if "://" not in url:
                    url_a = "http://" + url
                    return html.write(f"<a id='{id}' href='{url_a}'>{text}</a>\n")
                else:
                    return html.write(f"<a id='{id}' href='{url}'>{text}</a>\n")

        elif classname == "" and id == "" and url != "": #idurl y
            url_ok = str(re.search(url_regex, url))
            if url_ok == None:
                print("\nThis is not a Proper URL, Please Try Again.")
                print('If you want to enter a Unix local path, enter it like this: ')
                print('./example.html or ../folder/example.png \n')
            elif "match" in url_ok:
                if "://" not in url:
                    url_a = "http://" + url
                    return html.write(f"<a href='{url_a}'>{text}</a>\n")
                else:
                    return html.write(f"<a href='{url}'>{text}</a>\n")
    elif center == 1:
        if classname != "" and id != "" and url != "":  # all
            url_ok = str(re.search(url_regex, url))
            if url_ok == None:
                print("\nThis is not a Proper URL, Please Try Again.")
                print('If you want to enter a Unix local path, enter it like this: ')
                print('./example.html or ../folder/example.png \n')
            elif "match" in url_ok:
                if "://" not in url:
                    url_a = "http://" + url
                    return html.write(f"<center><a class='{classname}' id='{id}' href='{url_a}'>{text}</a></center>\n")
                else:
                    return html.write(f"<center><a class='{classname}' id='{id}' href='{url}'>{text}</a></center>\n")

        elif classname != "" and id == "" and url != "":  # classname y and url y
            url_ok = str(re.search(url_regex, url))
            if url_ok == None:
                print("\nThis is not a Proper URL, Please Try Again.")
                print('If you want to enter a Unix local path, enter it like this: ')
                print('./example.html or ../folder/example.png \n')
            elif "match" in url_ok:
                if "://" not in url:
                    url_a = "http://" + url
                    return html.write(f"<center><a class='{classname}' href='{url_a}'>{text}</a></center>\n")
                else:
                    return html.write(f"<center><a class='{classname}' href='{url}'>{text}</a></center>\n")

        elif classname == "" and id != "" and url != "":  # id y and url y
            url_ok = str(re.search(url_regex, url))
            if url_ok == None:
                print("\nThis is not a Proper URL, Please Try Again.")
                print('If you want to enter a Unix local path, enter it like this: ')
                print('./example.html or ../folder/example.png \n')
            elif "match" in url_ok:
                if "://" not in url:
                    url_a = "http://" + url
                    return html.write(f"<center><a id='{id}' href='{url_a}'>{text}</a></center>\n")
                else:
                    return html.write(f"<center><a id='{id}' href='{url}'>{text}</a></center>\n")

        elif classname == "" and id == "" and url != "":  # id n cn n and url y
            url_ok = str(re.search(url_regex, url))
            if url_ok == None:
                print("\nThis is not a Proper URL, Please Try Again.")
                print('If you want to enter a Unix local path, enter it like this: ')
                print('./example.html or ../folder/example.png \n')
            elif "match" in url_ok:
                if "://" not in url:
                    url_a = "http://" + url
                    return html.write(f"<center><a href='{url_a}'>{text}</a></center>\n")
                else:
                    return html.write(f"<center><a href='{url}'>{text}</a></center>\n")

def paragraph(text, classname="", id="", center=0):
    if center == 0:
        if text == "":
            return print("Please Enter Text!")

        #if stmt for class, id without href
        if classname != "" and id != "": #classname y and id y
            return html.write(f"<p class='{classname}' id='{id}'>{text}</p>\n")

        elif classname != "" and id == "": #classname y
            return html.write(f"<p class='{classname}'>{text}</p>\n")

        elif id != "" and classname == "": #id y
            return html.write(f"<p id='{id}>{text}</p>\n")

        elif id == "" and classname == "": #id y
            return html.write(f"<p>{text}</p>\n")
    elif center == 1:
        if text == "":
            return print("Please Enter Text!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<center><p class='{classname}' id='{id}'>{text}</p></center>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<center><p class='{classname}'>{text}</p></center>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<center><p id='{id}>{text}</p></center>\n")

        elif id == "" and classname == "":  # id y
            return html.write(f"<center><p>{text}</p></center>\n")
    else:
        print("Invalid Center Alignment Parameter!")

def img(src, classname="", id="", center=0):
    if center == 0:
        if src == "":
            return print("Please Enter Image Source")

        #if stmt for class, id without href
        if classname != "" and id != "": #classname y and id y
            return html.write(f"<img src='{src}' class='{classname}' id='{id}'></img>\n")

        elif classname != "" and id == "": #classname y
            return html.write(f"<img src='{src}' class='{classname}'></img>\n")

        elif id != "" and classname == "": #id y
            return html.write(f"<img src='{src}' id='{id}></img>\n")

        elif id == "" and classname == "": #all no
            return html.write(f"<img src='{src}'></img>\n")
    elif center == 1:
        if src == "":
            return print("Please Enter Image Source!")

        # if stmt for class, id without href
        if classname != "" and id != "":  # classname y and id y
            return html.write(f"<center><img src='{src}' class='{classname}' id='{id}' /></center>\n")

        elif classname != "" and id == "":  # classname y
            return html.write(f"<center><img src='{src}' class='{classname}' /></center>\n")

        elif id != "" and classname == "":  # id y
            return html.write(f"<center><img src='{src}' id='{id} /></center>\n")

        elif id == "" and classname == "":  # id y
            return html.write(f"<center><img src='{src}' /></center>\n")
    else:
        print("Invalid Center Alignment Parameter!")

def finHTML():
    html.write("""</body>
</html>""")
    html.close()
