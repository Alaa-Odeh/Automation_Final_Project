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

        stage('Run Tests in Parallel') {
            steps {
                script {
                    parallel(
                        'API Test': {
                            bat "docker run --name tests.test_web.test_log_in_page.Login_Page_Test.test_run ${IMAGE_NAME}:${TAG} python tests.test_web.test_log_in_page.Login_Page_Test.test_run.py"
                            bat "docker rm tests.test_web.test_log_in_page.Login_Page_Test.test_run"
                        }

                    )
                }
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