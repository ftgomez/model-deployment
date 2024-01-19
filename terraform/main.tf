provider "google" {
  region      = "us-central1"
}

resource "google_project_service" "vertex_ai" {
  service = "aiplatform.googleapis.com"
}
