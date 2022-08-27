from celery_app.celery_settings import app

@app.task
def loadVideo():
    (lambda: print(111111111))()

@app.task
def updateUserAccount(account_id, lst):
    pass
