from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI


class QAChainBuilder:
    """Builds and manages the conversational QA chain."""

    def __init__(
        self,
        temperature: float = 0,
        model_name: str = "gpt-4o-mini"
    ):
        self.temperature = temperature
        self.model_name = model_name

    def build_chain(self, retriever) -> ConversationalRetrievalChain:
        """Build conversational retrieval chain"""
        llm = ChatOpenAI(
            temperature=self.temperature,
            model_name=self.model_name)

        return ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            return_source_documents=True,
            verbose=True
        )
