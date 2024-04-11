from langchain.evaluation import load_evaluator
from langchain.evaluation.schema import EvaluatorType
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings


def main():
    print(f"Starting {main.__name__}")

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    embeddings = HuggingFaceEmbeddings(model_name=model_name,
                                       model_kwargs=model_kwargs,
                                       encode_kwargs=encode_kwargs)
    vector = embeddings.embed_query("door")
    # print(f"Vector for 'door': {vector}")
    print(f"Vector length: {len(vector)}")

    evaluator = load_evaluator(EvaluatorType.EMBEDDING_DISTANCE, embeddings=embeddings)
    words = ["line", "window", "car", "house", "dog", "cat", "horse", "poney", "keyboard", "read", "write", "book",
             "iphone", "spirit", "living", "aqua", "Orlando", "Paris"]
    print(type(words))

    # Dictionary of words and their scores
    scores = {}
    for i in range(len(words)):
        for j in range(len(words)):
            x = evaluator.evaluate_strings(prediction=words[i], reference=words[j])
            scores[f"{words[i]}-{words[j]}"] = x.get('score')

    # Print the highest and lowest scores
    print(f"Minimum : {min(scores.values())}")
    print(f"Maximum : {max(scores.values())}")


if __name__ == '__main__':
    main()
