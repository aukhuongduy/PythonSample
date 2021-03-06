from flask_restful import Resource, reqparse
from models.task import Task
from models.task import Message
import mlab


class TaskListRes(Resource):
    def get(self):
        tasks = Task.objects()
        tasks_json = mlab.list2json(tasks)
        return tasks_json

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(name="local_id", type=str, location="json")
        body = parser.parse_args()
        name = body["name"]
        local_id = body["local_id"]

        task = Task(name=name, local_id=local_id, done=False)
        task.save()

        added_task = Task.objects().with_id(task.id)
        return mlab.item2json(added_task)


class TaskRes(Resource):
    def get(self, task_id):
        task = Task.objects.with_id(task_id)
        return mlab.item2json(task)

    def put(self, task_id):
        task = Task.objects.with_id(task_id)
        parser = reqparse.RequestParser()
        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(name="done", type=bool, location="json")
        body = parser.parse_args()
        name = body["name"]
        done = body["done"]

        task.update(set__done=done,set__name=name)
        edited_task = Task.objects.with_id(task_id)
        return mlab.item2json(edited_task)
    def delete(self,task_id):
        task = Task.objects.with_id(task_id)
        task.delete()
        message = Message(message="Deleted")
        return mlab.item2json(message)
