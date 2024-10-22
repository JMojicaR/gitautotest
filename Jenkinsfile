pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 pytestin.py'
                sh 'python3 --version'
            }
        }
    }
}