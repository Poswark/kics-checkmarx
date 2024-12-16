
pipeline {
    agent {
        docker {
            image 'docker:20.10.7'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    } 
    environment {
        image = 'test'
        tag = 'latest'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh "docker  build  --no-cache -t ${image}:${tag} . "

            }
        }
        stage('scan image') {
            steps {
                sh "docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image --insecure ${image}:${tag}"
            }
        }
        stage('Run KICS Scan') {
            steps {
                sh '''
                docker run -t -v $(pwd):/path checkmarx/kics:latest scan \
                    -p /path -o ./results --report-formats "json,html"
                '''
            }
        }
        stage('Publish Results') {
            steps {
                archiveArtifacts artifacts: 'results/*', fingerprint: true
            }
        }
        stage('push Image') {
            steps {
                sh "docker tag ${image}:${tag} poswark/${image}:${tag}"
                sh "docker push poswark/${image}:${tag}"
            }
        }

    }
}