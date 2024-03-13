pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Set Python Env') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Running API tests...'
                // Replace "C:\\Path\\To\\Python\\python.exe" with the actual path where Python is installed
                bat 'C:\Users\Alaa Oda\AppData\Local\Programs\Python\Python312\\python.exe -m unittest test\\test_api\\test_runner.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
    post {
        always {
            echo 'This will always run as a cleanup or notification step.'
        }
    }
}