I'm not aiming to build a fully functional ITS or even a ITS at all.

In effect, I am trying to see if the DPO algorithm under the given constraints can produce noticable criteria.

For arguments sake, let's say the criteria are:

Clarity -> how clear are the explanations? 

Understanding -> how well do you understand the explanations

Sensical -> does the answer make sense?

Relevancy -> how relevant is the answer?

Then we can compute the score a average score like:

clarity = 4/5
understanding = 3/5
sensical = 5/5
relevancy = 4/5

4 + 3 + 5 + 4 = 0.8

With this, i'm gonna have to clearly define what each attribute means and justify it...

Writeup about evaluating LLM responses: https://cohere.com/llmu/evaluating-llm-outputs

Alternative i can just have the user rate the response from 1 - 10. 

## Generating Alternate Responses

How do I go about generating alternate responses? 

#### Option 1

I simply prompt the LLM with the same prompts and I let the LLM generate new responses each time. The responses should be slightly different due to a LLMs probabalistic outcomes

From the list, the users will pick a chosen and Ig a rejected or maybe many rejected but that would increase our training pairs where we would have:

```
pair
	chosen: r1
	rejected: r2
pair
	chosen: r1
	rejected: r2
```

so instead let's just have them pick the most preferred one and the lest preferred one out of the list of n generated responses.
#### Option 2

I prompt the LLM to responsd different each time.

Examples

```
1. Respond concisely and to the point
2. Response with great detail and explanations
3. Respond using many examples 
4. Respond assertively and xyz
5. Respond whatever
```

Therefore with let's say teacher prompt, the response should change...however, that likely biases the experiment. If the prompts change. Hmm instead we should just have 2 categories? 

I don't think I'll go with this since it has a lot of variability factors involved
#### Option 3

We let the users edit and create their own ideal responses.

#### Option 4

Option 1 for most but Option 3 for like 1 so that we can have a ideal answer. Why do we want an ideal 1?

## ChatGPT Generated Questions
#### Relevance
- **Question**: "How well does the response address your query or the topic at hand?"
- **Scale**: 1 (Irrelevant) to 5 (Highly Relevant)
#### Clarity
- **Question**: "Is the response easy to understand and clearly written?"
- **Scale**: 1 (Confusing) to 5 (Crystal Clear)
#### Usefulness
- **Question**: "How helpful or actionable do you find the response?"
- **Scale**: 1 (Not Helpful) to 5 (Very Helpful)
#### Completeness
- **Question**: "Does the response provide enough information, or is it missing key details?"
- **Scale**: 1 (Incomplete) to 5 (Thorough and Comprehensive)
#### Engagement
- **Question**: "Did the response engage you or feel interactive?"
- **Scale**: 1 (Unengaging) to 5 (Highly Engaging)
#### Naturalness
- **Question**: "Does the response sound natural, like it was written by a human?"
- **Scale**: 1 (Robotic/Unnatural) to 5 (Human-like and Conversational)
#### Conciseness
- **Question**: "Is the response appropriately concise or to the point?"
- **Scale**: 1 (Too Wordy/Too Short) to 5 (Perfectly Balanced)
#### Personalization
- **Question**: "Does the response feel tailored to your needs or context?"
- **Scale**: 1 (Generic) to 5 (Highly Personalized)


