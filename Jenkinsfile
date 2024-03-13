pipeline {
    agent any
    stages {
        stage('Set Python Env') {
            steps {
                bat """
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                """
            }
        }
        stage('Diagnostic') {
            steps {
                bat 'echo %PATH%'
                bat 'if exist C:\\Python3\\Scripts (echo Scripts directory exists) else (echo Scripts directory does not exist)'
                // Use the above outputs to debug the issue further
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                // Your build steps go here
            }
        }
        stage('Test') {
            steps {
                echo 'Running API tests...'
                bat """
                    call venv\\Scripts\\activate.bat
                    python -m unittest tests\\test_api\\test_runner.py
                """
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Your deploy steps go here
            }
        }
    }
    post {
        always {
            // This will always run after the stages, even if they fail
            echo 'This will always run as a cleanup or notification step.'
        }
    }
}