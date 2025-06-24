from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

# Create your models here.
class Tasks(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('Title', max_length=150, db_index=True, null=False)
    jira_id = models.CharField('Jira Id', max_length=100, db_index=True)
    objective = models.TextField('Objective')
    current_status = models.CharField('Current Status', max_length=50, db_index=True)
    steps_taken = models.TextField('Steps Taken')
    relevant_links = ArrayField(models.URLField(), blank=True, default=list)
    next_steps = models.TextField('Next steps')
    def __str__(self):
        return f"{self.title} ({self.jira_id})"
    class Meta:
        ordering = ['-id']
        db_table = 'tasks'