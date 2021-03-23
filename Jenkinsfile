// Declarative Pipeline
pipeline {
    agent {label 'first node'}
    triggers {
	//Execute when either job1 or job2 are successful
	upstream(downstreamProjects: 'firstansjob', threshold: hudson.model.Result.SUCCESS)
	   }	
    stages {
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
