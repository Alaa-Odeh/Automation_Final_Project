pipeline {
    agent any
    environment {
        PYTHON_PATH = "C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        PIP_PATH = "C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe"
    }
    stages {
        stage('Setup Environment') {
            steps {
                bat 'call "%PYTHON_PATH%" -m venv venv'
                bat 'call venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'call venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        stage('Selenium Tests') {
            steps {
                bat 'call venv\\Scripts\\python.exe -m unittest discover -s tests\\test_web -p "test_log_in_page.test_run.py"'
            }
        }
    }
}