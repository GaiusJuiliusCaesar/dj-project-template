/**
 *
 * Requires the Docker Pipeline plugin
 *
 **/

pipeline {
  agent {
      label 'linux'
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t dj_template -f Dockerfile.ci .'
      }
    }
    stage('Run') {
      steps {
        sh 'docker run --rm dj_template'
      }
    }
  }
  post {
    always {
      script {
        /* Clean up our workspace */
        if (getContext (hudson.FilePath)) {
          deleteDir()
        }
      }
    }
    success {
      echo 'I succeeded!'
    }
    unstable {
      echo 'I am unstable :/'
    }
    failure {
      echo 'I failed :('
    }
    changed {
      echo 'Things were different before...'
    }
  }
}
