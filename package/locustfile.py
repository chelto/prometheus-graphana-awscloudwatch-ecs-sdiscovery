from locust import User, task, between

class MyUser(User):
    @task
    def my_task(self):
        print("executing my_task")

    wait_time = between(0.5, 10)
    
    
    
from locust.contrib.fasthttp import FastHttpUser
import time
from locust.user import task
from locust.user.users import HttpUser
class UserTasks(FastHttpUser):
     @task
     def get_root(self):
        while self.environment.runner.user_count < self.environment.runner.target_user_count:
            time.sleep(1)
        self.client.get("/")