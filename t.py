# chatbot_core.py

import os
from langchain_huggingface import HuggingFaceEmbeddings,HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
import warnings
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Désactiver les avertissements spécifiques au tokenizer
warnings.filterwarnings("ignore", message=".*clean_up_tokenization_spaces*")

HF_TOKEN = os.getenv('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')
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Initialisation des embeddings et de la base de données vectorielle
embeddings = HuggingFaceEmbeddings(model_name="hkunlp/instructor-xl")
vectorstore = FAISS.load_local('faiss_index', embeddings=embeddings, allow_dangerous_deserialization=True)

# Configuration du modèle LLM
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0.1,
    model_kwargs={"max_length": 150},
    huggingfacehub_api_token='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'
)
# Initialisation de la mémoire pour stocker l'historique des conversations
memory = ConversationBufferMemory(
    k=3,
    memory_key='chat_history',
    return_messages=True
)

# Initialisation de la chaîne de récupération conversationnelle avec mémoire
conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type='map_reduce',
    retriever=vectorstore.as_retriever(), 
    return_source_documents=True,
    memory=memory,
)

# Modèle de prompt pour le chatbot
template = """
Vous êtes un chatbot spécialisé dans le code du travail au Maroc.
Utilisez le contexte fourni pour répondre à la question de l'utilisateur concernant les lois du travail marocaines.
Faites en sorte que votre réponse soit courte, précise et utile.
Si vous ne trouvez pas la réponse pertinente dans le contexte fourni, répondez simplement que vous ne savez pas.
Contexte: {context}
Historique: {chat_history}
Question: {question}
Réponse:
"""

prompt = PromptTemplate(template=template, input_variables=["context", "chat_history", "question"])

# Chaîne LLM qui intègre le contexte et l'historique de chat
llm_chain = RunnableSequence(prompt | llm)

# Fonction pour gérer les questions, récupérer le contexte et générer des réponses
def answer_question(question):
    # Récupérer le contexte depuis la base de données vectorielle
    docs = conversation_chain.retriever.invoke(question)
    context = " ".join([doc.page_content for doc in docs])

    # Générer la réponse en utilisant le contexte et l'historique de chat
    answer = llm_chain.invoke({
        "context": context,
        "chat_history": memory.load_memory_variables({})['chat_history'],
        "question": question
    })
    
    # Sauvegarder la question et la réponse dans la mémoire
    memory.save_context({"input": question}, {"output": answer})
    
    return answer

