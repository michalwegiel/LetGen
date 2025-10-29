from typing import List, Optional

from agents import Agent, Runner
from pydantic import BaseModel, Field


class Candidate(BaseModel):
    name: Optional[str] = Field(None, description="Full name of the candidate")
    title: Optional[str] = Field(None, description="Current or desired professional title")
    years_experience: Optional[int] = Field(None, description="Approximate years of professional experience")
    technologies: List[str] = Field(
        default_factory=list, description="List of known technologies or programming languages"
    )
    tools: List[str] = Field(
        default_factory=list, description="List of tools, frameworks, or platforms the candidate has used"
    )
    education: Optional[str] = Field(None, description="Highest relevant degree or education summary")
    experience_summary: Optional[str] = Field(None, description="Concise summary of career experience and achievements")
    certifications: List[str] = Field(default_factory=list, description="Relevant certifications, if any")
    languages: List[str] = Field(default_factory=list, description="Languages spoken or written")
    achievements: List[str] = Field(default_factory=list, description="Key achievements worth highlighting")


INSTRUCTIONS = """
You are an expert HR data analyst specialized in reading candidate CVs and extracting structured information.
You will receive the content of one or more documents (CVs, portfolios, certificates, etc.).
Your task:
1. Carefully read the text.
2. Identify the candidate’s:
   - Full name
   - Current title or role
   - Years of experience
   - Technologies, tools, and frameworks mentioned
   - Education
   - Notable experience summary
   - Certifications
   - Languages
   - Key achievements or recognitions
3. Return your answer strictly as a JSON object matching the Candidate schema.
4. Do NOT include explanations, markdown formatting, or text outside the JSON.
"""


async def extract_candidate_data(cv_text: str, additional_docs: list[str] | None = None):
    combined_input = [cv_text]
    if additional_docs:
        combined_input.append("Additional Documents:")
        combined_input.extend(additional_docs)
    combined_input = "\n\n".join(combined_input)

    agent = Agent(
        name="Candidate Extraction Agent", instructions=INSTRUCTIONS, model="gpt-5-nano", output_type=Candidate
    )

    result = await Runner.run(agent, combined_input)
    return result.final_output
