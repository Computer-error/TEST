from pyscript import document

def reveal(event):
    user = (document.getElementById("me"))
    password = (document.getElementById("pw"))
    active = True
    yes = ""
    no = ""

    if user == "ECRV" and password == "909150":
        if active == True:
           yes = "Access Granted, click me to proceed."
        else:
            no = "System error. Please try again later."
    else:
        no = "Wrong username or password. Please try again."    

    document.getElementById("nuhuh").innerText = no
    document.getElementById("yesyes").innerText = yes
