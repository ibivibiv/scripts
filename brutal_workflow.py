import uuid
import pprint
import time
import datetime
from conductor import conductor

test_workflow = {
    "createTime": 1530249600686,
    "name": "Abuser Test Workflow",
    "description": "This is a test workflow to abuse conductor",
    "version": 1,
    "schemaVersion": 2,
    "tasks": [

        {
            "name": "task_20",
            "taskReferenceName": "task_20",
            "type": "SIMPLE",
            "startDelay": 0,

        },

        {
            "name": "task_21",
            "taskReferenceName": "task_21",
            "type": "SIMPLE",
            "startDelay": 0,

        },

        {
            "name": "task_22",
            "taskReferenceName": "task_22",
            "type": "SIMPLE",
            "startDelay": 0,

        },

        {
            "name": "task_23",
            "taskReferenceName": "task_23",
            "type": "SIMPLE",
            "startDelay": 0,

        },

        {
            "name": "task_24",
            "taskReferenceName": "task_24",
            "type": "SIMPLE",
            "startDelay": 0,

        }

    ]
}

start = {
    "uuid": str(uuid.uuid4()),
    "version": 2
}

file = open(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))+".csv", "w")

try:

    base = 'http://169.46.11.166:8080/api'

    pp = pprint.PrettyPrinter()

    workflowClient = conductor.WorkflowClient(base)

    taskClient = conductor.TaskClient(base)

    metaClient = conductor.MetadataClient(base)

    #we don't care here we just want to load the data if it is missing
    try:
        response = metaClient.createWorkflowDef(test_workflow)
    except Exception as e :
        print(e)
        pass

    while True :
        try:
            response = workflowClient.startWorkflow(wfName="Abuser Test Workflow", inputjson=start)
            file.write(str(time.time()) + ", workflowstart \r")
        except Exception as e :
            print(e)
            file.write(str(time.time()) + ", workflowstartfail \r")

        time.sleep(5)

except Exception as e :
    print(e)
    pass
finally :
    file.close
