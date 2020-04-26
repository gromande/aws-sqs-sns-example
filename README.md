# AWS SQS and SNS Examples

This project contains some examples to showcase how SQS and SNS Topics work. The deployment process will create three public APIs:

- Producer: parses the JSON request payload and sends a message to the SQS queue
- Topic Publisher: parses the JSON request payload and publishes a message to the SNS topic
- Consumer: receives messages from the SQS queue and returns them as JSON

## Deploy the application

First, you will need to install the Serverless Application Model Command Line Interface (SAM CLI).
To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modified IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Tests
Produce new message:
```bash
curl -X POST --data '{"message":"Message for Producer"}' https://{API HOSTNAME}/Prod/producer
```

Publish message:
```bash
curl -X POST --data '{"message":"Message for Topic"}' https://{API HOSTNAME}/Prod/topic
```

Consume messages:
```bash
curl https://{API HOSTNAME}/Prod/consumer
```

## Cleanup

To delete the application that you created, you can run the following:

```bash
aws cloudformation delete-stack --stack-name aws-sqs-sns-example
```
