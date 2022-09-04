variable "project_id" {
  type        = string
  description = "development-359007"
}

variable "region" {
  type    = string
  default = "europe-north1"
}

variable "terraform_bucket" {
  type    = string
  default = "vapaus-terraform-bucket"
}

variable "terraform_bucket_state_path" {
  type    = string
  default = "terraform/state"
}