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
                bat "%PYTHON_PATH% -m venv venv"
                bat "call venv\\Scripts\\activate.bat && venv\\Scripts\\pip.exe install -r requirements.txt"
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                // Your build steps here
            }
        }

         stage('Test') {
            steps {
                echo 'Testing..'
                // Add test execution steps here
                bat 'python -m unittest API_tests_on_GamePower_and_UI_tests_on_YouTube/tests/api_test/api_test.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                bat "venv\\Scripts\\python.exe -m unittest tests/test_api/test_runner.py"
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
            echo 'Build succeeded.'
            // Additional steps for successful build
        }

        failure {
            echo 'Build failed.'
            // Additional steps for failed build
        }
    }
}