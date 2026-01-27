import json
import boto3
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client("ec2")
sns = boto3.client("sns")

EC2_INSTANCE_ID = os.environ["EC2_INSTANCE_ID"]
SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]

def lambda_handler(event, context):
    try:
        logger.info("Received alert from Sumo Logic")
        logger.info(json.dumps(event))

        # Restart EC2 instance
        ec2.reboot_instances(
            InstanceIds=[EC2_INSTANCE_ID]
        )

        message = f"EC2 instance {EC2_INSTANCE_ID} rebooted due to slow /api/data response"

        # Send SNS notification
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="EC2 Restart Triggered",
            Message=message
        )

        logger.info(message)

        return {
            "statusCode": 200,
            "body": json.dumps("EC2 reboot and SNS notification sent")
        }

    except Exception as e:
        logger.error(str(e))
        raise e

