from PyPDF2 import PdfReader


SKILLS = [
    "Python",
    "Django",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Java",
    "Docker",
    "Git",
    "AWS",
    "Machine Learning",
    "Flask",
    "Bootstrap"
]


def extract_skills(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text:

            found_skills.append(skill)

    return found_skills