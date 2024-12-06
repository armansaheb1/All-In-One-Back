from main import models
import os
import json
import time
import requests
from openai import OpenAI
from langchain_community.document_loaders import AsyncHtmlLoader, RSSFeedLoader
from django.core.management.base import BaseCommand
from llama_index.core import (
    SimpleDirectoryReader,
    GPTVectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.core import Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from Analyzer import settings
import nltk
import newspaper
import lxml


# nltk.download('punkt_tab')
def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats:
        return True
    return False


os.environ["OPENAI_API_KEY"] = settings.OPEN_AI_KEY

gpt_client = OpenAI(api_key=settings.OPEN_AI_KEY)

client = OpenAI(api_key=settings.OPEN_AI_KEY)


def get_news_gpt():
    Settings.llm = OpenAI(model="gpt-4o")
    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
    Settings.num_output = 512
    Settings.context_window = 3900
    Settings.chunk_size = 2048
    for itemmm in models.NewsSite.objects.all().order_by("id"):
        documents = str(RSSFeedLoader(urls=[itemmm.url]).load())
        # print(documents)
        with open("/Analyzer/input/copy.txt", "r+") as f:
            f.write(documents)
            f.truncate()
        documents = SimpleDirectoryReader("/Analyzer/input").load_data()
        index = GPTVectorStoreIndex.from_documents(documents)

        index.storage_context.persist(persist_dir="/Analyzer/done")

    for item in models.NewsIntrest.objects.all():
        # print(item.subject)
        prompt = f"Retrieve data related to {item.subject}  as a JSON list. Each item should be a dictionary containing relevant fields, such as 'title', 'description'. Return only the JSON array with no additional text or formatting."
        # prompt = "Retrieve the news articles in JSON format. Each entry should be a dictionary containing 'pic','description' and 'title' as keys. Return only the JSON array with no additional text or formatting."
        # prompt = f"a list of full news related to {item.subject} from context with pic,description and title  as only a json with data field with a list of dics"
        storage_context = StorageContext.from_defaults(persist_dir="/Analyzer/done")
        index = load_index_from_storage(storage_context)
        response = index.as_query_engine().query(prompt)

        response = response.response

        # print(response)

        response = response.replace("```json", "").replace("```", "")
        # print(response)
        response = json.loads(response)
        for itemm in response:
            # print(itemm)
            if "title" in itemm and "description" in itemm:
                if len(itemm["description"]):
                    if not len(
                        models.NewsReport.objects.filter(
                            title=itemm["title"], user=item.user
                        )
                    ):

                        models.NewsReport.objects.create(
                            user=item.user,
                            title=itemm["title"],
                            text=itemm["description"],
                            subject=item.subject,
                            resource=itemmm.name,
                        )


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_news_gpt()
