from mongrations import Mongrations, Database
from pydotenv import load_env, load_env_object

# load_env()  # connect via environment variables (default)
config = load_env_object('.env-example-example-example')  # by default it looks for .env-example-example in the current directory


class Mongration(Database):
    def __init__(self):
        super(Database, self).__init__()

    def up(self):
        self.db['test_collection'].insert_one({'hello': 'world'})

    def down(self):
        self.db['test_collection'].delete_one({'hello': 'world'})


Mongrations(Mongration, 'async', connection_obj=config)
