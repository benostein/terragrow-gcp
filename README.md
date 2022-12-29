# prerequisite

1. Create service account in IAM GCP and download credentials.json with contain permisson:
* Read/Write Cloud Run IAM permissions
* Read/Write Artifact Registry IAM permissions

2. Enable API each GCP used service:
* Cloud Run
* Cloud Build
* Cloud Artifact

3. Route The registry to Nearest location. we can run this command using glcoud sdk:
```console
gcloud beta artifacts settings enable-upgrade-redirection \
    --project=PROJECT_ID
```
