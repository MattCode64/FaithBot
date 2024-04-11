# FAITHBOT

## Description
This is a LLM (Large Language Model) based chatbot that can be used to answer questions about the Christian faith. It is based on the Mistral model. The chatbot is designed to be used in a conversational manner, where the user can ask questions and the chatbot will respond with relevant information. The technology used to build the chatbot is the RAG method (Retrieval-Augmented Generation), which is a combination of a retrieval model and a generative model. The retrieval model is used to find relevant passages from a knowledge base, and the generative model is used to generate responses based on the retrieved passages. It is designed to provide accurate and informative answers to questions about the Christian History.

## Installation

### Ollama

This bot requires Ollama, an open-source conversational AI platform, to run.
You can install Ollama by following the instructions on the [Ollama GitHub page](https://github.com/ollama/ollama).

### Requirements

This bot is based on LangChain Framework. You can install the requirements by running:

`pip install -r requirements.txt`

## Usage

- First, start the Ollama server by running this command in the terminal:

`ollama serve` (keep this terminal open)

- Then, in the terminal of your project directory, pull/download the model you want to use:

`ollama pull mistral` or `ollama pull llama2`

- Finally, start the chatbot by running:

`ollama run mistral` or `ollama run llama2`

#### You can now interact with the chatbot by typing in the terminal or RAG your model.

## RAG (Retrieval-Augmented Generation)

RAG stands for Retrieval-Augmented Generation. It's a technique to improve the accuracy of LLM about specific subject. RAG lets them access trustworthy external sources like a giant knowledge base, in our case, the entire Bible.

RAG can for exemple :

- [x] Increase the accuracy of the model for a specific subject
- [x] Reduce hallucination
- [x] Provide dated information
- [x] Less ressource intensive than a full fine-tuning

### How it works

To integrate RAG into a LLM, we need to follow important steps :

#### 1. Get data

First, we need to get a dataset about the subject we want to improve the model on. In our case, we used the Bible in this project to improve the model on the Christian faith. (but you can use any dataset you want like a book, documentations, etc.)

#### 2. Load documents

We need to load the documents into the model to make it accessible. In this project, I used the loader from LangChain Framework to load my documents.
Loading documents is a simple process, you just need to provide the path to the documents.


#### 3. Split documents

In the case that you have long and complex documents, you can split them into smaller parts to make it easier for the model to find the right information. LangChain Framework provides a splitter to split the documents into smaller parts with specific parameters.
We can adjust the chunk size and the overlap and there are the effects of the splitting :

- **Chunk_size** : Bigger chunks can provide more context and manage more information but require more memory. It can help the model to increase coherence and reduce hallucination when the documents are several links between them.
- **Overlap** : Bigger overlap means that each chunk will have more context from the previous chunk. It helps to link the chunks together. But it can also increase the redundancy of the information.

#### 4. Embed documents

This is the most important step in configuring RAG. We need to embed the documents into the model to make them accessible, readable and searchable. Embedding documents is a process that converts the documents into vectors that the model can understand. In this project, I used a very popular embedding model called "all-MiniLM-L6-v2" by Sentence-Transformers. It's very efficient and provides good results.


#### 5. Store documents in a Vector Storage

ChromaDB is the vector storage I choose to use. 

#### 6. Retrieve

I have defined a prompt template to format the retrieve query. The model will use this template to search for the most relevant documents to the user's question. The model will retrieve the most relevant documents from the vector storage, using the same embedding model as the one used to embed the documents.

#### 7. Generate

Choose the LLM model, ask the model to generate a response based on the retrieved documents and... Voilà!

## Contributing

Me

