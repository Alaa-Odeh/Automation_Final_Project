pipeline {
    agent any
    stages {
        stage('Selenium Tests') {
            steps {
                // Assuming you have a script to set up and run Python Selenium tests
                bat 'python -m unittest discover -s tests/test_web -p test_log_in_page.test_run.py'
            }

        }
    }
}