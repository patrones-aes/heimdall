from typing import Dict, Any, Type

import boto3
from botocore.exceptions import ClientError
from modi.config.settings import settings
from modi.core.base_model import BaseModel


class DatabaseConnection:
    """
    Database connection
    """
    def __init__(self, model: Type[BaseModel]):
        self.model = model
        self.connection = boto3.resource(
            'dynamodb',
            endpoint_url=settings.DYNAMODB_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_DEFAULT_REGION,
        )
        self.table = self.connection.Table(model.table_name)
        self._ensure_table()

    def _create_table(self):
        """
        Create the table using metadata from the model.
        """
        metadata = self.model.get_table_metadata()
        try:
            self.table = self.connection.create_table(**metadata)
            print(f"Waiting for table '{self.model.table_name}' to be created...")
            self.table.wait_until_exists()
            print(f"Table '{self.model.table_name}' created successfully.")
        except ClientError as e:
            print(f"Failed to create table '{self.model.table_name}': {e.response['Error']['Message']}")
            raise

    def _ensure_table(self):
        """
        Ensure the table exists; create it if it doesn't.
        """
        try:
            self.table.load()  # Check if the table exists
            print(f"Table '{self.model.table_name}' already exists.")
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                print(f"Table '{self.model.table_name}' does not exist. Creating it...")
                self._create_table()
            else:
                raise

    def __call__(self):
        return self

    def scan_table(self) -> Dict[str, Any]:
        """
        Scan the entire table.
        """
        return self.table.scan()

    def get_item(self, key: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get an item by primary key.
        """
        return self.table.get_item(Key=key)

    def put_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """
        Insert or update an item.
        """
        return self.table.put_item(Item=item)

    def delete_item(self, key: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delete an item by primary key.
        """
        return self.table.delete_item(Key=key)

    def update_item(self, key: Dict[str, Any],
                    update_expression: str,
                    expression_values: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an item by primary key.
        """
        return self.table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values,
            ReturnValues="UPDATED_NEW",
        )
