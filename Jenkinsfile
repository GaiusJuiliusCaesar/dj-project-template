pipeline {
	agent any
		stages {
			stage('Stage 1') {
				steps {
					echo "This is Stage 1 Step 1."
				}
				steps {
					sh "echo $PWD"
				}
			}
			stage('Stage 2') {
				steps {
					echo "This is Stage 2 Step 1."
				}
				steps {
					sh "echo $PWD"
				}
			}
		}
	post {
		always {
			echo 'One way or another, I have finished'
				deleteDir() /* clean up our workspace */
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
