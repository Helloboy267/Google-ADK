terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 4.0.0"
    }
  }
  required_version = ">= 1.3.0"
}

provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

resource "google_cloud_run_v2_service" "accessibility_agent" {
  name     = "accessibility-agent"
  location = var.gcp_region
  template {
    containers {
      image = var.container_image
      env {
        name  = "GEMINI_API_KEY"
        value = var.gemini_api_key
      }
      env {
        name  = "GCP_PROJECT_ID"
        value = var.gcp_project_id
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
}

variable "gcp_project_id" { default = "causal-tracker-464305-f7" }
variable "gcp_region" { default = "us-central1" }
variable "container_image" {}
variable "gemini_api_key" {}
variable "service_name" { default = "accessibility-agent-service" }
variable "google_cloud_location" { default = "us-central1" }
