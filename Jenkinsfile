pipeline {
    agent any

    stages {
        stage('Clone Git Repo') {
            steps {
                echo 'Checking Out SCM'
                git branch: 'flaskapp_compose', 
                credentialsId: 'git_cred', 
                url: 'https://github.com/sundayfagbuaro/flaskapp_project.git'
            }
        }
        stage('Build Docker Image') {
            steps{
                echo 'Building Docker Image'
                sh 'docker build -t class-demo-img .'             
            }
        }
        stage('Push Inage to Docker Hub') {
            steps{
                echo "Pushing Image to Docker Hub"
                withCredentials([
                    usernamePassword(credentialsId: 'docker-hub-cred', 
                    passwordVariable: 'docker_pass', 
                    usernameVariable: 'docker_user')]) {
                    sh 'docker login -u ${docker_user -p ${docker_pass}}'
                }
                sh """ 
                    docker tag class-demo-img sundayfagbuaro/class-demo-img:v1
                    docker push sundayfagbuaro/class-demo-img:v1
                """
            }
        }
    }
}
