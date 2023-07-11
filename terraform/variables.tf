variable "project_id" {
  description = "ID of the project you want to use"
  type        = string
}

variable "region" {
  description = "Region of your project"
  default     = "us-central1"
}

variable "service_account" {
  description = "Service Account ID"
  type        = string
}
