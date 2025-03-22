pipeline {
    agent any

    stages{
        stage('Clone Git Repository') {
            git branch: 'class_demo', 
            credentialsId: 'git_cred', 
            url: 'https://github.com/sundayfagbuaro/flaskapp_project.git'
        }
    }
}



    