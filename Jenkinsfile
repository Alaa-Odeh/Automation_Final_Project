pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def customImage = docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Run API Test') {
            steps {
                bat "docker run --name tests.test_api.test_runner ${IMAGE_NAME}:${TAG} python tests.test_api.test_runner.py"
                bat "docker rm tests.test_api.test_runner"
            }
        }

    }

    post {
        always {
            echo 'Cleaning up...'
            bat "docker rmi ${IMAGE_NAME}:${TAG}"
        }
    }
}