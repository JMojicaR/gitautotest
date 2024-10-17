def token
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                token="${Token}"
                python3 -u '/home/javier/Escritorio/ghubpoc/gitautotest/gitauto.py ${token}'
                
            }
        }
    }
}