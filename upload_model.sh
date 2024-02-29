PROJECT_ID="kubeflow-project-403002"
REGION="us-central1"
REPOSITORY="vertex-ai-models-repo"
IMAGE_TAG="tomas_model:latest"
JSON_FILE="kubeflow-project-403002-95f27c6e1770_1.json"

gcloud auth configure-docker $REGION-docker.pkg.dev
gcloud auth activate-service-account --key-file=$JSON_FILE

docker build . -t $REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE_TAG
docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE_TAG