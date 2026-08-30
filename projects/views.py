from django.shortcuts import render
from projects.models import Project
from vulnerabilities.models import Finding
from remediation.models import Action

def dashboard(request):
    projects = Project.objects.all()
    total_findings = Finding.objects.count()
    critical_findings = Finding.objects.filter(severity='CRITICAL').count()
    remediations = Action.objects.select_related('finding').all()

    context = {
        'projects': projects,
        'total_findings': total_findings,
        'critical_findings': critical_findings,
        'remediations': remediations,
    }
    return render(request, 'dashboard.html', context)
