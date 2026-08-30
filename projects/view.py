from django.shortcuts import render
from projects.models import Project
from vulnerabilities.models import Finding
from remediation.models import Action

def dashboard(request):
    projects = Project.objects.all()
    findings = Finding.objects.all()
    
    # Case-insensitive check for critical findings
    critical_findings = Finding.objects.filter(severity__iexact='CRITICAL').count()
    
    # Fetch actions linked to findings
    remediations = Action.objects.select_related('finding').all()

    context = {
        'projects': projects,
        'findings': findings,
        'total_findings': findings.count(),
        'critical_findings': critical_findings,
        'remediations': remediations,
    }
    return render(request, 'dashboard.html', context)
