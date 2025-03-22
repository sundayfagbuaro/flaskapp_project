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
                    
                    sh "docker login -u ${docker_user} -p ${docker_pass}"
                }
                sh    "docker tag class-demo-img sundayfagbuaro/class-demo-img:v1"
                sh    "docker push sundayfagbuaro/class-demo-img:v1"
                
            }
        }

        stage('Copy docker-compose file to docker host'){
            steps{
                echo "Coping Deployment file to remote host"
                sh "scp -i /var/lib/jenkins/.ssh/id_rsa docker-compose.yml bobosunne@10.10.1.42:/home/bobosunne/class_demo_deploy/"
                sh "scp -i /var/lib/jenkins/.ssh/id_rsa init.sql bobosunne@10.10.1.42:/home/bobosunne/class_demo_deploy/"
                    
            }
        }
        stage('Deploy App on The Remote Host') {
            steps{
                script{
                    echo "Running Containers on the remote host"
                    sshagent(['jenkins-bobosunne']) {
                       sh """
                            ssh -tt -o StrictHostKeyChecking=no bobosunne@10.10.1.42 << EOF
                            cd class_demo_deploy
                            docker compose up -d
                            docker compose ps
                            exit
                            EOF
                        """              
                    }
                }
            }
        }
    }
}
