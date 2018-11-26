import pprint
import time
import datetime
from conductor import conductor

file = open(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))+".csv", "w")

try:
    base = 'http://169.46.11.166:8080/api'

    pp = pprint.PrettyPrinter()

    workflowClient = conductor.WorkflowClient(base)

    taskClient = conductor.TaskClient(base)

    metaClient = conductor.MetadataClient(base)

    while True:

        workflow_list = workflowClient.getRunningWorkflows(wfName="Abuser Test Workflow")

        for wfId in workflow_list:

            workflow = workflowClient.getWorkflow(wfId=wfId, includeTasks=True)

            for task in workflow['tasks']:
                workflowId = str(task['workflowInstanceId']).strip()
                taskId = str(task['taskId']).strip()

                taskObj = taskClient.getTask(taskId)
                taskObj['status'] = "COMPLETED"
                taskObj['workerId'] = "test"
                try:
                    response = taskClient.ackTask(taskId, "brutalizer")
                    response = taskClient.updateTask(taskObj=taskObj)
                    pp.pprint("completed")
                    file.write(str(time.time())+", taskcomplete \r")
                except Exception as e:
                    if "Extra data" in str(e) or "Expecting" in str(e):
                        pp.pprint("completed")
                        file.write(str(time.time()) + ", taskcomplete \r")
                    else:
                        pp.pprint(e)
                        file.write(str(time.time()) + ", taskerror \r")
except Exception as e:
    pass

finally :
    file.close()
