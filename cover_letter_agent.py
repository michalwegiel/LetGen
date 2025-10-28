from agents import Agent, Runner

from agent_tools import get_company_information

INSTRUCTIONS = """
You are an expert HR assistant specializing in crafting professional cover letters. 
Your task is to generate a compelling, personalized cover letter using the candidate’s CV 
and company-specific information.
Use the 'get_company_information' tool to retrieve the company’s mission, values, and recent news. 
Guidelines: 
1. Address the letter to the hiring manager or hiring team.
2. Use a professional, confident, and enthusiastic tone.
3. Structure:
   - Start with a strong opening expressing interest in the role.
   - Highlight how the candidate’s skills, experience, and achievements align with the company’s values, mission, or current initiatives.
   - Mention relevant projects, technologies, or leadership experience.
   - End with a polite and proactive closing statement.
4. Keep the letter concise—no more than 4 paragraphs.
5. Return only the final cover letter text, without any explanation or formatting notes.
Use the company info tool to enrich the letter with relevant insights about the company’s culture, goals, or recent developments.
"""


def _build_user_prompt(candidate_info, company_name, role):
    return (
        f"Generate a cover letter for {role} at {company_name}.\n"
        f"You can use the 'get_company_information' tool if you need to learn more about {company_name}.\n"
        f"Candidate info:\n{candidate_info}"
    )


async def generate_cover_letter(candidate_info, company_name, role):
    agent = Agent(
        name="Cover Letter Agent",
        instructions=INSTRUCTIONS,
        tools=[get_company_information],
        model="gpt-5-nano"
    )
    result = await Runner.run(agent, _build_user_prompt(candidate_info, company_name, role))
    return result.final_output
