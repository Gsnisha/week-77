pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo 'Build a python app'
                bat 'docker build -t flaskapp .'
            }
        }
        stages{
        stage('Run'){
            steps{
                echo 'Run the app'
                bat 'docker rm -f mycontainer || exit0 '
                bat 'docker run -d -p flaskapp 5000:5000 '
            }
        }
        }
        
        stages{
        stage('Push image'){
        steps{
        bat 'docker tag flaskapp:latest nisha1310/simple_demo:latest
        bat 'docker push nisha1310/simple_demo:latest
        }
        }
        post{
        success {
        echo 'Pipeline running successfully'
        docker portforward service/myflaskapp service 5003:5000
        }
        failure{
        echo 'Pipeline failed please check the logs.'
        }
        }
    }
}
        
