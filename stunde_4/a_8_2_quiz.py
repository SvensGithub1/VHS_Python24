import csv
import random
# schreibe ein Funktion die ein Quiz durchführ und den Nutzer nach den richtigen Antworten fragt
# am Ende wird ausgegeben was das Egebnis / Score des Nutzers ist 
# In der run_quiz funktion ist die TODO stelle zu füllen. Der rest kann als gegeben angesehen werden.


def load_questions(filename):
    '''
    diese Funktion liest die Fragen aus der csv ein und gibt sie in einer List wider aus

    Parameters
    ----------
    filename : String
        Dateiname.

    Returns
    -------
    questions : List
        Liste an Fragen.

    '''
    questions = []
    with open(filename, newline='', encoding='latin1') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            question, *answers, correct_answer = row
            questions.append((question, answers, correct_answer))
    return questions


def generate_quiz(questions, num_questions=4):
    quiz = random.sample(questions, num_questions)
    return quiz

def run_quiz(quiz):
    score = 0
    for i, (question, answers, correct_answer) in enumerate(quiz, start=1):
        #!TODO hier muss die Frage an den Nutzer gegeben werden und überprüft 
        # werden was die richtige Antwort ist.
    return score

def main():
    filename = "fragen.csv"  # Name der CSV-Datei mit den Fragen
    questions = load_questions(filename)
    quiz = generate_quiz(questions)
    print("Willkommen zum Quiz!")
    input("Drücken Sie Enter, um zu beginnen...")
    print()
    score = run_quiz(quiz)
    print()
    print(f"Ihr Ergebnis: {score} von {len(quiz)} Punkten")

if __name__ == "__main__":
    main()
