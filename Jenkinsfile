// Declarative Pipeline
pipeline {
    agent {label 'master'}
    parameters {
        string(name: 'USERID', defaultValue: '', 
         description: 'Enter your userid')
    }
#   triggers {
#	//Execute when either job1 or job2 are successful
#	upstream(upstreamProjects: 'firstansjob', threshold: hudson.model.Result.SUCCESS)
#	   }	
    stages {
        stage('Login') {
            steps {
                echo "Active user is now ${params.USERID}"
            }
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
