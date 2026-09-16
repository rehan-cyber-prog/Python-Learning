questions = {"Python kis ne banayi?": "guoido", "2 + 2 = ?": "4", "Capital of India?": "new delhi", "5 * 6 = ?": "30", "Python ka full form kya hai?": "programming language"}
score = 0
print("===== QUIZ GAME =====")
for question, answer in questions.items():
    user = input(question + " : ").lower()
    if user == answer:
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print("Correct Answer:", answer)
print("\n===== RESULT =====")
print("Your Score:", score, "/", len(questions))
if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good Job!")
else:
    print("Better Luck Next Time!")