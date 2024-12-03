import azure.functions as func
import logging
MONGO_URI = "mongodb://autocomppoc:fqX5VFRG7VF9LJ0TgvWMGPGyNwLJQmNVrT3qiNks1iZSjJdbMVFJvnOVYLqw1C76xtdi7eS6gdvfACDbStHCVg==@autocomppoc.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@autocomppoc@"
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
user = "savita"
password = "fqX5VFRG7VF9LJ0TgvWMGPGyNwLJQmNVrT3qiNks1iZSjJdbMVFJvnOVYLqw1C76xtdi7eS6gdvfACDbStHCVg!"
@app.route(route="GetDetails")
def GetDetails(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a incoming request.')

    name = req.params.get('name')
    job = req.params.get('job')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if not job:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name} with job as {job}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name and job in the query string or in the request body for a personalized response.",
             status_code=200
        )