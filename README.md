# Prerequisite

1. Create service account in IAM GCP and download `credentials.json` with contain following permisson:
* Read/Write Cloud Run IAM permissions
* Read/Write Artifact Registry IAM permissions
* Read/Write Storage Admin

2. Enable API each GCP used service:
* Cloud Run
* Cloud Build
* Cloud Artifact

3. Route The registry to Nearest location. We can run this command using glcoud sdk:
```console
gcloud beta artifacts settings enable-upgrade-redirection \
    --project=PROJECT_ID
```
Note: Change the `PROJECT_ID` to your GCP Project ID
