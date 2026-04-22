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

def delete_player(ids, gdpr, days, status):
    player_id = input("Enter ID to delete: ")

    if player_id in ids:
        index = ids.index(player_id)

        ids.pop(index)
        gdpr.pop(index)
        days.pop(index)
        status.pop(index)

        print("Player deleted successfully.")
    else:
        print("ID not found.")

def add_player(ids, gdpr, days, status):
    player_id = input("Enter new ID: ")

    if player_id in ids:
        print("ID already exists.")
    else:
        ids.append(player_id)
        gdpr.append("No")
        days.append(0)
        status.append("Active")

        print("Player added successfully.")
