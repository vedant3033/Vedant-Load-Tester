from locust import HttpUser, task, between, events

class WebsiteUser(HttpUser):
    wait_time = between(0.5, 1)

    @task(3)
    def index_page(self):
        self.client.get("/home/")

    @task(2)
    def history_page(self):
        self.client.get("/history/")

    @task(1)
    def boarding_page(self):
        self.client.get("/colvin-boarding-house/")

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    if environment.web_ui:
        @environment.web_ui.app.after_request
        def add_custom_branding(response):
            if response.content_type and 'text/html' in response.content_type:
                html = response.get_data(as_text=True)
                html = html.replace('<title>Locust</title>', '<title>Vedant HTTP Performance Tester</title>')
                response.set_data(html)
            return response
