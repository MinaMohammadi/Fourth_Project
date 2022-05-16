from faker import Faker
import datetime

fake = Faker()
n = datetime.datetime.now(datetime.timezone.utc)

def get_users():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "Timestamp": n.isoformat()
    }

if __name__ == "__main__":
    print(get_users())
