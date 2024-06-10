import os
import json
import requests

from typing import Optional, Type, Any
from pydantic.v1 import BaseModel, Field
from crewai_tools.tools.base_tool import BaseTool

class SearchApiToolSchema(BaseModel):
	"""Input for SearchApiTool."""
	search_query: str = Field(..., description="Mandatory search query you want to use to search the internet")

class SearchApiTool(BaseTool):
	name: str = "Search the internet"
	description: str = "A tool that can be used to search the internet with a search_query."
	args_schema: Type[BaseModel] = SearchApiToolSchema
	search_url: str = "https://www.searchapi.io/api/v1/search"
	gl: Optional[str] = None
	hl: Optional[str] = None
	location: Optional[str] = None
	num: int = 10

	def _run(
		self,
		**kwargs: Any,
	) -> Any:
		search_query = kwargs.get('search_query')
		if search_query is None:
			search_query = kwargs.get('q')

		params = {
			"q": search_query,
			"engine": "google",
      "gl": self.gl,
      "hl": self.hl,
      "location": self.location,
      "num": self.num,
		}
		headers = {
        'Authorization': f'Bearer {os.environ["SEARCHAPI_API_KEY"]}',
				'content-type': 'application/json'
		}
		response = requests.get(self.search_url, headers=headers, params=params)

		results = response.json()

		summary = ""
		if 'answer_box' in results:
			summary += str({k: v for k, v in results['answer_box'].items() if k != 'thumbnail'}) # Removes thumbnail from answer_box
		elif 'sports_results' in results:
			summary += str(results['sports_results'])
		elif 'knowledge_graph' in results:
			summary += str(results['knowledge_graph'])
		elif 'organic_results' in results:
			filtered_results = [
				{k: v for k, v in result.items() if k not in ['favicon', 'thumbnail']}
				for result in results['organic_results']
			]
			summary += str(filtered_results)
		elif 'top_stories' in results:
			filtered_results = [
					{k: v for k, v in result.items() if k not in ['favicon', 'thumbnail']}
					for result in results['top_stories']
			]
			summary += str(filtered_results)


		return summary
