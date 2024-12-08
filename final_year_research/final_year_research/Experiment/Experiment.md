## Evaluation Metrics
[[Experiment_Design#ChatGPT Generated Questions |Evaluation Metrics]] -> 9 questions

What are we evaluating?

The first response -> the first response that the LLM generates
The chosen response -> the response that the user picks or provides as the best response

The fine tuned response (that is the first response after LLM)

we're only going to present the user with the final model weight after training on 32 n dataset. Otherwise it'll be too much to evaluate in the scope. However, we're still going to measure the times for training each weights at $2^n$ steps. Afterwards, we use that model checkpoint and continue training (sDPO approach)

#### Measuring Times for DPO with QLoRa

Given model A.
GIven configuration X.

for the GPUs, lets use, should also mention RAM and CPU:

1. 8GB -> Nvidea laptop 3070 ti 8gb VRAM (mine) -> 32 gb RAM
2. 15GB -> Google Collab T4GPU  -> thin
3. 24GB -> RTX 3090 Run Pod

gradient has GPUs for use from 8 to 16 gbs, for our purposes. 

Regardless, for each GPU, we train $2^n$ -> $2^i$ where n starts at 1 and ends at 5.

Take for example:

input: non finetuned LLM
n dataset: 2
output: model-2-pairs.pt

Input: model-2.pairs.pt
n dataset: $2^i$ - $2^{i-1}$ (4 - 2 = 2)
output: model-4-pairs.pt

Input: model-4.pairs.pt
n dataset: $2^i$ - $2^{i-1}$ (8 - 4 = 4)
output: model-8-pairs.pt

Input: model-8.pairs.pt
n dataset: $2^i$ - $2^{i-1}$ (16 - 8 = 8)
output: model-16-pairs.pt

Input: model-16.pairs.pt
n dataset: $2^i$ - $2^{i-1}$ (32 - 16 = 8)
output: model-32-pairs.pt

*record times at each step*

Limitations:
- access to perfectly ascending GPUs
- does not consider number of Cuda Cores

# Secondary Measurements
## Measuring RAG Times

Just measure the times for RAG, time taken from input to time taken to find a document

without RAG
also to measure -> infering 


## Measurements

Comparison between the first response and chosen response -> if significant, this shows that the language preferences per user can have some significant effect for the given evaluation metrics

Comparison between the chosen response and the fine tuned response -> if similar, this shows that the DPO algorithm was able to aptly reflect the preferences given the small training set. Furthermore, we can do a qualitative question to affirm this, like how well does the provided response match your chosen response?

n
	prompt:
	chosen: 
	rejected