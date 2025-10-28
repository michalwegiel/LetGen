from agents import function_tool
from langchain_community.utilities import SerpAPIWrapper


@function_tool
def get_company_information(company_name: str) -> str:
    """Look up company mission, values, and news using SerpAPI."""
    serp_api = SerpAPIWrapper()
    company_info = serp_api.run(f'"{company_name}" "about us" "mission statement" "core values" "latest press release"')
    return company_info
