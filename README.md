# Chain of Verification Agent

Codebase Owner: Enes Özeren

## Problem Analsyis

### Problem:
A RAG system generates hallucinated summaries given retrieved customer review data.

### Assumptions
The retrieved customer review data and a hallucinated summary output from the RAG system is available

### Proposed Solution
Deploy another LLM agent into the loop which will ask questions about the summary of the RAG system. Then the RAG system focuses on answering those questions from the data. This can help the RAG system to realize the hallucinations and adjust the summary.

## Methodology
This codebase implements an Agent designed for integration into a Retrieval-Augmented Generation (RAG) system. Its primary function is to ask verification questions about the generated answers, enhancing their accuracy by preventing hallucination.

This implementation is inspired from CoVe (Dhuliawala et al., 2023) method. While CoVe method is mainly build for non-RAG systems, this codebase adapts it to be relevant in RAG systems with some tweaks.

### Steps of the Proposed Method
Terminology:

- RetrieverAgent: Retrieves the customer review data with respect to user query (Not available in this case study)
- ChatAgent: Generates summary by looking at the retrieved customer review data.
- CoveAgent: Asks questions about the generated summary by the ChatAgent.

Steps:

0) A summary written by ChatAgent is available.
1) CoveAgent will ask questions about the summary of the ChatAgent without seeing the customer review data.
2) The ChatAgent will generate answers to the questions asked by CoveAgent by looking at the customer review data.
3) The ChatAgent will generate a new summary based on the initial/hallucinated summary, verification answers, and the customer review data.


### References:
- Dhuliawala, S., Komeili, M., Xu, J., Raileanu, R., Li, X., Celikyilmaz, A., & Weston, J. (2023). Chain-of-verification reduces hallucination in large language models. arXiv preprint arXiv:2309.11495.

## Instructions for usage:

Please create a conda environment with python 3.12.8 and then install the `requirements.txt` with.
```bash
pip install -r requirements.txt
```

Also create an `.env` file and store your Openai API key in `OPENAI_API_KEY` variable

Then you can run the following script for a RAG with CoVe Agent demo. This script will create a `demo_data/outputs.txt` file which contains the outputs generated from ChatAgent and CoveAgent.
```bash
python run_rag_system.py
```

You can also check the existing `demo_data/outputs.txt` file if there are no OpenAI API tokens available for you.

## Folder structure:
```
.
├── README.md                       
├── demo_data                                   <- contains dummy customer reviews and a hallucinated answer
├── cove_rag                                    <- contains the agent class descriptions
├── run_rag_system.txt                          <- scripts to run the demo with the dummy demo data
├── requirements.txt                            <- python package requirements
└── .gitignore                                  <- git ignored files
```

## Further Comments

Since this is a prototype prepared in a couple of hours, OpenAI APIs are utilized. However, to protect customer data, these APIs can be simply replaced with a couple of lines to use open-sourced LLM models from huggingface transformers package.
