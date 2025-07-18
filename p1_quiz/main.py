questions = [
    {
        "question": "What is the capital of Pakistan?",
        "answer": "Islamabad",
        "marks": 5,
        "penalty": -2
    },
    {
        "question": "What is 5 + 7?",
        "answer": "12",
        "marks": 3,
        "penalty": -1
    },
    {
        "question": "Which language is used for web apps?",
        "answer": "JavaScript",
        "marks": 4,
        "penalty": -2
    }
]


total_score = 0
current_question = 1
total_questions = len(questions)


for q in questions:
    print(f"\nQuestion {current_question}/{total_questions}: {q['question']}")
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == q['answer'].lower():
        print("Correct!")
        total_score += q['marks']
    else:
        print(f"Wrong! The correct answer is: {q['answer']}")
        total_score += q['penalty']

    current_question += 1


print("\n Quiz Completed!")
print(f"Your Total Score: {total_score}")


if total_score > 10:
    print("Excellent!")
elif total_score > 5:
    print("Good job!")
else:
    print("Keep practicing!")




