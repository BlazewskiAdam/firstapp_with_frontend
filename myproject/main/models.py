from django.db import models

class Champion(models.Model):
    name = models.CharField(max_length=100)  
    cost = models.IntegerField()
    passive = models.CharField(max_length=20000)
    lor_type = models.CharField(max_length=100)


class todolist(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def status_check(self):
        if self.status == True:
            return "this todolist is completed"
        else:
            return "this todolist isnt completed"
        
class task(models.Model):
    todolist = models.ForeignKey(todolist, on_delete=models.CASCADE, related_name="tasks")
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)


