from django.core.files.storage import FileSystemStorage

def loadTo(name, file, folder):
    storage = FileSystemStorage()
    storage.location += folder

    name = storage.save(name, file)
    return folder + '\\' + name
