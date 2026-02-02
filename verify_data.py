import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_core.settings')
django.setup()

from web.models import Skill, Project

def verify():
    skill_count = Skill.objects.count()
    project_count = Project.objects.count()
    
    print(f"Skills count: {skill_count}")
    print(f"Projects count: {project_count}")
    
    if skill_count > 0:
        print("First Skill:", Skill.objects.first())
    if project_count > 0:
        print("First Project:", Project.objects.first())

if __name__ == '__main__':
    verify()
