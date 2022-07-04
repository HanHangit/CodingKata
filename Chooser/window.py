from operator import truediv
import PySimpleGUI as sg
import json
from random import seed
from random import randint
from Exercise import Exercise

themes = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'PythonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']

value = randint(0, len(themes))
theme = themes[value]
sg.theme(theme)

layout = [
    [
        sg.Text("Typ der Aufgabe: "),
        sg.Radio("Kurz", "group 1", key="-SHORT-", default=True),
        sg.Radio("Mittel", "group 1",key="-MEDIUM-"),
        sg.Radio("Lang", "group 1", key="-LONG-"),
        sg.Radio("Uni Zeug", "group 1", key="-UNI-")
    ],
    [
        sg.Text("Aufgabe geschafft "),
        sg.Radio("Keiner", "group 2", key="-NOBODY-", default=True),
        sg.Radio("Johannes", "group 2",key="-JOH-"),
        sg.Radio("Chris", "group 2", key="-CHRIS-"),
        sg.Radio("Beide", "group 2", key="-BOTH-"),
    ],
    [
        sg.Button("Ok", key="-OK-", bind_return_key=True),
        sg.Button("Add", key="-ADD-", bind_return_key=True)
    ],
    [
        sg.Text("", key="-TITLE-", visible=False)
    ],
    [
        sg.Text("", key="-DESCRIPTION-", visible=False, size=(50,15))
    ],
    [
        sg.Button("Ich habs geschafft!",key="-ACCEPT-", bind_return_key=True, visible=False)
    ],
]

window = sg.Window("Choose your Challenge!", layout)

def ParseToJson(exercise_list):
    with open('test.json','w') as json_file:
                json.dump(exercise_list, json_file, indent=4, default=Exercise.to_dict)

def CreateNewList(exerciseList, newExercise):
    newList = []
    for u in exerciseList:
        if u.title != newExercise.title:
            newList.append(u)

    newList.append(newExercise)    
    return newList


def AddWindow(exercise_list):
    windowLayout = [
        [sg.Text("Title")],
        [sg.InputText(size=(35,1), key="-TITLE-")],
        [sg.Text("Description")],
        [sg.MLine(size=(35,15), key="-DESCRIPTION-")],
        [
            sg.Radio("Kurz", "group 1", key="-SHORT-", default=True),
            sg.Radio("Mittel", "group 1",key="-MEDIUM-"),
            sg.Radio("Lang", "group 1", key="-LONG-"),
            sg.Radio("Uni Zeug", "group 1", key="-UNI-")],
        [sg.Button("Add", key="-ADD-", bind_return_key=True), sg.Button("Back", key="-REJECT-", bind_return_key=True)]
    ]
    newWindow = sg.Window("Neue Exercise hinzufügen", windowLayout)

    while True:
        event, values = newWindow.read()
        if event == "-ADD-":
            titleText = values["-TITLE-"]
            descriptionText = values["-DESCRIPTION-"]
            if values["-SHORT-"] == True:
                complexity = "Short"
            elif values["-MEDIUM-"] == True:
                complexity = "Medium"
            elif values["-LONG-"] == True:
                complexity = "Long"
            elif values["-UNI-"] == True:
                complexity = "Uni"          
            
            exercise = Exercise(titleText, complexity, descriptionText, worker=[])
            finalList = CreateNewList(exercise_list, exercise)
            ParseToJson(finalList)
            break

        elif event == sg.WIN_CLOSED or event == "-REJECT-":
            break
    newWindow.close()

def ChallengeWindow(exercise_list, targetExercise):
    windowLayout = [[sg.Text("Aufgaben abgeschlossen? Bitte eintragen!")],
                    [sg.Text("Bearbeiter"), sg.Radio("Johannes", "group 2",key="-JOH-", default=True), sg.Radio("Chris", "group 2", key="-CHRIS-"),],
                    [sg.Button("Ich habs geschafft!", key="-OK-", bind_return_key=True), sg.Button("Nicht geschafft", key="-REJECT-", bind_return_key=True)]
                    ]

    newWindow = sg.Window("Aufgabe geschafft", windowLayout)

    while True:
        event, values = newWindow.read()

        key_joh = values["-JOH-"]
        key_chris = values["-CHRIS-"]

        if key_chris == True:
            user = "Christian"
        elif key_joh == True:
            user = "Johannes"

        targetExercise.worker.append(user)

        newList = CreateNewList(exercise_list, targetExercise)  

        if event =="-OK-":
            ParseToJson(newList)
            newWindow.close()
        elif event == "-REJECT-" or event == sg.WIN_CLOSED:
            break

    newWindow.close()

while True:
    event, values = window.read()

    exercise_list = []
    with open('test.json','r') as json_file:
        exercise_data = json.loads(json_file.read())
        for u in exercise_data:
            exercise_list.append(Exercise(**u))

    if values["-SHORT-"] ==  True:
        target_complexity = "Short"
    elif values["-MEDIUM-"] == True:
        target_complexity = "Medium"
    elif values["-LONG-"] == True:
        target_complexity = "Long"
    elif values["-UNI-"] == True:
        target_complexity = "Uni"

    if values["-NOBODY-"] ==  True:
        target_worker = []
    elif values["-JOH-"] == True:
        target_worker = ["Johannes"]
    elif values["-CHRIS-"] == True:
        target_worker = ["Christian"]
    elif values["-BOTH-"] == True:
        target_worker = ["Christian", "Johannes"]

    def contains(list, filter):
        newList = []
        for x in list:
            if filter(x):
                newList.append(x)
        return newList
        
    list = contains(exercise_list, lambda x: x.complexity == target_complexity)
    finalList = contains(list, lambda x: x.worker == target_worker)

    if len(finalList) > 0:
        rndvalue = randint(0, len(finalList) -1)
        targetExercise = finalList[rndvalue]

    if event == sg.WIN_CLOSED:
        break

    elif event == "-OK-":

        if len(finalList) > 0:
            title = targetExercise.title
            description = targetExercise.description
            window["-ACCEPT-"].update(visible=True)
        else:
            title = "Kein Akku mehr"
            description = "Wir brauchen mehr Einträge in der Datenbank! Alles leer :("
            window["-ACCEPT-"].update(visible=False)

        window['-TITLE-'].update(title, visible=True)
        window["-DESCRIPTION-"].update(description, visible=True)

    elif event == "-ACCEPT-":
        ChallengeWindow(exercise_list, targetExercise),
    elif event == "-ADD-":
        AddWindow(exercise_list),
    
window.close()
