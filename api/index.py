from weather_project.wsgi import handler

def lambda_handler(event, context):
    return handler(event, context) 