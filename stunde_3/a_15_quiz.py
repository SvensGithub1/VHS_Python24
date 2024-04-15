import csv
import random

def load_questions(filename):
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
        print(f"Frage {i}: {question}")
        random.shuffle(answers)
        for j, answer in enumerate(answers, start=1):
            print(f"{j}. {answer}")
        user_answer = input("Ihre Antwort (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if answers[int(user_answer) - 1] == correct_answer:
                print("Richtig!")
                score += 1
            else:
                print("Falsch!")
                print(f"Die richtige Antwort war: {correct_answer}")
        else:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 4 ein.")
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
