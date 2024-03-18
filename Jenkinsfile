pipeline {
    agent any
    environment {
        PYTHON_PATH = "C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        PIP_PATH = "C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe"
        TEST_REPORTS = 'test-reports'
    }
    stages {
        stage('Setup Environment') {
            steps {
                bat 'call "%PYTHON_PATH%" -m venv venv'
                bat 'call venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'call venv\\Scripts\\pip.exe install -r requirements.txt'
                bat 'call venv\\Scripts\\pip.exe install pytest pytest-html'
            }
        }
        stage('Run API Tests with Pytest') {
            steps {
                bat 'call venv\\Scripts\\pytest tests/test_api/api_test_runner.py --html=%TEST_REPORTS%\\report.html --self-contained-html'
            }
        }

    }
     post {
        always {
            junit '**/test-reports/*.xml'
            archiveArtifacts artifacts: 'test-reports/*.html', allowEmptyArchive: true
        }
    }
  }