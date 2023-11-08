import boto3

dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

table = dynamodb.create_table(
    TableName='games',
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH',
        }
    ],
    AttributeDefinitions=[{'AttributeName': 'name', 'AttributeType': 'S'}],
    ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5},
)


print(f'Table status: {table.table_status}')
