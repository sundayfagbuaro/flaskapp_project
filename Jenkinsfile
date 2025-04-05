pipeline {
    agent any

    stages{
        stage('Clone Git Repository') {
            steps{
                git branch: 'k8_real', 
                credentialsId: 'git_cred', 
                url: 'https://github.com/sundayfagbuaro/flaskapp_project.git'
            }
            
        }
        stage('Build Docker Image') {
            steps{
                sh "docker build -t k8s-deploy-demo ."
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
                sh "docker tag k8s-deploy-demo sundayfagbuaro/k8s-deploy-demo:v1"
                sh "docker push sundayfagbuaro/k8s-deploy-demo:v1"
            }
        }
        stage('Deploy to K8s Cluster') {
            steps{
                withKubeCredentials(kubectlCredentials: [[caCertificate: '', clusterName: '', contextName: '', credentialsId: 'k8s-cred', namespace: 'default', serverUrl: 'https://10.10.1.47:6443']]) {
                    sh 'kubectl apply -f deployment_files/secret_storage_configmap.yml'
                    sh 'kubectl apply -f deployment_files/svc_deployment.yml'
                    sh 'kubectl apply -f deployment_files/flask_combined.yml'

                }
            }
        }
        
    }
}



    