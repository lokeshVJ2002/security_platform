from django.db import models
from scans.models import Scan

# Create your models here.
class Finding(models.Model):
    SEVERITY_CHOICES = [
       ('CRITICAL', 'Critical'),
       ('HIGH', 'High'),
       ('MEDIUM', 'Medium'),
       ('LOW', 'Low'),
       ('INFO', 'Info'),
     ]

    scan = models.ForeignKey(Scan, on_delete=models.CASCADE, related_name='findings')
    title = models.CharField(max_length=255)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    confidence = models.CharField(max_length=20, default='HIGH') # Evidences vs Infernce
    affected_component = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    evidence = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.severity}] {self.title}"

