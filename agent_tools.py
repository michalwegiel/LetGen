from agents import function_tool
from dotenv import load_dotenv
from langchain_community.utilities import SerpAPIWrapper

load_dotenv()


@function_tool
def get_company_information(company_name: str) -> str:
    """Look up company mission and values using SerpAPI."""
    serp_api = SerpAPIWrapper()
    company_info = serp_api.run(f'"{company_name}" "about us" "mission statement" "core values"')
    return company_info
