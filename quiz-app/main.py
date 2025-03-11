import streamlit as st
import random
import time

st.title("🐍 Python Quiz Application")

questions = [
    {
        "question": "What is Python?",
        "options": ["A snake", "A programming language", "A car brand", "A type of coffee"],
        "answer": "A programming language",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "lambda"],
        "answer": "def",
    },
    {
        "question": "What is the output of 2 + 2 in Python?",
        "options": ["3", "4", "22", "None"],
        "answer": "4",
    },
    {
        "question": "What does the len() function do?",
        "options": ["Adds two numbers", "Finds the length of a string", "Prints output", "None of the above"],
        "answer": "Finds the length of a string",
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": "Tuple",
    },
    {
        "question": "How do you start a comment in Python?",
        "options": ["//", "#", "/*", "<!--"],
        "answer": "#",
    },
    {
        "question": "What is the output of print(type([]))?",
        "options": ["<class 'tuple'>", "<class 'list'>", "<class 'dict'>", "<class 'set'>"],
        "answer": "<class 'list'>",
    },
    {
        "question": "What is the result of 10 // 3?",
        "options": ["3.33", "3", "1", "0"],
        "answer": "3",
    },
    {
        "question": "Which of the following is not a Python data type?",
        "options": ["Integer", "Float", "Real", "List"],
        "answer": "Real",
    },
    {
        "question": "How do you create a variable in Python?",
        "options": ["x = 5", "var x = 5", "int x = 5", "x: 5"],
        "answer": "x = 5",
    },
    {
        "question": "Which function is used to get user input in Python?",
        "options": ["input()", "scanf()", "get()", "read()"],
        "answer": "input()",
    },
    {
        "question": "Which module in Python is used for mathematical operations?",
        "options": ["math", "random", "os", "sys"],
        "answer": "math",
    },
    {
        "question": "How do you handle exceptions in Python?",
        "options": ["if-else", "try-except", "catch-throw", "error handling"],
        "answer": "try-except",
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "12"],
        "answer": "8",
    },
    {
        "question": "Which keyword is used to create a class in Python?",
        "options": ["class", "Class", "define", "cls"],
        "answer": "class",
    },
    {
        "question": "What is the purpose of the pass statement?",
        "options": ["To break a loop", "To do nothing", "To continue a loop", "To exit a function"],
        "answer": "To do nothing",
    },
    {
        "question": "How do you import a module in Python?",
        "options": ["module import", "import module", "include module", "use module"],
        "answer": "import module",
    },
    {
        "question": "What is a lambda function?",
        "options": ["A regular function", "An anonymous function", "A built-in function", "None of the above"],
        "answer": "An anonymous function",
    },
    {
        "question": "How do you start a for loop in Python?",
        "options": ["for i in range(10)", "for (i=0; i<10; i++)", "foreach i in range(10)", "loop i in range(10)"],
        "answer": "for i in range(10)",
    },
    {
        "question": "What does the break statement do in Python?",
        "options": ["Ends the loop", "Skips the current iteration", "Restarts the loop", "None of the above"],
        "answer": "Ends the loop",
    },
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.balloons()
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])

    time.sleep(2)

    st.session_state.current_question = random.choice(questions)

    st.rerun()
