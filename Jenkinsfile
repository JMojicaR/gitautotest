def token
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                token=${Token}
                sh 'python3 gitauto.py ${token}'
            }
        }
    }
}