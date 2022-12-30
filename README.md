# Prerequisite

1. Create service account in IAM GCP and download `credentials.json` with contain following permisson:
* Read/Write Cloud Run IAM permissions
* Read/Write Artifact Registry IAM permissions
* Read/Write Storage Admin

2. Enable API each GCP used service:
* Cloud Run
* Cloud Build
* Cloud Container Registry / Artifact Registry

3. Create Github secret in desired environment name to secure sensitive information
