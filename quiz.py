name = input("Enter Your Name: ")

print("\n========================================")
print("     Welcome to Smart Quiz Challenge")
print("========================================")
print("Hello", name)
print("Let's Start the Quiz!")

score = 0

questions = {

    "What is Python?": "programming language",

    "What is AI?": "artificial intelligence",

    "Who developed Python?": "guido van rossum",

    "What is CPU?": "central processing unit",

    "What is RAM?": "random access memory",

    "What is HTML used for?": "web pages",

    "What is the full form of URL?": "uniform resource locator",

    "Which keyword is used for loop in Python?": "for",

    "What is the extension of Python file?": ".py",

    "What is the brain of computer?": "cpu",

    "Which function is used to take user input?": "input",

    "Which symbol is used for comments in Python?": "#",

    "What is the full form of WWW?": "world wide web",

    "Which data type stores True or False values?": "boolean",

    "What is the output function in Python?": "print"
}

for question, answer in questions.items():

    print("\n" + question)

    user_answer = input("Your Answer: ").strip().lower()

    if user_answer == answer:

        print("✅ Awesome! Correct Answer")
        score += 1

    else:

        print("❌ Wrong Answer")
        print("Correct Answer is:", answer)

print("\n========================================")
print("Quiz Completed!")
print("Final Score:", score, "/", len(questions))
print("========================================")

# Performance Message

if score >= 12:
    print("🌟 Excellent Performance!")

elif score >= 8:
    print("👍 Good Job!")

else:
    print("📘 Keep Practicing!")

# Saving score into file

file = open("scores.txt", "a")

file.write(f"{name} Score: {score}/{len(questions)}\n")

file.close()

print("✅ Score Saved Successfully!")
print("Thank You For Using Smart Quiz Challenge")