pipeline {
    agent any



    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat "%PYTHON_PATH% -m venv venv"
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