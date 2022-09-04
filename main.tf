resource "google_storage_bucket" "test-bucket" {
  name                        = "my-test-bucket"
  location                    = "europe-north1"
  uniform_bucket_level_access = true
}