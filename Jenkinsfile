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
        stage('Copy deployment files to k8s cluster'){
            steps{
                sh "scp -i /var/lib/jenkins/.ssh/id_rsa deployment_files/k8s_mysql_deployment_files/secret_storage_configmap.yml, svc_deployment.yml bobosunne@10.10.1.34:/home/bobosunne/deployment_files/"
                sh "scp -i /var/lib/jenkins/.ssh/id_rsa deployment/k8s_flaskapp_deployment_files/flask_combined.yml bobosunne@10.10.1.34:/home/bobosunne/deployment_files/"
            }
        }
          
    }
   
}


