def start_quiz():
    print("Welcome to Edge Tech Quiz")
    start_input = input("Do you want to start the quiz? (yes/no): ").strip().lower()

    if start_input == "yes":
        question = [
            "What is the capital of Nigeria?",
            ""

        ]

        score = 0

        