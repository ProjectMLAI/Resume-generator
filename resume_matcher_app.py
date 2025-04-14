def generate_tailored_resume(resume_text, job_description):
    prompt = f"""
You are an AI resume assistant. Your task is to improve the following resume so that it aligns with the job description below. 

Make sure:
- It remains ATS-friendly (no images, no tables, only plain text).
- You retain real experiences and only reword where relevant.
- Remove repetition or irrelevant information.
- Emphasize achievements and key skills relevant to the job.

Resume:
{resume_text}

Job Description:
{job_description}

Now provide the improved resume:
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Use gpt-3.5 if gpt-4 gives access issues
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def generate_cover_letter(resume_text, job_description):
    prompt = f"""
Using the following resume and job description, write a professional, personalized cover letter. Keep it concise, engaging, and tailored for the role. Do not invent new degrees or jobs.

Resume:
{resume_text}

Job Description:
{job_description}

Cover Letter:
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # gpt-4 if available and you have access
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
