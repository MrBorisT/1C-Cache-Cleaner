import os
import shutil

def cleanFolder(folder):
    folders = None
    try:
        folders = os.listdir(folder)
    except:
        print("no folders to clean")
        return
    for filename in folders:
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def clean():
    comp = "\\\\s201-ts-1"
    print("select computer: " +
    "\n 1 - s201-ts-1 (press enter, default)" +
    "\n 2 - s201-ts" +
    "\n 3 - locally" +
    "\n     or type manually\n q - to exit")
    choice = input()
    if choice == "q":
        print("exiting")
        return
    if choice != "":
        comp = "\\\\" + choice
    if choice == "1":
        comp = "\\\\s201-ts-1"
    if choice == "2":
        comp = "\\\\s201-ts"

    comp += "\\C$\\Users\\"
    if choice == "3":
        comp = "C:\\Users\\"

    print("you chose " + comp)

    users = os.listdir(comp)

    print("select username or press 'enter' for your own account")
    userToFind = input()
    if userToFind == "":
        userToFind = os.getlogin()

    filteredUsers = list(filter(lambda user: userToFind.lower() in user.lower(), users))

    if len(filteredUsers) == 0:
        print("No users found!")
        return

    userToClean = filteredUsers[0]
    if len(filteredUsers) > 1:
        print("select user:")
        i = 0
        for user in filteredUsers: 
            i += 1
            print("" + str(i) + " - " + user)
        inputIndex = input()
        userToClean = filteredUsers[int(inputIndex) - 1]
    print("cleaning 1C cache of user " + userToClean)
    pathToClean1 = comp + userToClean + "\\AppData\\Local\\1C\\1cv8"
    pathToClean2 = comp + userToClean + "\\AppData\\Roaming\\1C\\1cv8"
    cleanFolder(pathToClean1)
    cleanFolder(pathToClean2)
    print("done...")

clean()
