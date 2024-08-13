from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

def create_vector_db_from_youtube_url(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)
    return FAISS.from_documents(docs, embeddings)

def get_response_from_query(db, query, k=4):
    docs = db.similarity_search(query, k)
    docs_page_content = " ".join([d.page_content for d in docs])
    llm = OpenAI(model="gpt-4o-mini")

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a helpful YouTube assistant that can answer questions about videos based on the video's transcript.
        Answer the following question: {question} 
        By searching the following video transcript: {docs}
        Only use the factual information from the transcript to answer the question.
        If you feel like you don't have enough information to answer the question, say "I don't know".
        Your answers should be detailed.
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(question=query, docs=docs_page_content)
    return response.replace("\n", ""), docs

if __name__ == "__main__":
    video_url = "https://youtu.be/-Osca2Zax4Y?si=iyOiePxzUy_bUayO"
    result = create_vector_db_from_youtube_url(video_url)
    print(result)
