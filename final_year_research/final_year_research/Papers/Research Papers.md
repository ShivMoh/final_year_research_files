## Large Language Models For Robotics (2023)

Essentially provides a overview of the state of LLMs use and potential uses in robotics. Ideas that stand out are the use of LLMs for personalized adaptability and LLMs for emotional responsiveness. Another interesting thing in brought up is the deployment issue whereby it introduced the two brain approach whereby a smaller model runs locally on the robot's hardware and a more powerful AI runs in the cloud.

In my case, I think I would rather have the option to run a more powerful AI locally on my computer rather than having to connect it to cloud. 

https://arxiv.org/pdf/2311.07226

## Affective Personalization of a Social Robot Tutor for Children's  Second Language Skills (2016)

The research involved the creation of a robot enabled with vision and language inputs paired with a game designed for learning spanish. There was the robot and the 'tucan'. The robot served as a encouraging tutor while the tucan served as an informative third party speaker. 

The experiment effectively utilized a reinforcement learning algorithm (I believe Q Learning) that learned the children's behaviours and updated itself accordingly. The research found that the children's learning improved as the learning became more personalized.

Critique: could it be that the learning simply improved because the children had more overall time with the platform and learning spanish as a whole. Over time, concepts could be more likely to be caught by kids.

Terms Introduced.

- Intelligent Tutoring Systems
- Valence 
- Affect Aware Tutors

https://cdn.aaai.org/ojs/9914/9914-13-13442-1-2-20201228.pdf

## Personalizing Robot Tutors to Individual's Learning Differences (2014)

This researched the role and effect of personalization for robot tutors on student learning. It concluded that personalized tutors resulted in a one sigma improvement over non personalized learning. 

Most participants were graduate and undergraduate students of Yale University with little to no knowledge of robotics and artificial intelligence.

Terms Introduced:
- Bloom's two sigma
- bayesian network
- nonograms (just a type of puzzle, not really relevant)

Robots:
- Hugging robot
- Snackbot
- Keepon

https://www.researchgate.net/publication/262405053_Personalizing_robot_tutors_to_individuals'_learning_differences

## Affective Social Robots (2007)

Essentially about the need for better and more adaptive robots in terms of displaying emotional states.

- Of importance are emotions, moods and attitudes - suggested by Schere
- Focus on long term relationships rather than short term
- **Utilized categorical model of emotions rather than a mapping between a continuous multidimensional space and the robot's expression**
- **Could not find psychological evidence for a computational model of fimiliarity**
- Interestly, a conclusion was made that different levels of fimiliarity with the robot react to the robot's mood in different ways which shows that a social robot needs to remember people who have interacted with it.

https://www.ri.cmu.edu/pub_files/2010/3/Kirby10Affective.pdf
#### Terms Introduced

