import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_core.settings')
django.setup()

from web.models import Profile, Skill, Project, Experience, Education, ContactMessage

def populate():
    print("Populating data...")
    
    # Profile
    # Create User if not exists
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        user = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    else:
        user = User.objects.get(username='admin')

    # Profile
    Profile.objects.all().delete()
    profile = Profile.objects.create(
        user=user,
        full_name="Henry Wanjiru",
        title="Full Stack Developer",
        bio="Experienced full-stack developer skilled in building robust web applications. Proficient in frontend technologies like JavaScript, React, and CSS, with a strong backend foundation in Python, PHP, and SQL/MongoDB databases.",
        email="info@kushpedia.co.ke",
        phone="+254703443827",
        github_link="https://github.com/henrywanjiru",
        linkedin_link="https://linkedin.com/in/henrywanjiru",
    )
    
    print(f"Created Profile: {profile}")

    # Skills
    Skill.objects.all().delete()
    skills_data = [
        ("Python", 90, "fab fa-python"),
        ("Django", 85, "fas fa-code"),
        ("JavaScript", 80, "fab fa-js"),
        ("React", 75, "fab fa-react"),
        ("SQL", 85, "fas fa-database"),
        ("Git", 90, "fab fa-git-alt"),
    ]
    for name, prof, icon in skills_data:
        Skill.objects.create(name=name, proficiency=prof, icon_class=icon)
    print(f"Created {len(skills_data)} skills")

    # Projects
    Project.objects.all().delete()
    projects_data = [
        ("Kingdom of the Planet of the Apes", "A movie fan page with rich interactions.", "projects/apes.jpg", "Django, HTML, CSS"),
        ("To Do List", "A productive task management app.", "projects/todo.jpg", "React, Firebase"),
        ("E-Commerce Store", "Full featured online shop.", "projects/store.jpg", "Django, Stripe"),
    ]
    for title, desc, img, tags in projects_data:
        Project.objects.create(title=title, description=desc, tags=tags)
    print(f"Created {len(projects_data)} projects")

    # Experience
    Experience.objects.all().delete()
    exp1 = Experience.objects.create(
        role="Full Stack Developer",
        company="Tech Solutions Ltd",
        start_date=date(2023, 1, 1),
        is_current=True,
        description="Developing scalable web applications using Django and React."
    )
    print(f"Created Experience: {exp1}")

    # Education
    Education.objects.all().delete()
    edu1 = Education.objects.create(
        degree="BSc. Information Technology",
        institution="Maseno University",
        start_date=date(2019, 9, 1),
        end_date=date(2023, 12, 1),
        description="Graduated with First Class Honors."
    )
    print(f"Created Education: {edu1}")

if __name__ == '__main__':
    populate()
