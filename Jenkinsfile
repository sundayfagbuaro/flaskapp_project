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
                sh "docker tag class-flaskapp-demo sundayfagbauro/class-flaskapp-demo:v1.0"
                sh "docker push sundayfagbauro/class-flaskapp-demo:v1.0"
            }
        }

    }
}



    