import json, boto3

def producer_lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(
        QueueName='StandardQueue'
    )

    body = json.loads(event['body'])
    message = body['message']

    response = queue.send_message(
        MessageBody=message
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message_id": response['MessageId']
        }),
    }


def topic_lambda_handler(event, context):
    body = json.loads(event['body'])
    message = body['message']

    sns = boto3.resource('sns')
    topic = sns.create_topic(Name='SampleTopic')

    response = topic.publish(
        Message=message
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message_id": response['MessageId']
        }),
    }


def consumer_lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(
        QueueName='StandardQueue'
    )

    messages = queue.receive_messages(MaxNumberOfMessages=10)

    message_bodies = []

    if messages:
        for message in messages:
            message_bodies.append(message.body)
            message.delete()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "messages": message_bodies
        }),
    }

event = {
  "body": "{\"message\": \"hello world\"}"
}