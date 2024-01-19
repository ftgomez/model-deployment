provider "google" {
  region  = var.gcp_region
  project = var.gcp_project
}

resource "google_project_service" "vertex_ai" {
  service = "aiplatform.googleapis.com"
}
