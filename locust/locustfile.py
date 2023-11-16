from locust import HttpUser,between,task


class WebUser(HttpUser):
    wait_time = between(0.05,0.1)
    ## 每個使用者 每 0.05 - 0.1 秒 執行一次

    @task
    def index(self):
        self.client.get("/ping")




