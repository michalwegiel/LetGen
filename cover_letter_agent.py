from agents import Agent, Runner, trace
from dotenv import load_dotenv

from agent_tools import get_company_information
from candidate_info_agent import extract_candidate_data

load_dotenv()


INSTRUCTIONS = """
You are an expert HR assistant specializing in crafting professional cover letters. 
Your task is to generate a compelling, personalized cover letter using the candidate’s structured data 
and company-specific information.

Use the 'get_company_information' tool to retrieve the company’s mission, values, and recent news. 

Guidelines: 
1. Address the letter to the hiring manager or hiring team.
2. Use a professional, confident, and enthusiastic tone.
3. Structure:
   - Strong opening expressing interest in the role.
   - Highlight how the candidate’s skills, experience, and achievements align with the company’s mission or initiatives.
   - Mention relevant projects, technologies, or leadership experience.
   - End with a polite, proactive closing.
4. Keep it concise (max 4 paragraphs).
5. Return only the final cover letter text — no explanations or markdown.
"""


def _build_user_prompt(candidate_info, company_name, role):
    return (
        f"Generate a cover letter for {role} at {company_name}.\n"
        f"You can use the 'get_company_information' tool if you need to learn more about {company_name}.\n"
        f"Candidate info:\n{candidate_info}"
    )


async def generate_cover_letter(candidate, company_name, role):
    agent = Agent(
        name="Cover Letter Agent",
        instructions=INSTRUCTIONS,
        tools=[get_company_information],
        model="gpt-5-nano"
    )
    result = await Runner.run(agent, _build_user_prompt(candidate.json(), company_name, role))
    return result.final_output


async def generate_cover_letter_from_documents(cv_text: str, company_name: str, role: str, additional_docs: list[str] | None = None):
    with trace("LetGen"):
        candidate = await extract_candidate_data(cv_text, additional_docs)
        cover_letter = await generate_cover_letter(candidate, company_name, role)

    print(candidate)
    return cover_letter
