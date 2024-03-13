pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'maven:3-alpine'
                    args '-v /home/user/.m2:/root/.m2'
                }
            }
            steps {
                bat 'mvn -B clean package'
            }
        }
    }
}