resource "aws_lambda_function" "restart_lambda" {
  function_name = "restart-ec2-on-alert"
  role          = aws_iam_role.lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"
  filename      = "../lambda_function/lambda.zip"

  environment {
    variables = {
      EC2_INSTANCE_ID = aws_instance.web.id
      SNS_TOPIC_ARN   = aws_sns_topic.alert_topic.arn
    }
  }
}

