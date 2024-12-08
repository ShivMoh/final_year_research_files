I assume that personalising the way explanations are offered, will result in a positive correlation of said scores.

non-personalised text -> 8/10
personalised text - 10/10

However, is that a baseless assumption? Do i need to try and find evidence to back that up. I think so yh

If I do, then my research is is simply about checking if my algorithm is capable of doing that.

Alternatively my research will be

Does finetuning on n dataset produce any noticable learning outcomes

Basically i have baseline evaluated score -> 8/10

And then I have a score for DPO personalised text -> 9 / 10.

Issues:

This does not differentiate whether the algorithm worked or not. Or if its simply the case that changing the response did not have a effect on the person.

How to control?

Simple, if the algorithm worked -> then we simply compare the difference in response for x and y. We store the response and just compare since questions will be the same.

If its different, the algorithm worked -> I think that I'll have a similarity score to compare the previous text for the new text and use that.
So like i can say, the output changed 80% from what it did before. Ideally, i could get a ideal response from the user and see how that compares, but that assumes fimiliarity with the content. Maybe I can just have 1 or 2 for that. Like I have one simply question. "What is an operating system" and I have the users provide a response that would be ideal. So then if I ask for that specific question, the algorithm should produce a high similarity score with that ideal response for its outputted response.

However, if its different and the scores do not change, then no noticable learning outcomes were produced.

If it is not significantly different and scores do not change -> then we cannot conclude if it language had an impact or not

To test if the algorithm worked

``` python
finetuned_llm = llm()
text_similarity = cossinsim()

for user of users:
	for i, question in enumerate(questions):
		for chosen in user.chosen[i]:
			response = finetuned_llm.query(question)				
			score = cossinsim().compare(response, chosen)
			print(score)
```

If the algorithm worked, then what we expect is a fairly high similarity score between the generated response and the chosen answer.

**I think I prefer the below, tho it would require more from the user:**

Alternative, we make the users rate the chosen answers in terms of the same metrics. Effectively, we then have the user score for the baseline and the user score for the chosen and afterwards, we'll have a baseline for the finetuned one. If the algorithm works, then what that means is that the scores for the chosen would be similar to the scores for the non chosen.

Ideally, I would then be able to effectively move foward with that idea and test how it impact learner outcomes through some sort of test. Maybe a simple memory test, asking the users the same set of questions that it asked the LLM and we have them reply. Problem with that is that ofc, people can cheat as they definitely do in exams, also its tedious.

**So a major limitation** is that so far, the results will depend on user reported data. We're acc having them do a test afterwards or anything like that. If they say the personalised text improves the clarity and understanding or whatever, we believe them and that's that.

## Outcomes
p = the algorithm worked q = the scores changed
~p = the algorithm did not work q = the scores did not change

p + q = the algorithm worked and the scores changed 
- conclusion: the algorithm is capable of learning for n interaction pairs and that is reflected positively in the changed scores.
p + ~q = the algorithm worked but the scores did not change
- conclusion: the algorithm is capable of showing noticable impacts of n interaction pairs but this does not seem to significantly impact the user's socres
~p + q = the algorithm did not work but the scores did change (don't know what to conclude there. in consistent users ig)
~p + ~q = the algorithm did not work and the scores did not change
- conclusion: nothing worked, ggs

