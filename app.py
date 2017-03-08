from flask import Flask
import mlab
from models.task import Task
from flask_restful import Api
from resources.task_resources import *

mlab.connect()
app = Flask(__name__)

api = Api(app)

# all_task = Task.objects()
# for task in all_task:
#       print(mlab.item2json(task))

api.add_resource(TaskListRes,"/tasks")
api.add_resource(TaskRes,"/tasks/<task_id>")

# my_task = Task.objects(name="QuanOcCho").first()
# print(mlab.item2json(my_task))

# my_task.update(set__done=True)
# my_task.delete()

if __name__ == '__main__':
    app.run()
