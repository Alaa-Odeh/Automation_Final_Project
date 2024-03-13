pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Your build steps go here
            }
        }
        stage('Test') {
            steps {
                echo 'Running API tests...'
                python -m test_api.test_runner
                sh 'python3 -m unittest tests/test_api/test_runner.py'
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