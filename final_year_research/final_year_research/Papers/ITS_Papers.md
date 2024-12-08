## Seis Tutors

Offers personalisation by identifying tutoring strategy based on a pretest (learning style and domain test), exclusive curriculum design and observation of learner physchological state during sessions.
## CIRCSIM-Tutor: An Intelligent Tutoring System using Natural Language Dialogue (1996)

Essentially described the system they're creating/created, CIRCSIM.

Aimed to provide tutor assistance to students studying cardiovascular physiology. 

It trained itself on dialogues created from human to human tutoring sessions.


## Hybrid Intelligent Systems Based on Psychological and Learning Styles Design Implementation

Used neural networks to aid in providing curated "navigation" of content in an ITS catered for students' learning styles, for example MYERs personality profiles.

Answers of questionnaire were used to characterise, the pschological profile and learning styles of users and learning styles of users. These characteristics of the users along with expert rules are used to guide students through the navigation of content.

Say for example, there are three levels: easy, intermediary, advanced. You have a test for the entry level (say intermediary) and then you can choose guided navigation whereby the system will help you navigate throughout the different levels inorder to optimize student performance.


## Design framework of adaptive intelligent tutoring systems (2020)

Provides a very useful overview for designing an adaptive ITS. particularly of note, it provides a table for ITS elements in the field of information technology in terms of what adaptive features are typically there at a university level.

## Automated Data-Driven Generation of Personalized Pedagogical Interventions in Intelligent Tutoring Systems (2021)

In effect, this describes some techniques and stuff relevant to designing and utilizing their own Intelligent Tutoring systems. The system described used some RL framework for selecting personalized hints when solving some problem and also utilized generative AI with wikipedia articles for providing generative explanations. Personalized hints were deemed more successful even though students liked wikipedia explanations.

The problem addressed with this was to encounter the rigerous process of creating rules and systems for a typical Intelligent Tutoring System, hence the automation of such.

It also gives some general guidelines for future work. Following are ones of particular interest and perhaps relevance to myself:

1. development of models capable of formative feedback "Such models can be applied both to mathematical hints, providing students with further insights as to why their equations may be
incorrect, and to textual hints and explanations, identifying what is missing or what is
conceptually incorrect in the given answer and providing students with the guidance
towards fixing the missing or incorrect ideas in their answers."

2. Investigate the interplay between the granularity of formative feedback and student learning profile

Hints are generated based on extracted keywords from both the question and the expected answer. e.g. 
![[Pasted image 20241101140631.png]]

Then the hints are selected based on other algorithms that take into a personalisation aspect. There are three levels of personalisation that the system takes:

1. BASELINE : lingustics features pertaining to hints
2. SHALLOW : linguistic features + performance based features
3. DISCOURSE :  lingustics features pertaining to hints + performance based features + linquistic features applied to student intereactions

Wikipedia based explanations


## Design of an Intelligent Tutor System for the Personalization of Learning Activities Using Case-Based Reasoning and Multi-Agent System


## Artificial Intelligence in Intelligent Tutoring Systems Toward Sustainable Education: A Systematic Review

Overall makes note of the drive of using ITS towards sustainable education development and also makes note of several tables highlighting the need for personalization as both a use and a research avenue.
##### RQ4: what is the future trend of AI/IT embedded ITS in sustainable education

Problems of note: 
- The amount of data limits how good a system can be. Some research focuses (Corrigan eta al., 2015a; Guerrero-Higueras et al,. 2018) on obtaining more sampling data. Other limitations included needing longer period learning data and the solution not being portable to other tutoring systems. (here i can insert arguments for dpo and sdpo as a incremental increase of performance while extracting data.)

## Intelligent Tutoring Systems An Overview

Ill defined domains - not what you think, these are just domains or areas where the problem can have multiple solutions or there is known consensus on a solution. Think of the humanities, for example. Lots of questions, lot of controversies, no clear answers.

they lack a definitive answer; 2) the answer is heavily dependent upon
the problem’s conception; 3) problem solving requires both retrieving rele-
vant concepts and mapping them to the task at hand

Linear problem
branching programs

Three model architecture
- student
- tutor
- domain

 Four model architecture
- student
- tutor
- domain
- user interface

Examples of ITS:
- SCHOLAR
- ANDES (Physics)
- Cognitive tutor (Algebra)
- Wayang (Mathematics)
- Project Listen (Reading) - interestingly enough, used SST it seems
- ASSISTments (Mathematics)
- Crystal Island (Microbiology) - 3D game based environments
- BILAT, Interview, A Military Simulation
- Helicopter PilotUs Army and ARI, StottlerHenke - adaptive flight simulation tutor
- Tactical Action Officer - tactical training tutor. speech enabled graphic user interface. soldiers converse with simulated team member to issue commands.
- Blitz Game Studio's Triage Trainer

#### Rule-based model
Model training
step by step solutions
with ill defined domains or overly complex domains, it is difficult to contruct these rules

#### Constraint based model

Focuses on specifying constraints rather than rules. if a learner violates a constraint during a task, the tutor diagnoses that error and provides help to the learner.

The sequence of steps is not deemed important, anyalysing the current state is enough to diagnose mistakes.

#### Expert Systems

An emulated expert that can be used to compare learner solutions with expert solutions.

Challenges:
- developing or adapting an expert system can be costly and difficult espescially for ill defined domains
- some expert systems cannot justify their inferences, or provide explanations that are appropriate for learning

After stating the characteristics of well-defined domain (Ill-defined
domains lack well-defined models and formal theories that can be opera-
tionalized, typically problems do not have clear and unambiguous solutions)
and underling that in ill-defined domains are typically taught by human
tutors using exploratory, collaborative, or Socratic instruction techniques
they describe the challenges facing researchers in the field of ill-defined: 

1.  Defining a viable computational model for aspects of under specified or open-ended domains;
2. Development of feasible strategies for search and inference in such domains; 
3. Provision of feedback when the problem-solving model is not definitive; 
4. Structuring of learning experiences in the absence of a clear problem, strategy, and answer; 
5. User models that accommodate the uncertainty of ill-defined domains; and 
6. User interface design for ITSs in ill-defined domains where usually the learner needs to be creative in his actions, but the system still has to be able to analyze them

