pipeline {
    agent any
    environment {
        PYTHON_PATH = "C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        PIP_PATH = '"C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe"'
        TEST_REPORTS = 'test-reports'
    }
     stages {
        stage('Setup Environment') {
            steps {
                bat 'call "%PYTHON_PATH%" -m venv venv'
                bat 'call venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'call venv\\Scripts\\pip.exe install -r requirements.txt -m pytest pytest-html'
            }
        }
        stage('Run API Tests with Pytest') {
            steps {
                // Run pytest with the HTML report flag
                bat "%PYTHON_PATH% -m pytest --html=${TEST_REPORTS}\\report.html --self-contained-html"
            }
        }
    }
    post {
        always {

            archiveArtifacts artifacts: "${TEST_REPORTS}/*.html", allowEmptyArchive: true

        }
    }
}