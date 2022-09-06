resource "google_compute_instance" "vm_instance" {
  name         = var.instance_name
  zone         = var.instance_zone
  machine_type = var.instance_type
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }
  network_interface {
    network = var.instance_network
    access_config {
      # Allocate a one-to-one NAT IP to the instance
    }
  }
}


resource "google_storage_bucket" "test-bucket-for-state" {
  name                        = "qwiklabs-gcp-01-fcc41be75880"
  location                    = "US"
  uniform_bucket_level_access = true
}
terraform {
  backend "gcs" {
    bucket = "qwiklabs-gcp-01-fcc41be75880"
    prefix = "terraform/state"
  }
}