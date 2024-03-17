import pandas as pd
import os
import os.path as osp
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from dotenv import load_dotenv, find_dotenv
import openai
print(f'load key from {find_dotenv()}')
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.getenv('OPENAI_API_KEY')

###### data
file_path = osp.join('data', 'vec.xlsx')
print(f'load data in {file_path}')
excel_file = pd.ExcelFile(file_path)
bird2data = {}  # map bird_name 2 its data(interpret_2_content)

sheet_name2bird = {'Sheet1': '伏特加', 'Sheet2': '朗姆酒'}
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    attribute = df['二级维度'].tolist()
    attribute_interpretations = df['解释'].tolist()
    attribute_content = df['内容'].tolist()
    interpret_2_content = dict(zip(attribute_interpretations, attribute_content))

    bird_name = sheet_name2bird[sheet_name]
    bird2data[bird_name] = interpret_2_content
# print(bird2data)


###### load demo data into faiss
# file_path = osp.join("data", "西洋.txt")
# loader = TextLoader(file_path, encoding='gbk')
# documents = loader.load()
# print(type(documents[0]))  # <class 'langchain.schema.document.Document'>
# text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
# texts = text_splitter.split_documents(documents)
# print(type(texts[0])) # <class 'langchain.schema.document.Document'>
texts = [Document(page_content=interpret, metadata = {"source": file_path}) for interpret in bird2data['朗姆酒'].keys()]
embeddings = OpenAIEmbeddings()  # text-embedding-ada-002
db = FAISS.from_documents(texts, embeddings)  # texts是values，用embedding来encode texts得到嵌入，进而之后用于索引

query = "途中左侧的朗姆酒好喝，这个朗姆酒的俗名是？" # target interpret: '百加得朗姆酒的的俗称'
docs = db.similarity_search(query)  # 从db索引出的docs is like a list like sorted(texts, reverse=True)



most_similar_interpret = Document(page_content=docs[0].page_content, metadata = {"source": file_path})
cor_content = bird2data['北美红雀'][most_similar_interpret.page_content]
print('query: ', query)
print('most related keys: ', most_similar_interpret.page_content)
print('answer: ', cor_content)

docsearch = Chroma.from_documents(search_texts, embeddings, metadatas=[
    {"source": str(i)} for i in range(len(search_texts))])

llm = OpenAI(temperature=0)

retriever = docsearch.as_retriever()
retriever.search_kwargs['distance_metric'] = 'cos'
retriever.search_kwargs['fetch_k'] = 100
retriever.search_kwargs['maximal_marginal_relevance'] = True
retriever.search_kwargs['k'] = 10

chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm, chain_type="stuff", retriever=retriever)
result = chain({"question": query}, return_only_outputs=False)
chat_history = []
chat_history.append((query, result['answer']))
print(f"答复: {result['answer']} \\n")