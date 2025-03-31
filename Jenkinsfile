pipeline {
    agent any

    stages {
        stage('SCM Checkout') {
            steps {
                script {
                    git branch: 'k8_deploy_test', credentialsId: 'git_cred', url: 'https://github.com/sundayfagbuaro/flaskapp_project.git'
                
                }
            }
        }
        stage('Build docker image for app'){
            steps{
                sh """
                    docker build -t k8s-test-img .
                    docker tag k8s-test-img sundayfagbuaro/k8s-test-img:v1
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

                sh 'docker push sundayfagbuaro/k8s-test-img:v1'
            }
        }
        stage('Deploy Kubernetes Pod') {
            steps {
                withKubeCredentials(kubectlCredentials: [[caCertificate: '', clusterName: 'kubernetes', contextName: '', credentialsId: 'k8s-credentials', namespace: 'default', serverUrl: 'https://192.168.1.94:6443']]) {
                    sh 'kubectl get node'
                    script {
                    // Deploy the pod
                    sh 'kubectl apply -f deployment_files/k8s_mysql_deployment_files/secret_storage_configmap.yml'
                    sh 'kubectl apply -f deployment_files/k8s_mysql_deployment_files/svc_deployment.yml'
                    sh 'kubectl apply -f deployment_files/k8s_flaskapp_deployment_files/flask_combined.yml'
                    }
                }
                
            }
        }
          
    }
   
}


