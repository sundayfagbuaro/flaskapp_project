pipeline {
    agent any

    stages {
        stage('SCM Checkout') {
            steps {
                script {
                    git branch: 'k8_deploy_test', credentialsId: 'git-pat', url: 'https://github.com/sundayfagbuaro/flaskapp_project.git'
                
                }
            }
        }
        stage('Build docker image for app'){
            steps{
                sh """
                    docker build -t test-img .
                    docker tag test-img sundayfagbuaro/test-img
                """
            }
        }
        stage('Push Docker Image To DockerHub') {
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-cred', 
                    passwordVariable: 'docker_pass', 
                    usernameVariable: 'docker_user')]) {
                    
                sh 'docker login -u ${docker_user} -p ${docker_pass}'
                }

                sh 'docker push sundayfagbuaro/test-img'
            }
        }
        stage('SSH To K8s Cluster') {
            steps{
                def remote = [:]
                remote.name = 'k8-master-test'
                remote.host = '10.10.1.34'
                remote.user = 'bobosunne'
                remote.password = 'P@ssWord1'
                remote.AllowAnyHost = true
            }
        }
            stage('Put Deployment files to k8 cluster') {
            steps{
                sshput remote: remote, from: 'deployment_files/k8s_mysql_deployment_files/secret_storage_configmap.yml, svc_deployment.yml', into: '~/deployment_files/'
                sshput remote: remote, from: 'deployment/k8s_flaskapp_deployment_files/flask_combined.yml', into: '~/deployment_files/'
            }
        }
        stage('Deploy App') {
            sshcommand remote: remote, command: 'kubectl apply -f deployment_files/secret_storage_configmap.yml'
            sshcommand remote: remote, command: 'kubectl apply -f deployment_files/svc_deployment.yml'
            sshcommand remote: remote, command: 'kubectl apply -f deployment_files/flask_combined.yml'
        }
        
    }
}


