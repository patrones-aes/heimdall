from subscription.subscription_model import Subscription

class SubscriptionRepository:
    def __init__(self):
        if not Subscription.exists():
            Subscription.create_table(
                read_capacity_units=1,
                write_capacity_units=1,
                wait=True
            )

    def get_all(self):
        return list(Subscription.scan())

    def create(self, body):
        new_subscription = Subscription(**body)
        new_subscription.save()
        return new_subscription.get_attributes()
