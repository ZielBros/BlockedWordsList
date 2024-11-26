import WriteData
import json

MainLoop = True
WriteLoop = False
AddLoop = False
RemoveLoop = False

with open('BlockedList.json', 'r') as file:
    data = json.load(file)

def main():
    global MainLoop
    global WriteLoop
    global AddLoop
    global RemoveLoop
    print("=======================Viktors Ord Blocker=======================")
    print("[1] Skriv en besked")
    print("[2] Tilføj et ord")
    print("[3] Fjern et ord")
    print("[4] Se Listen")
    print("[0] Luk Program")
    print("=======================Viktors Ord Blocker=======================")
    choice = input('Vælg en Mulighed: ')
    if choice == '0':
        MainLoop = False
    elif choice == '1':
        MainLoop = False
        WriteLoop = True
    elif choice == '2':
        MainLoop = False
        AddLoop = True
    elif choice == '3':
        MainLoop = False
        RemoveLoop = True
    elif choice == '4':
        print(f"Listen er {data['BlockedList']}\n ")

# AddOrd
def BlockOrd():
    global MainLoop
    global AddLoop
    if data['BlockedList'] == []:
        x = input("Skriv et ord du vil blokere\n[0] For at gå tilbage: ")
        if x == '0':
            MainLoop = True
            AddLoop = False
            WriteData.InsertData(data['BlockedList'])
        elif x == 'liste':
            print(f"Listen er: {data['BlockedList']}")
        else:
            data['BlockedList'].append(x)
            print(f"Listen af blokerede ord er nu: {data['BlockedList']}")
    else:
        print(f"Skriv endnu et ord for at tilføje ordet til listen\nListen: {data['BlockedList']}\n[0] For at gå tilbage")
        x = input()
        if x == '0':
            MainLoop = True
            AddLoop = False
            WriteData.InsertData(data['BlockedList'])
        elif x == 'liste':
            print(f"Listen er: {data['BlockedList']}")
        else:
            data['BlockedList'].append(x)
            print(f"Listen af blokerede ord er nu: {data['BlockedList']}")

# WriteMessage
def WriteMessage():
    global MainLoop
    global WriteLoop
    message = input(f"Listen: {data['BlockedList']}\n[0] For at gå tilbage\nSkriv en Besked: ")
    if message == '0':
        MainLoop = True
        WriteLoop = False
    elif message == 'liste':
        print(f"Listen er: {data['BlockedList']}")
    else:
        for word in data['BlockedList']:
            if word in message:
                print(f"Du kan ikke skrive dette fordi at {word} er i listen\n \n ")

# RemoveWord
def RemoveOrd():
    global MainLoop
    global RemoveLoop
    if data['BlockedList'] == []:
        print("Listen af blokerede ord er tom!")
        RemoveLoop = False
        MainLoop = True
    else:
        x = input(f"Listen: {data['BlockedList']}\n[0] For at gå tilbage\nSkriv et ord du vil fjerne fra listen: ")
        if x == '0':
            MainLoop = True
            RemoveLoop = False  # Set RemoveLoop to False to exit this loop
            WriteData.InsertData(data['BlockedList'])
        elif x == 'liste':
            print(f"Listen er: {data['BlockedList']}")
        else:
            if x in data['BlockedList']:
                data['BlockedList'].remove(x)
                print(f"Listen af blokerede ord er nu: {data['BlockedList']}")
            else:
                print("Ordet er ikke i listen")

while MainLoop:
    main()
    while WriteLoop:
        WriteMessage()
    while RemoveLoop:
        RemoveOrd()
    while AddLoop:
        BlockOrd()
