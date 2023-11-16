## Locust Multi-Core Template

For the first-time use, you can directly initiate the launch. After starting, it will automatically conduct load testing on the built-in API and generate a report. It is recommended to confirm successful execution with the built-in API before modifying the script.

Default load testing duration: 60 seconds

The report will be located at locust/report.html.

---

### QuickStart


```bash

cd locust_multi_core_template 

docker-compose up --scale worker=10 
## execute
## 1 worker = 1 cpu

docker-compose down
# grateful finish

```
---

### Settings


locust/master.conf  
```
host = http://test_api:8080
users = 1000
spawn-rate = 100
run-time = 60s
```


/locust/locustfile.py
```python
from locust import HttpUser,between,task


class WebUser(HttpUser):
    wait_time = between(0.05,0.1)

    @task
    def index(self):
        self.client.get("/ping")
```
