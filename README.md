# Prerequisite

1. Create service account in IAM GCP and download `credentials.json` with contain following permisson:
* Read/Write Cloud Run IAM permissions
* Read/Write Artifact Registry IAM permissions
* Read/Write Storage Admin

2. Enable API each GCP service that needed:
* Cloud Run
* Cloud Build
* Cloud Container Registry / Artifact Registry

3. Docker Oauth2 access token. Please refer to this link https://github.com/google-github-actions/auth

3. Create Github secret with desired environment name to secure sensitive information