- Embodied Conversational Agents (ECAs)
- TAME architecture: traits, attitudes, moods and emotions
- Affect: a general term relating to emotions, moods and other such states with varying degrees of positivity or negativity - that is states with valence. [[#Affective Personalization of a Social Robot Tutor for Children's Second Language Skills]]
#### Robots
- Kismet
- Vikia
- Affective Reasoner
- FearNot!

## A MultiModal Social Robot Toward Personalized Emotion Interaction (2021)

- Makes a statement "...robots can also imporve the user's engagement in the long term interaction through personalized interaction policy" -> (Leite, Martinho, and Paiva 2013)
- feature-level fusion, decision level fusion and model level fusion. 
- Policy Optimization Algorithm
- Kullback Leibler divergence penalty
- Negative Attitudes towards Robots Scale (NARS)
- Notably the use for this would be to provide personalized intevention for adolescents with Autism Spectrum Disorder (ASD)

It also shared its hypothesis " Our hypothesis is that multimodal social cues can
give the robot a better ability to understand human emo-
tional states and enhance interactive behaviors."


#### Robots
Pepper Robot: SoftBank robotics group

![[Pasted image 20240909223117.png]]

## Computational Rationality as a Theory of Interaction (2022)

Overall i don't think this is too relevant to what i want.

Talks about the theory of computational rationality which i believe aims to study user specific interaction preferences with computers. Interestingly it introduced some further research areas:

- Adaption to memory limits
- Adaption to perceptual bounds
- Adaption to motor bounds
- Adaptation to the environments

It also has a list of theoritical commitments for building a RL agent:

- An agent solves bounded optimality problems defined by its internal environment
- The internal environment represents mental states and imposes individually determined bounds on adaptation
- The internal environmen includes not only a device design but also its spatially and temporally extended context of use (ecology)
- Interaction between internal and external environments itself a source of bounds on adaptation
- Human perferences and goals are represented with subjective reward function that takes as input the internal state of the agent

Terms:

- Partially Observable Markov decision processes (POMDPs)
- EPIC
- ACT-R
## A Systematic Review of Human and Robot Personality in Health Care Human-Robot Interaction (2021)

Just a literature review of research relevant to personality in health care robots. Nothing really stands out for relevant for me. Other than maybe the five big personality traits: extroversion, agreeableness, conscientiousness, neuroticism and openness to experience.

## Excercize Robots are Perceived as more Competent and Trustworthy

Essentially concluded that the greater the level of automation for a system's adaptability, the better the user's rating of competence, warmt and alliance. 

The study evaluated and compared two methods of personalization for a excercise robot: a method whereby users chose what excercises to do (user controlled personalization) and a method whereby the robot adapted itself to the users via RL learning.

Ultimately, the method whereby the robot adapted itself via RL learning was deemed the prefered method of personalization showing the LOA (levels of automation) of personalization increases users likability and acceptance.

Furthermore, the study utilized a Dueling Bandit Algorithm for the personalization via RL thus proving its feasibility as a RL feedback personalization alogorithm in a online setting.

Terms Introduced:
Cold start problem
K Armed Dueling Bandit Problem
Multi Armed Bandit Problem
RMED
ECW-RMED
Wizard of Oz (WoZ) style

## Reinforcement learning for personalizaron: A systematic literature review

Just an overview of well reinforcement learning for personalization. Of note, it mentioned and briefly explains some common general techniques. Interestingly, it also provides numerical counts of the times that a specific algorithm was used for personalization. So food for thought, maybe your research can focus on evaluating a specific algorithm for personalization in the context of social robotics for learning.

| RL Algorithm        | Types / Sub Topics         | Points of Interest                                                                                                                                                                    | General Comments                                                                                                                                       |
| ------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Multi-armed bandits | Associative                |                                                                                                                                                                                       |                                                                                                                                                        |
|                     | Non Associative            | Only suitable when context is not important<br><br>Attractive in terms of performance and simplicity<br>                                                                              | Both do not take into account temporal separation of actions and related rewards                                                                       |
|                     | Contextual Bandit          | Provides a good starting point for personalizing an application<br><br>Less optimal than K armed problems but more simple to implement , evaluate and maintain than full RL solutions |                                                                                                                                                        |
| K-armed problem     | Action Value methods       | Value function for picking the best action given the state your in                                                                                                                    | Whether these methods are suitable or not depends on the context<br><br>Large number of tasks or constanly changin tasks make these methods unsuitable |
|                     | Incremental implementation | summing/estimation the rewards                                                                                                                                                        | Exploration may take longer than an item stays relevant                                                                                                |
|                     | Upper confidence bound     | a better way to incorporate exploration than the greedy-$\epsilon$ strategy                                                                                                           | Not suitable when the action values depend on the situation at hand. e.g time of day, user specific specifications, etc.                               |
| Contextual Bandits  |                            |                                                                                                                                                                                       |                                                                                                                                                        |
## Reading with Robots: A Personalized Robot Based Learning Companion for Solving Cognitively Demanding Tasks

Just a write up on descripting the design (both software and hardware) for this reading companion robot (IQRA') that intends to help manage the congnitive load of a read.

Congnitive load being essentially the limit of where the influx  information becomes too much for someone to handle

It identified three subcategories of confignitive load:
- intrinsic congnitie load
- extraneous cognitive load
- germane cognitive load

The robot itself had screen input capatablities, it could also move its like "head" and respond with various animated facial expressions

At the end the study also stated that this implemetation could be extended to a different domain so...I suppose that that could be something

The study also evaluated 5 constructs of the robot, namely:

- Likeability
- Perceived intelligence
- Sociability
- Social presence
- Cognitive load

Terms introduced:

- Network Oriented Modeling
- Temporal-casual network models



# Narrowing the Feedback Gap: Examining Student Engagement with Personalized and Actionable Feedback Messages

Examines and measures the effects of feedback on student performance. Of note, it designed a emperical way to evaluate which student's utilise the feedback and which did not. It found that those who utilised feedback resulted in higher grades.

It also introduceds the term "Feedback Gap"

As defined in this study, the feedback gap is as follows:

"This discrepancy between the potential and actual use of feedback has been referred to as
the “feedback gap” (Dawson et al., 2018; Evans, 2013), and its evaluation is the key to understanding the effectiveness of the provided feedback on improving student learning."

