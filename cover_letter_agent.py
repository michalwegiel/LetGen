from typing import Literal

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
   - Signature.
4. Keep it concise (max 4 paragraphs).
5. Use Latin characters.
6. Return only the final cover letter text — no explanations or markdown.
"""


def _build_user_prompt(candidate_info, company_name, role, tone, length):
    return (
        f"Generate a {tone} cover letter for {role} at {company_name}.\n"
        f"The letter should be {length} in length.\n"
        f"You can use the 'get_company_information' tool if you need to learn more about {company_name}.\n"
        f"Candidate details:\n{candidate_info}"
    )


async def generate_cover_letter(candidate, company_name, role, tone, length):
    agent = Agent(
        name="Cover Letter Agent", instructions=INSTRUCTIONS, tools=[get_company_information], model="gpt-5-nano"
    )
    result = await Runner.run(agent, _build_user_prompt(candidate.json(), company_name, role, tone, length))
    return result.final_output


async def generate_cover_letter_from_documents(
    cv_text: str,
    company_name: str,
    role: str,
    additional_docs: list[str] | None = None,
    tone: Literal["Professional", "Confident", "Friendly", "Enthusiastic"] | None = "Professional",
    length: (
        Literal["Short (~180–250 words)", "Medium (~250–350 words)", "Long (~350–500 words)"] | None
    ) = "Medium (~250–350 words)",
):
    with trace("LetGen"):
        candidate = await extract_candidate_data(cv_text, additional_docs)
        cover_letter = await generate_cover_letter(candidate, company_name, role, tone, length)

    return cover_letter
