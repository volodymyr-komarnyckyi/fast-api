from dotenv import load_dotenv
from elasticsearch.exceptions import NotFoundError
from elasticsearch import Elasticsearch
import os

load_dotenv()

INDEX_NAME = "cve-index"
ES_URL = os.getenv("ES_URL")
ES_API_KEY = os.getenv("ES_API_KEY")

es = Elasticsearch(
    ES_URL,
    api_key=ES_API_KEY
)


def init_db(data):
    try:
        # Create index if it doesn't exist
        if not es.indices.exists(index=INDEX_NAME):
            es.indices.create(
                index=INDEX_NAME,
                body={
                    "settings": {"number_of_shards": 1, "number_of_replicas": 0},
                    "mappings": {
                        "properties": {
                            "cveID": {"type": "keyword"},
                            "vendorProject": {"type": "text"},
                            "product": {"type": "text"},
                            "vulnerabilityName": {"type": "text"},
                            "dateAdded": {"type": "date"},
                            "shortDescription": {"type": "text"},
                            "requiredAction": {"type": "text"},
                            "dueDate": {"type": "date"},
                            "knownRansomwareCampaignUse": {"type": "keyword"},
                            "notes": {"type": "text"},
                            "cwes": {"type": "keyword"},
                        }
                    },
                },
            )
        # Add documents to db
        for cve in data:
            es.index(index=INDEX_NAME, document=cve)
    except Exception as e:
        raise RuntimeError(f"Error initializing the database: {e}")


def get_all_cve():
    try:
        result = es.search(index=INDEX_NAME, body={"query": {"match_all": {}}})
        return result["hits"]["hits"]
    except NotFoundError:
        return []


def search_cve(query: str):
    try:
        result = es.search(
            index=INDEX_NAME,
            body={
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": ["shortDescription", "vulnerabilityName"]
                    }
                }
            }
        )
        return result["hits"]["hits"]
    except NotFoundError:
        return []


def get_known_ransomware_cve():
    try:
        result = es.search(
            index=INDEX_NAME,
            body={
                "query": {
                    "match": {"knownRansomwareCampaignUse": "Known"}
                }
            }
        )
        return result["hits"]["hits"]
    except NotFoundError:
        return []


def get_new_cve(limit: int = 10):
    try:
        result = es.search(
            index=INDEX_NAME,
            body={
                "query": {"match_all": {}},
                "sort": [{"dateAdded": {"order": "desc"}}],
                "size": limit,
            },
        )
        return result["hits"]["hits"]
    except NotFoundError:
        return []
