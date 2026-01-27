# Platform Engineer Coding Test

## Overview
This project implements monitoring, alerting, and automated remediation for web application performance issues.

## Part 1 – Sumo Logic
A query identifies `/api/data` requests exceeding 3 seconds and triggers alerts if more than 5 occur in 10 minutes.

## Part 2 – AWS Lambda
A Python Lambda function reboots an EC2 instance and sends an SNS notification when triggered.

## Part 3 – Terraform
Terraform provisions EC2, Lambda, SNS, and IAM roles following least-privilege principles.

## Deployment
1. Run `terraform init` and `terraform apply`
2. Zip and deploy Lambda code
3. Configure Sumo Logic alert webhook

## Testing
Manual Lambda invocation and simulated alert confirmed EC2 restart and SNS notification.

