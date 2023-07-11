terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "~> 3.78"
    }
  }
}

provider "google" {
  project     = var.project_id
  region      = var.region
}

resource "google_project_service" "vertexai" {
  project = var.project_id
  service = "aiplatform.googleapis.com"
}

resource "google_project_iam_binding" "vertexai" {
  project = var.project_id
  role    = "roles/aiplatform.user"
  members = [ "serviceAccount:${var.service_account}" ]
}

resource "google_project_iam_binding" "storage" {
  project = var.project_id
  role    = "roles/storage.admin"
  members = [ "serviceAccount:${var.service_account}" ]
}
