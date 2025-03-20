pipeline {
    agent any

    stages {
        stage('Clone Git Repo') {
            steps {
                echo 'Checking Out SCM'
                git branch: 'flask app_compose', 
                credentialsId: 'git_cred', 
                url: 'https://github.com/sundayfagbuaro/flaskapp_project.git'
            }
        }
    }
}
