from pyscript import document

def reveal(event):
    user = (document.getElementById("me").value)
    password = (document.getElementById("pw").value)
    active = True

    if user == "ECRV" and password == "909150":
        if active == True:
           yes = "Access Granted, click me to proceed."
        else:
            no = "Wrong username or password. Please try again."

    document.getElementById("nuhuh").innerText = no
    document.getElementById("yesyes").innerText = yes