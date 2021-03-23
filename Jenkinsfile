// Declarative Pipeline
pipeline {
    agent {label 'first node'}
    stages {
        stage('Source') { // Get code
            steps {
                // get code from our Git repository
                git branch:'apache-dep',https://github.com/sagarbaratam/Methodtomadness.git'
            }
        }
        stage('Compile') { // Compile and do unit testing
            steps {
                // run Gradle to execute compile and unit testing
                sh "echo hi"
            }
        }
    }
}
