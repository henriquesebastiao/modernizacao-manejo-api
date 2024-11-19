# Usage: locust -f locustfile.py --headless --users 10 --spawn-rate 1 -H http://localhost:8000
from locust import HttpUser, between, task


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(10)
    def root(self):
        self.client.get('/', name='/root')

    @task(5)
    def get_all_users(self):
        self.client.get('/user', name='/user')

    @task(5)
    def get_all_farmers(self):
        self.client.get('/farmer', name='/farmer')

    @task(3)
    def get_all_farms(self):
        self.client.get('/farm', name='/farm')

    @task(10)
    def employment(self):
        self.client.get('/employment', name='/employment')

    @task(9)
    def create_employee(self):
        self.client.post(
            '/user/employee',
            json={
                'first_name': 'string',
                'last_name': 'string',
                'email': 'user@example.com',
                'password': 'string',
                'phone': '66999999999',
            },
            name='/user/employee',
        )

    @task(15)
    def not_found(self):
        self.client.get('/not_found', name='/not_found')
