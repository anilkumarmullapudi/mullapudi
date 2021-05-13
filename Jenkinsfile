pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'echo "today\'s date is: $(date) "'
      }
    }

  }
  environment {
    server1 = 'web'
  }
}