import asyncio
import json
from functools import lru_cache

from agents import function_tool
from dotenv import load_dotenv
from langchain_community.utilities import SerpAPIWrapper

load_dotenv()


@lru_cache(maxsize=64)
async def search_company_info(company_name: str, query: str) -> str:
    """Perform an async search for a specific company-related query."""
    serp_api = SerpAPIWrapper()
    company_info = await serp_api.arun(f'{company_name} "{query}"')
    return company_info


@function_tool
async def get_company_information(company_name: str) -> str:
    """Look up company background, mission, and core values using SerpAPI."""
    about, mission, values = await asyncio.gather(
        search_company_info(company_name, "about us"),
        search_company_info(company_name, "mission statement"),
        search_company_info(company_name, "core values"),
    )

    result = {
        "company": company_name,
        "about": about.strip(),
        "mission": mission.strip(),
        "values": values.strip(),
    }

    return json.dumps(result, ensure_ascii=False, indent=4)
