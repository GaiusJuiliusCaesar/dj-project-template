/**
 *
 * Requires the Docker Pipeline plugin
 *
 **/

pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile.ci'
      label 'linux'
      customWorkspace '/home/jenkins/workspace'
    }
  }
  stages {
    stage('Check') {
      steps {
        sh 'python --version'
      }
    }
  }
  post {
    always {
      /* Clean up our workspace */
      deleteDir()
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
