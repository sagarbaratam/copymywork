pipeline {
      
      stage('Source') {
      git branch: 'test', url: 'git@diyv:repos/gradle-greetings'
      stash name: 'test-source', includes: '/home/ec2-user/test.txt'
   }
   stage ('Test') {
   // execute required unit tests in parallel

      parallel (
         master: { node ('master') {
            unstash 'test-sources'
            sh 'ls -lrt /home/ec2-user/test.txt'
         }},
         worker2: { node ('first node') {
            unstash 'test-sources'
            sh 'ls -lrt /home/ec2-user/test.txt'
         }},
      )
   }
}