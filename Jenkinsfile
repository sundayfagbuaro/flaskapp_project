pipeline {
    agent any

    stages {
        stage('SCM Checkout') {
            steps {
                script {
                    git branch: 'k8_deploy_test', credentialsId: 'git_pat', url: 'https://github.com/sundayfagbuaro/flaskapp_project.git'
                
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
        //stage('Copy deployment files to k8s cluster'){
        //    steps{
        //        sh "scp -i /var/lib/jenkins/.ssh/id_rsa deployment_files/k8s_mysql_deployment_files/secret_storage_configmap.yml, svc_deployment.yml bobosunne@10.10.1.34:/home/bobosunne/deployment_files/"
        //        sh "scp -i /var/lib/jenkins/.ssh/id_rsa deployment/k8s_flaskapp_deployment_files/flask_combined.yml bobosunne@10.10.1.34:/home/bobosunne/deployment_files/"
        //    }
        //}
        stage('Copy Deployment Files to K8s Cluster') {
            
        }

        stage('Deploy to MySQL Pod to K8s Cluster') {
            steps{
                sh 'cd deployment_files/k8s_mysql_deployment_files'
                withKubeCredentials(kubectlCredentials: [[caCertificate: '', clusterName: 'kubernetes', contextName: '', credentialsId: 'k8s-secret-token', namespace: 'default', serverUrl: 'https://10.10.1.47:6443']]) {
                    sh 'kubectl get node'
                    sh 'kubectl apply -f secret_storage_configmap.yml'
                    sh 'kubectl apply -f svc_deployment.yml'
                }
            }
        }
          
    }
   
}


