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

def update_status(ids, status):
    player_id = input("Enter ID: ")

    if player_id in ids:
        index = ids.index(player_id)

        new_status = input("Enter new status: ")
        status[index] = new_status

        print("Status updated.")
    else:
        print("ID not found.")

def save_file(filename, ids, gdpr, days, status):
    file = open(filename, "w")

    for i in range(len(ids)):
        line = ids[i] + "," + gdpr[i] + "," + str(days[i]) + "," + status[i] + "\n"
        file.write(line)

    file.close()

def menu():
    filename = "gamers.txt"
    ids, gdpr, days, status = read_file(filename)

    choice = ""
    while choice != "8":
        print("\nMenu")
        print("1. View all players")
        print("2. Delete a player")
        print("3. Register new player")
        print("4. Update player status")
        print("5. Placeholder for Exam")
        print("6. Placeholder for Exam")
        print("7. Placeholder for Exam")
        print("8. Quit and save")

        choice = input("Enter choice: ")

        if choice == "1":
            view_players(ids, gdpr, days, status)

        elif choice == "2":
            delete_player(ids, gdpr, days, status)

        elif choice == "3":
            add_player(ids, gdpr, days, status)

        elif choice == "4":
            update_status(ids, status)

        elif choice == "5":
            print("Option 5 not implemented yet.")

        elif choice == "6":
            print("Option 6 not implemented yet.")

        elif choice == "7":
            print("Option 7 not implemented yet.")

        elif choice == "8":
            save_file(filename, ids, gdpr, days, status)
            print("Data saved. Goodbye.")

        else:
            print("Invalid choice.")


if __name__ == '__main__':
    menu()


