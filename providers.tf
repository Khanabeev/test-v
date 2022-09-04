provider "google" {
  project = var.project_id
  region  = var.region
}

terraform {
  backend "gcs" {
    bucket = "vapaus-terraform-staging"
    prefix = "terraform/state"
  }
}