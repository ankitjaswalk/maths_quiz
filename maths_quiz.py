import random

def generate_question():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    answer = eval(question)  # Safe here because we control the input
    return question, answer

def math_quiz():
    score = 0
    total_questions = 5

    print("🧠 Welcome to the Math Quiz Game!")
    print(f"Answer {total_questions} questions correctly to win!\n")

    for i in range(1, total_questions + 1):
        question, correct_answer = generate_question()
        print(f"Question {i}: What is {question}?")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.\n")
            continue

        if user_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {correct_answer}.\n")

    print(f"🎉 Game Over! You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    math_quiz()
