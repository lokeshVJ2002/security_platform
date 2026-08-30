from django.db import models
from projects.models import Project

class Scan(models.Model):
    SCAN_TYPES = [
        ('APK', 'APK Security'),
        ('AI', 'AI Gateway'),
        ('CLOUD', 'Cloud Infrastructure'),
        ('DEP', 'Dependencies'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('RUNNING', 'Running'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='scans')
    scan_type = models.CharField(max_length=10, choices=SCAN_TYPES)
    target = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.scan_type} - {self.target} ({self.status})"

