from typing import Dict, Any
from pathlib import Path


class ResponseFormatter:
    """Formats responses with source citations."""

    @staticmethod
    def format_answer_with_sources(
        result: Dict[str, Any],
        max_source_length: int = 300
    ) -> str:
        """Format answer with source document citations"""
        answer = result.get('answer', 'No answer provided')
        sources = result.get('source_documents', [])

        if not sources:
            return answer

        formatted_response = answer + "\n\n" + "="*50 + "\nSOURCES:\n" + "="*50

        for i, doc in enumerate(sources, 1):
            source_path = doc.metadata.get('source', 'Unknown source')
            source_page = doc.metadata.get('page', 'Unknown page')

            formatted_response += f"\n\nSource {i}: {Path(source_path).name} (Page: {source_page})"
            formatted_response += f"\n{doc.page_content[:max_source_length]}..."

        return formatted_response
