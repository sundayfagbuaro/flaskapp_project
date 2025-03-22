pipeline {
    agent any

    stages{
        stage('Clone Git Repository') {
            steps{
                git branch: 'class_demo', 
                credentialsId: 'git_cred', 
                url: 'https://github.com/sundayfagbuaro/flaskapp_project.git'
            }
            
        }
        stage('Build Docker Image') {
            steps{
                sh "docker build -t class-flaskapp-demo ."
                sh "docker image ls"
            }
        }
        stage('Push Image to Docker Hub') {
            steps{
                withCredentials([
                    usernamePassword(credentialsId: 'docker-hub-cred', 
                    passwordVariable: 'docker_password', 
                    usernameVariable: 'docker_username')]) {
                sh "docker login -u ${docker_username} -p ${docker_password}"
            }
                sh "docker tag class-flaskapp-demo sundayfagbuaro/class-flaskapp-demo:v1"
                sh "docker push sundayfagbuaro/class-flaskapp-demo:v1"
            }
        }
        stage('Copy deployment files to remote docker host'){
            steps{
                sh "scp -i /var/lib/jenkins/id_rsa docker-compose.yml bobosunne@10.10.1.42:/home/bobosunne/class_demo_deploy/"
                sh "scp -i /var/lib/jenkins/id_rsa db_init.sql bobosunne@10.10.1.42:/home/bobosunne/class_demo_deploy/"
            }
        }
        stage('Deploy Flaskapp to Docker Host') {
            steps{
                echo "Deloying Application to Docker Host"
                sshagent(['jenkins-bobosunne']) {
                    sh """
                        ssh -tt -o StrictHostKeyChecking=no bobosunne@10.10.142 << EOF
                        cd class_demo_deploy
                        docker compose up -d
                        exit
                        EOF
                     """
                }
            }
        }
    }
}



    