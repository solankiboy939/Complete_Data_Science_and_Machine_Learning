import streamlit as st
import bcrypt

# Initialize user database if not present in session_state
if "users" not in st.session_state:
    st.session_state["users"] = {
        "johndoe": {
            "name": "John Doe",
            "password": bcrypt.hashpw("password123".encode(), bcrypt.gensalt())
        },
        "janesmith": {
            "name": "Jane Smith",
            "password": bcrypt.hashpw("password456".encode(), bcrypt.gensalt())
        }
    }

# Dummy data for recommendations and quizzes
courses = {
    "Data Science": ["Python Basics", "Data Analysis with Pandas", "Machine Learning"],
    "Web Development": ["HTML & CSS", "JavaScript Basics", "React for Beginners"],
    "AI & ML": ["Intro to AI", "Deep Learning", "AI Ethics"]
}

quizzes = {
    "Python Basics": {
        "question": "What is the output of print(2 + 3 * 4)?",
        "options": ["14", "20", "10", "None of the above"],
        "answer": "14"
    },
    "Data Analysis with Pandas": {
        "question": "Which method is used to read a CSV file in pandas?",
        "options": ["read_csv()", "readFile()", "readData()", "load_csv()"],
        "answer": "read_csv()"
    },
    "Machine Learning": {
        "question": "Which algorithm is used for classification?",
        "options": ["Linear Regression", "Logistic Regression", "K-means", "None of the above"],
        "answer": "Logistic Regression"
    }
}

def authenticate(username, password):
    if username in st.session_state["users"]:
        if bcrypt.checkpw(password.encode(), st.session_state["users"][username]["password"]):
            return st.session_state["users"][username]["name"]
    return None

def register(username, name, password):
    if username in st.session_state["users"]:
        return False
    st.session_state["users"][username] = {
        "name": name,
        "password": bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    }
    return True

def logout():
    st.session_state["authenticated"] = False
    st.session_state.pop("username", None)

# Sidebar for authentication, registration, and logout
st.sidebar.title("Login / Register")
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    option = st.sidebar.selectbox("Select Option", ["Login", "Register"])

    if option == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            name = authenticate(username, password)
            if name:
                st.sidebar.success(f"Welcome {name}!")
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.experimental_rerun()
            else:
                st.sidebar.error("Invalid username or password")

    elif option == "Register":
        new_username = st.sidebar.text_input("New Username")
        new_name = st.sidebar.text_input("Name")
        new_password = st.sidebar.text_input("New Password", type="password")

        if st.sidebar.button("Register"):
            if register(new_username, new_name, new_password):
                st.sidebar.success("Registration successful! Please log in.")
            else:
                st.sidebar.error("Username already exists. Please choose a different username.")
else:
    # Show the user’s name and offer a logout option
    name = st.session_state["users"][st.session_state["username"]]["name"]
    st.sidebar.title("Personalized Learning Companion")
    st.sidebar.write(f"Logged in as {name}")

    # Logout button
    if st.sidebar.button("Logout"):
        logout()
        st.sidebar.success("Logged out successfully!")
        st.experimental_rerun()

    # Main content
    st.title(f"Welcome, {name}!")
    learning_interest = st.sidebar.selectbox("Select your interest:", list(courses.keys()))

    if learning_interest:
        st.write(f"Your selected interest: **{learning_interest}**")

        # Recommendations
        st.subheader("Recommended Courses")
        for course in courses[learning_interest]:
            st.write(f"- {course}")
            st.markdown(f"[Explore {course}](https://www.example.com)")

        # Progress tracking
        st.subheader("Your Progress")
        course_progress = {}
        for course in courses[learning_interest]:
            progress = st.slider(f"{course} progress:", 0, 100, 0, key=course)
            course_progress[course] = progress
            st.progress(progress / 100.0)

        # Display overall progress
        total_progress = sum(course_progress.values()) / len(course_progress) if course_progress else 0
        st.write(f"**Overall Progress: {total_progress:.2f}%**")

        # Interactive Quiz
        st.subheader("Take a Quiz")
        selected_course = st.selectbox("Select a course to take a quiz:", courses[learning_interest])
        if selected_course:
            question = quizzes[selected_course]["question"]
            options = quizzes[selected_course]["options"]
            answer = quizzes[selected_course]["answer"]

            st.write(question)
            user_answer = st.radio("Choose your answer:", options)

            if st.button("Submit Answer"):
                if user_answer == answer:
                    st.success("Correct! Well done.")
                else:
                    st.error("Incorrect! Try again.")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.write("Powered by Streamlit")
