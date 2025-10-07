from index import document

def calculate_average(event=None):
    try:
        score1 = float(document.getElementById("score1").value or 0)
    except Exception:
        score1 = 0.0
    try:
        score2 = float(document.getElementById("score2").value or 0)
    except Exception:
        score2 = 0.0

    avg = (score1 + score2) / 2

    if avg >= 75:
        result = "Passed"
    else:
        result = "Failed"

    document.getElementById("average").innerText = str(round(avg, 2))
    document.getElementById("result").innerText = result