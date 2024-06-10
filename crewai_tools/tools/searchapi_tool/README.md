# SearchApiTool Documentation

## Description
The SearchApiTool lets you perform a semantic search on text content across the internet using the `searchapi.io` API. It fetches and displays the most relevant search results for a given query.

## Installation
To add this tool to your project, run:
```shell
pip install 'crewai[tools]'
```

## Example
Here's how to initialize and use the tool for a search:

```python
from crewai_tools import SearchApiTool

# Initialize the tool
tool = SearchApiTool()
```

## Steps to Get Started
To use the `SearchApiTool`, follow these steps:

1. **Install the Package**: Ensure the `crewai[tools]` package is installed in your Python environment.
2. **Get an API Key**: Sign up for a free account at [SearchApi.io](https://www.searchapi.io/) to get your API key.
3. **Set Up the Environment**: Store your API key in an environment variable named `SEARCHAPI_API_KEY`.

## Conclusion
The SearchApiTool allows you to perform real-time, relevant searches on the internet directly from your applications. Follow the setup and usage instructions to easily integrate this tool into your projects.
