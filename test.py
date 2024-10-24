# Define the function to ask a question
def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # Get user input and validate
    answer = input("Your answer (1/2/3/4): ")
    
    # Check if the answer is correct
    if options[int(answer)-1].lower() == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")
        return False

# Main function to conduct the quiz
def quiz():
    score = 0
    total_questions = 3
    
    print("Welcome to the quiz!\n")
    
    # First Question
    if ask_question("What is the capital of France?", 
                    ["Berlin", "Paris", "Rome", "Madrid"], 
                    "Paris"):
        score += 1
    
    # Second Question
    if ask_question("Which language is used for web development?", 
                    ["Python", "HTML", "C++", "Java"], 
                    "HTML"):
        score += 1
    
    # Third Question
    if ask_question("Is Python case-sensitive?", 
                    ["Yes", "No"], 
                    "Yes"):
        score += 1
    
    # Provide feedback
    print(f"\nYour score is {score}/{total_questions}.")
    
    if score == total_questions:
        print("Excellent! You got everything right!")
    elif score > 1:
        print("Good job! You did well.")
    else:
        print("Better luck next time!")

# Run the quiz
quiz()
