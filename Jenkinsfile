// Declarative Pipeline
pipeline {
    agent {label 'master'}
    parameters {
        string(name: 'USERID', defaultValue: '', 
         description: 'Enter your userid')
    }	
    stages {
        stage('Login') {
            steps {
                echo "Active user is now ${params.USERID}"
            }
        }
        stage ('Test') {
       // execute required unit tests in parallel

   parallel (
      master: { node ('master'){
         sh 'date'
      }},
      worker2: { node ('first node'){
         sh 'java --version'
      }},
   )
}

        stage('Source') { // Get code
            steps {
                // get code from our Git repository
                git branch:'apache-dep',
		       url:'https://github.com/sagarbaratam/Methodtomadness.git'
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
