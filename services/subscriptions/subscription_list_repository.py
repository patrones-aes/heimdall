import uuid

subscriptions = []

class SubscriptionListRepository:
    def get_all(self):
        return subscriptions

    def create(self, body):
        body['id'] = uuid.uuid4()
        return subscriptions.append(body)
