class METHOD_TYPE:
    @property
    def get(self):
        return "GET"
    @property
    def post(self):
        return "POST"
    @property
    def delete(self):
        return "DELETE"
    @property
    def put(self):
        return "PUT"
    @property
    def path(self):
        return "PATH"

method = METHOD_TYPE()