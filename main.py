# Anik Desai

def read_file(filename):
    ids = []
    gdpr = []
    days = []
    status = []

    file = open(filename, "r")
    for line in file:
        line = line.strip()
        parts = line.split(",")

        ids.append(parts[0])
        gdpr.append(parts[1])
        days.append(int(parts[2]))
        status.append(parts[3])

    file.close()
    return ids, gdpr, days, status

def view_players(ids, gdpr, days, status):
    print("\nAccounts:\n")

    for i in range(len(ids)):

        # Account type
        if ids[i].startswith("CAS"):
            acc_type = "Casual"
        else:
            acc_type = "Pro"

        # Paid symbol
        if gdpr[i] == "Yes":
            paid = "✅"
        else:
            paid = "❎"

        # Alert
        alert = ""
        if days[i] > 90:
            alert = "🚨"

        print(ids[i], acc_type, paid, status[i], alert)

