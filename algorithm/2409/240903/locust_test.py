from locust import HttpUser, task, between
from itertools import cycle

email_list = [
    "email0@example.com"
]

email_iterator = cycle(email_list)

class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://localhost:8080"  # 여기에 호스트 URL을 설정합니다.

    @task
    def post_request(self):
        headers = {'Content-Type': 'application/json'}
        email = next(email_iterator)
        payload = {
            'memberEmail': email,
            'subjectName': 'COMPUTERSCIENCE'
        }
        self.client.post('/registration', headers=headers, json=payload)
