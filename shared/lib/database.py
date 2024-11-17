from typing import Dict, Any

import boto3

class DatabaseConnection:
    def __init__(self, table_name: str,
                 endpoint_url=None, region_name='us-east-1',
                 aws_access_key_id=None, aws_secret_access_key=None):
        self.connection = boto3.resource(
            'dynamodb',
            endpoint_url=endpoint_url,
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        self.table = self.connection.Table(table_name)

    def scan_table(self) -> Dict[str, Any]:
        """Scan the entire table."""
        return self.table.scan()

    def get_item(self, key: Dict[str, Any]) -> Dict[str, Any]:
        """Get an item by primary key."""
        return self.table.get_item(Key=key)

    def put_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Insert or update an item."""
        return self.table.put_item(Item=item)

    def delete_item(self, key: Dict[str, Any]) -> Dict[str, Any]:
        """Delete an item by primary key."""
        return self.table.delete_item(Key=key)

    def update_item(self, key: Dict[str, Any],
                    update_expression: str, expression_values: Dict[str, Any]) -> Dict[str, Any]:
        """Update an item by primary key."""
        return self.table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values,
            ReturnValues="UPDATED_NEW",
        )
