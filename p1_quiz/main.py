mock_answers = ["Islamabad", "4", "Python"]

questions = [
    {"question": "What is the capital of Pakistan?", "answer": "Islamabad", "marks": 5, "penalty": -2},
    {"question": "What is 2 + 2?", "answer": "4", "marks": 2, "penalty": -1},
    {"question": "Which language is this quiz in?", "answer": "Python", "marks": 3, "penalty": -1}
]

total_score = 0
total_possible = sum(q["marks"] for q in questions)
total_questions = len(questions)
current_question = 1

for i, q in enumerate(questions):
    print(f"\nQuestion {current_question}/{total_questions}: {q['question']}")
    
    user_answer = mock_answers[i] 
    print(f"Auto Answered: {user_answer}")

    if user_answer.lower() == q['answer'].lower():
        total_score += q['marks']
        print("Correct!")
    else:
        total_score += q['penalty']
        print(" Wrong!")
    current_question += 1

print(f"\nFinal Score: {total_score}")

if score == total_possible:
    print(" Excellent! You answered everything correctly.")
elif score >= total_possible - 2:
    print(" Great job! Just missed a few points.")
elif score >= 4:
    print(" Not bad, keep practicing!")
else:
    print(" Better luck next time. Try again!")





