stage ('Test') {
// execute required unit tests in parallel

   parallel (
      master: { node ('master'){
         sh 'date'
      }},
      worker2: { node ('first node'){
         sh 'dmidecode'
      }},
   )
}