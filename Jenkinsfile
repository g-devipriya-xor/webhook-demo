//added comments
//added
//version update in jenkins file
//version update
//Not a version update
//not a version update
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code..."
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies..."
                sh 'pip3 install -r requirements.txt || true'
            }
        }

        stage('Run App') {
            steps {
                echo "Running Flask app..."
                sh 'python3 app.py & sleep 5'
            }
        }
    }
}
