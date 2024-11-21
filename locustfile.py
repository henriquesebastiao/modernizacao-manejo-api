from locust import HttpUser, between, task


class QuickstartUser(HttpUser):
    wait_time = between(5, 30)

    @task(9)
    def get_all_users(self):
        self.client.get('/user')

    @task(4)
    def get_user_by_id(self):
        self.client.get('/user/1')

    @task(2)
    def get_all_farmers(self):
        self.client.get('/farmer')

    @task(2)
    def get_all_farms(self):
        self.client.get('/farm')

    @task(1)
    def get_all_employments(self):
        self.client.get('/employment')

    @task(6)
    def not_found(self):
        self.client.get('/not_found')
