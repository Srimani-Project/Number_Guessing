questions = [
    {
        "prompt" : "What is the capital of France?",
        "options": ["A. Berlin\nB. Madrid\nC. Paris\nD. Rome\n"],
        "answer": "C"
    },
    {
        "prompt" : "Which planet is known as the Red Planet?",
        "options":["A. Earth\nB. Mars\nC. Jupiter\nD. Venus"],
        "answer":"B"
    },
    {
        "prompt":"Who wrote the play 'Romeo and Juliet'?",
        "options":["A. Charles Dickens\nB. George Orwell\nC. William Shakespeare\nD. Mark Twain"],
        "answer":"C"
    },
    {
        "prompt":"What is the largest mammal in the world?",
        "options":["A. African Elephant\nB. Blue Whale\nC. Giraffe\nD. Hippopotamus"],
        "answer":"B"
    },
    {
        "prompt":"What is the chemical symbol for gold? ",
        "options":["A. Au\nB. Ag\nC. Pb\nD. Fe"],
        "answer":"A"
    },
    {
        "prompt":"Which element has the atomic number 1? ",
        "options":["A. Oxygen\nB. Helium\nC. Hydrogen\nD. Nitrogen"],
        "answer":"C"
    },
    {
        "prompt":"In which year did the Titanic sink? ",
        "options":["A. 1912\nB. 1905\nC. 1898\nD. 1920"],
        "answer":"A"
    },
    {
        "prompt":"Who painted the Mona Lisa? ",
        "options":["A. Vincent van Gogh\nB. Pablo Picasso\nC. Leonardo da Vinci\nD. Claude Monet"],
        "answer":"C"
    },
    {
        "prompt":"What is the largest continent on Earth? ",
        "options":["A. Africa\nB. Asia\nC. Europe\nD. Antarctica"],
        "answer":"B"
    },
    {
        "prompt":"How many bones are there in the human body? ",
        "options":["A. 204\nB. 206\nC. 210\nD. 214"],
        "answer":"B"
    },

]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter a Option: ").upper()
        if answer == question["answer"]:
            print("Hooray! Correct Option\n")
            score +=1
        else:
            print("Wrong,LOSERR!!! The Correct Option: ",question["answer"],"\n")
    print(f"You got {score} out of {len(questions)} questions correct.")


run_quiz(questions)