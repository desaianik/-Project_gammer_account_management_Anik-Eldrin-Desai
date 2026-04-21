# Your name here...

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
