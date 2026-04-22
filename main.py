# Anik Desai
from itertools import count


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
#option 5
def options5(ids):
    casual = 0
    pro = 0
    for player_id in ids:
        if player_id.stratswith("CAS"):
            casual += 1
        else :
            pro += 1
    total = len(ids)

    if total > 0 :
        casual_perc = (casual/total)*100
        pro_perc = (pro/total)*100
    else :
        casual_perc = 0
        pro_perc = 0
    print("\nCasual players:", casual, f"({casual_perc:.2f}%)")
    print("Pro players:", pro, f"({pro_perc:.2f}%)")
#option 6
def option6(ids,status):
    locked_file = open("locked.txt", "w")
    active_file = open("active.txt", "w")
    disabled_file = open("disabled.txt", "w")

    for i in range (len(ids)):
        if status[i] == "locked":
            locked_file.write(ids[i] + "\n")
        elif status[i] == "active":
            active_file.write(ids[i] + "\n")
        elif status[i] == "disabled":
            disabled_file.write(ids[i] + "\n")

    locked_file.close()
    active_file.close()
    disabled_file.close()
    print('file created successfully.')

#option7

def option7(gdpr, status):
    count = 0
    for i in range(len(status)):
        if gdpr[i] == "No" and status[i] == "active":
            status[i] ="disabled"
            count += 1
    return count


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


