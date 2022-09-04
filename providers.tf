provider "google" {
  project = var.project_id
  region  = var.region
}

terraform {
  backend "gcs" {
    bucket = var.terraform_bucket
    prefix = var.terraform_bucket_state_path
  }
}