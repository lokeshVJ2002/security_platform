from django.db import models
from vulnerabilities.models import Finding

# Create your models here.
class Action(models.Model):
    STATUS_CHOICES = [
        ('PROPOSED', 'Proposed'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('APPLIED', 'Applied'),
        ('VERIFIED', 'Verified'),
      ]

    finding = models.OneToOneField(Finding, on_delete=models.CASCADE, related_name='remediation')
    recommendation = models.TextField()
    patch_diff = models.TextField(blank=True) # Automated config/file diff
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PROPOSED')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Fix for {self.finding.title} - {self.status}"
