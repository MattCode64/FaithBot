# FAITHBOT

## Description
This is a LLM (Large Language Model) based chatbot that can be used to answer questions about the Christian faith. It is based on the Mistral model. The chatbot is designed to be used in a conversational manner, where the user can ask questions and the chatbot will respond with relevant information. The technology used to build the chatbot is the RAG method (Retrieval-Augmented Generation), which is a combination of a retrieval model and a generative model. The retrieval model is used to find relevant passages from a knowledge base, and the generative model is used to generate responses based on the retrieved passages. It is designed to provide accurate and informative answers to questions about the Christian faith.

## Installation

### Ollama

This bot requires Ollama, an open-source conversational AI platform, to run.
You can install Ollama by following the instructions on the [Ollama GitHub page](https://github.com/ollama/ollama).

### Requirements

This bot is based on LangChain Framework. You can install the requirements by running:

`pip install -r requirements.txt`

## Usage

First, start the Ollama server by running this command in the terminal:

`ollama serve` (keep this terminal open)

Then, in the terminal of your project directory, pull/download the model you want to use:

`ollama pull mistral` or `ollama pull llama2`

Finally, start the chatbot by running:

`ollama run mistral` or `ollama run llama2`

You can now interact with the chatbot by typing in the terminal or RAG your model.

## RAG (Retrieval-Augmented Generation)

RAG stands for Retrieval-Augmented Generation. It's a technique to improve the accuracy of LLM about specific subject. RAG lets them access trustworthy external sources like a giant knowledge base, in our case, the entire Bible.

RAG can for exemple :

- [x] Increase the accuracy of the model for a specific subject
- [x] Reduce hallucination
- [x] Provide dated information
- [x] Less ressource intensive than a full fine-tuning


## Contributing

Me

