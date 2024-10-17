def token
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                token="${Token}"
                sh "python3 -u '/home/javier/Escritorio/bashCourse/test.py ${token}'"
            }
        }
    }
}