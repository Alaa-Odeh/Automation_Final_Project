pipeline {
    agent any

    environment {
        PIP_PATH = "\"C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pip\""
        PYTHON_PATH = "\"C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\python.exe\""
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat "%venv/bin/activate% -m venv venv"
                bat "call venv\\Scripts\\activate.bat && venv\\Scripts\\pip.exe install -r requirements.txt"
            }
        }


        stage('Test') {
            steps {
                echo 'Testing..'
                bat "venv\\Scripts\\python.exe -m unittest tests/test_api/test_blogs.py"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Your deployment steps here
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "rd /s /q venv"
        }

        success {
            echo 'Test succeeded.'
            // Additional steps for successful build
        }

        failure {
            echo 'Test failed.'
            // Additional steps for failed build
        }
    }
}