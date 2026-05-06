questions = [
    {
        "question": "What is the color of the sky?",
        "choices": ["Green", "Blue", "Red", "Yellow"],
        "answer": 2
    },
    {
        "question": "How many legs does a cat have?",
        "choices": ["Two", "Four", "Six", "Eight"],
        "answer": 2
    },
    {
        "question": "What do bees make?",
        "choices": ["Milk", "Honey", "Water", "Bread"],
        "answer": 2
    },
    {
        "question": "Which shape has three sides?",
        "choices": ["Square", "Circle", "Triangle", "Rectangle"],
        "answer": 3
    },
    {
        "question": "What is the opposite of hot?",
        "choices": ["Cold", "Warm", "Boiling", "Spicy"],
        "answer": 1
    },
    {
        "question": "Which animal barks?",
        "choices": ["Cat", "Cow", "Dog", "Sheep"],
        "answer": 3
    },
    {
        "question": "What is 2 + 2?",
        "choices": ["3", "4", "5", "6"],
        "answer": 2
    },
    {
        "question": "What color are bananas?",
        "choices": ["Red", "Blue", "Yellow", "Purple"],
        "answer": 3
    },
    {
        "question": "Which planet do we live on?",
        "choices": ["Mars", "Earth", "Venus", "Jupiter"],
        "answer": 2
    },
    {
        "question": "What do you use to write on paper?",
        "choices": ["Spoon", "Pencil", "Plate", "Cup"],
        "answer": 2
    }
]

prizes = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

score = 0

for q in questions:
    print(q["question"])
    
    for i, choice in enumerate(q["choices"], start=1):
        print(f"{i}. {choice}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect! The correct answer was option {q['answer']}.")
        break

if score > 0:
    print(f"You won {prizes[score - 1]}")
else:
    print("You didn't win anything.")