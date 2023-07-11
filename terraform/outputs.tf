output "enabled_services" {
  description = "The services that were enabled in this project"
  value       = [google_project_service.vertexai.service]
}

output "iam_roles" {
  description = "The roles that were assigned to the service account"
  value       = [google_project_iam_binding.vertexai.role, google_project_iam_binding.storage.role]
}
