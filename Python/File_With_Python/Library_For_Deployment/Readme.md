# Streamlit Application for Data Visualization

## Streamlit Application

This repository contains a Streamlit application. Streamlit is an open-source app framework in Python that helps create and share beautiful, custom web apps for machine learning and data science.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Creating a Streamlit Application](#creating-a-streamlit-application)
- [Deployment](#deployment)
  - [Deploying on Streamlit Sharing](#deploying-on-streamlit-sharing)
  - [Deploying on Heroku](#deploying-on-heroku)
  - [Deploying on AWS](#deploying-on-aws)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7 or higher installed on your computer.
- `pip` for package management.
- (Optional) Git for version control.

## Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/solankiboy939/Complete_Data_Science_and_Machine_Learning/tree/main/Python/File_With_Python/Library_For_Deployment
    ```

2. **Create a Virtual Environment**
    ```sh
    python -m venv env
    ```

3. **Activate the Virtual Environment**

    - **Windows**
        ```sh
        .\env\Scripts\activate
        ```
    - **MacOS/Linux**
        ```sh
        source env/bin/activate
        ```

4. **Install the Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Navigate to the Application Directory**
    ```sh
    cd src
    ```

2. **Run the Streamlit Application**
    ```sh
    streamlit run app.py
    ```

![image](https://github.com/solankiboy939/Complete_Data_Science_and_Machine_Learning/assets/119101769/f3340a99-922f-409d-8237-8a5c97b08123)


## Creating a Streamlit Application

To create a basic Streamlit application, follow these steps:

1. **Import Streamlit**
    ```python
    import streamlit as st
    ```

2. **Write Your First Streamlit App**
    ```python
    st.title('Hello, Streamlit!')
    st.write('Welcome to your first Streamlit app.')
    ```

3. **Save the File**
    Save the file as `app.py` in your project directory.

4. **Run the Application**
    ```sh
    streamlit run app.py
    ```

## Deployment

### Deploying on Streamlit Sharing

1. **Push Your Code to GitHub**
    ```sh
    git add .
    git commit -m "Initial commit"
    git push origin main
    ```

2. **Sign Up on Streamlit Sharing**
    - Go to [Streamlit Sharing](https://share.streamlit.io/) and sign up or log in.
    - Click on "New app" and select your repository and branch.
    - Click "Deploy".

### Deploying on Heroku

1. **Create a `Procfile`**
    ```sh
    echo "web: sh setup.sh && streamlit run src/app.py" > Procfile
    ```

2. **Create a `setup.sh`**
    ```sh
    echo "mkdir -p ~/.streamlit/
    echo \"[general]\nemail = \\\"your-email@domain.com\\\"\" > ~/.streamlit/credentials.toml
    echo \"[server]\nheadless = true\nenableCORS=false\nport = \$PORT\" > ~/.streamlit/config.toml" > setup.sh
    ```

3. **Create a `requirements.txt`**
    ```sh
    pip freeze > requirements.txt
    ```

4. **Push Your Code to Heroku**
    ```sh
    heroku create your-app-name
    git push heroku main
    ```

### Deploying on AWS

1. **Create a Dockerfile**
    ```Dockerfile
    FROM python:3.9

    WORKDIR /app

    COPY requirements.txt requirements.txt
    RUN pip install -r requirements.txt

    COPY . .

    EXPOSE 8501

    CMD ["streamlit", "run", "src/app.py"]
    ```

2. **Build and Push Docker Image to AWS ECR**
    - Follow the AWS ECR guide to push your Docker image to ECR.

3. **Deploy to AWS ECS**
    - Use AWS ECS to run your Docker container.

## Contributing

Contributions are always welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
