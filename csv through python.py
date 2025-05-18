import csv


def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r', newline='', encoding='iso-8859-1') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if len(row) >= 2:
                credentials[row[0]] = row[1]
    return credentials


def write_credentials(file_path, credentials):
    path = "E:\\software project\\hotel-reservation-main\\login.csv"
    credential = read_credentials(path)
    user=list(credentials.keys())
    if user[0] in credential:
        print("User name already exists")
    else:
        with open(file_path, 'a+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for user_name, pass_word in credentials.items():
                csv_writer.writerow([user_name, pass_word])


def login():
    file_path = "E:\\software project\\hotel-reservation-main\\login.csv"
    credentials = read_credentials(file_path)

    user_name = input("Username: ")
    pass_word = input("Password: ")

    if user_name in credentials and credentials[user_name] == pass_word:
        print("Login successful!")
    else:
        print("Invalid username or password.")


k = 1
while k == 1:
    print("\n1. Login")
    print("2. Signup")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        login()

    elif choice == '2':
        username = input("Username:")
        password = input("Password:")
        data = {username: password}
        file = "E:\\software project\\hotel-reservation-main\\login.csv"
        write_credentials(file, data)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
