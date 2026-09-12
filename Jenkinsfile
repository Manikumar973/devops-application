pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Getting source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing application...'
                sh '''python3 -c "from app import app; client=app.test_client(); response=client.get('/health'); assert response.status_code == 200; print(response.json)"'''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t devops-demo:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Docker container...'
                sh 'docker rm -f devops-demo 2>/dev/null || true'
                sh 'docker run -d --name devops-demo -p 5000:5000 devops-demo:latest'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}