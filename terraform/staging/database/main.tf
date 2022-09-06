resource "google_sql_database_instance" "main" {
  name             = "test-instance"
  database_version = "POSTGRES_14"
  region           = "europe-north1"

  settings {
    tier = "db-f1-micro"
  }
}