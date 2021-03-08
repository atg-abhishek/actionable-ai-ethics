# Responsible AI #AIForAll : Approach Document for India - Part 1: Principles for Responsible AI

**Authors**: Anna Roy, Rohit Satish, and Tanay Mahindru

[Paper link](http://www.niti.gov.in/sites/default/files/2021-02/Responsible-AI-22022021.pdf)

## Summary 

### One-line summary

Given the release of the national strategy for AI from the Indian Government a couple of years ago, this paper articulates principles for building Responsible AI systems. 
It takes an approach that is rooted in the Indian Constitution to link the principles to concrete segments of the law that provide a firm mandate for the adoption of these principles. 
It draws from similar efforts from around the globe while ensuring that the principles are somewhat tailored to the Indian context. 

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>

### Introduction 

The release of the National Strategy for AI (NSAI) by the Indian Government in 2018 was received with much fanfare as India has one of the largest populations in the world and a market that is well poised to utilize AI to further strengthen its economic posture and improve the standard of living for its people. 
One of the pillars, as articulated in the NSAI to nurture a flourishing AI ecosystem in India, is “the development of guidelines for ‘responsible AI’”. 

While there are many efforts around the world trying to do the same, this document sets the tone from the outset that it is meant to be very action-oriented with the goal of providing system and societal considerations for the design, development, and deployment of AI systems. 

### Overarching approach 

The document emphasizes the need for adhering to constitutional morality over social morality (as articulated by the Supreme Court) as the former extends beyond just the formulations in the Constitution, capturing the values of an inclusive and just society while still working in tandem with other constitutional principles. 

### The principles considered 

The principles articulated in the document mirror quite closely the [Responsible AI principles from Microsoft](https://www.microsoft.com/en-us/ai/our-approach) including safety and reliability, equality, inclusivity and non-discrimination, privacy and security, transparency, accountability, and protection and reinforcement of positive human values. 

The document starts by making a case for the need for responsible AI, leaning on arguments of how trustworthy technology also has benefits in its adoption and subsequent revenue generation for organizations that choose to take this approach.

### Systems considerations 

Leaning on the idea of procedural fairness in law, the first two systems considerations examine the requirement of explainability from the perspective of being able to build safe and reliable AI systems and being able to explain decisions made by the system to those who use the system and those who are impacted by it. The first part is important because it helps developers fine-tune and debug the system to minimize failure scenarios. The second part is important to elicit higher levels of trust and increase adoption of these systems in practice. 

An important consideration in an extremely diverse place like India is the potential for bias in these systems. This is further emphasized as a core need in the Indian context since a lot of people live below the poverty line unfortunately and the push for automation in the provision of social services. A great example in the document talks about how even though automation is used in fraud detection in making claims for medical expenses, care is always provided to those who need it and payment is settled later on with hospitals after review for fraud claims. This makes sense because the social cost of getting a decision wrong is very high in this case. 

The document then uses the example of Elaine Herzberg and the fatal Uber AV crash in Arizona (US) and a case study of automated investments in Hong Kong to articulate the need for having strong accountability measures that are able to appropriately allocate responsibility for failures though it acknowledges how that can be hard due to the blurry boundaries and intermingled nature of an AI system with the rest of the operating software and social infrastructure around it. 

One of the very few government-issued, national AI documents that I have come across that talk about adversarial attacks on machine learning, this paper does a good job of talking about breaches like membership inference attacks (when an attacker can, through querying the ML system, glean if a particular data point was used in the training of the AI system) and model inversion attacks that can hamper the safety and privacy of an AI system. 

Building on those attacks, the document also talks about how the reliability of AI systems can be affected, say through the use of adversarial examples that can trigger misclassifications of a panda as a gibbon through the insertion of barely human-perceptible noise to images. This has severe implications for AI systems that might be used in contexts like AVs that might fail unexpectedly due to the presence of such manipulations to trick the computer vision system of the AV causing it to crash. 

### Societal considerations 

The document draws from broader literature to caution against the malicious uses of AI, for example, the Cambridge Analytica incident whereby the private information of about 87 million people was leaked including that of about 5 million people from India. 

It also talks about the job impacts of AI, especially in sectors in India that have a very high potential for automation like customer support services that are being replaced with automated systems that use natural language processing and other developments to reduce the need for human labour. 

### Legal and regulatory mechanisms for the governance of AI 

The document then mentions a few examples of regulatory efforts from around the world including the EU, US, and Singapore. In India, the financial sector regulatory authority SEBI has been quite active in putting forward requirements that can help to manage the risks from AI systems. One of the other initiatives from NITI Aayog (the organization behind this document) is called the Data Empowerment and Protection Architecture (DEPA) which is a technical framework that provides guidance on how to protect the personal data of people while allowing them to leverage it to obtain services. 

The draft Personal Data Protection (PDP) bill from 2019 and the IT Act (2000) provide some more fundamental grounding in the Indian legal context to protect the rights of Indian citizens when it comes to the use of their data for building AI systems. 

A few articles in the Indian Constitution strengthen the case of the principles that have been mentioned in the document including Article 14: Right to Equality, Article 15 & 16: Right against Discrimination, Article 21: Right to life and healthcare, Article 21: Right to Privacy, and Article 38: Right to State Directive for Economic Equality. 

The principles as articulated in this document emerged from multi-stakeholder consultations that were undertaken by NITI Aayog with the goal of aligning them with the Indian Constitution to give them more teeth. A following document will further detail the implementation strategy for the principles lending even more credence to the approach. 

The document then concludes with a brief self-assessment checklist for those who want to ascertain their ethical posture when it comes to the AI systems that they are developing. 

### Between the lines

The document provides a great starting point for the various government agencies in India and other players who are going to be involved in the design, development, and deployment of AI systems. One of the places where the document can use some improvement is to ground the various principles in some realistic use cases and mention some of the approaches, both technical and otherwise, that have been used to address the challenges that have arisen. These will help the reader of the document gain a more realistic view of the state of affairs and also eliminate a degree of uncertainty that comes from reading such documents that can paralyze practitioners because of the potentially immense amount of work that they would have to undertake. 


### What does this mean for [Actionable AI Ethics](https://atg-abhishek.github.io/actionable-ai-ethics)?

* As a practitioner, aligning with the laws of the land where your solution will be operating is key and having such a document does help you become more cognizant of some of the requirements that will be non-negotiable in your development process. 
* As we get more national AI strategies that are constitutionally-aligned, it will become easier to comply with those requirements, since they would have popped up in various forms in other avenues as well such as compliance with local privacy laws. 

### Questions that I am exploring

**If you have answers to any of these questions, please [tweet](https://twitter.com/actionable_ai) and let me know!**

1. How will we move to reconcile differences in approaches across different countries?
2. How do we increase the transparency in the stakeholder consultation process when it comes to the development of documents like these?

### Potential further reading

A list of papers that I think might be interesting related to this paper.

* The [OECD Policy Observatory](https://oecd.ai) has a lot of other country-wise documents that form an interesting repository of strategies to read.

*Please note that this is a wish list of sorts and I haven't read through the papers listed here unless specified otherwise (if I have read them, there will be a link from the entry to the page for that.)*

### Twitter discussion

I'll write back here with interesting points that surface from the Twitter discussion. 

*If you have comments and would like to discuss more, please leave a [tweet here](https://twitter.com/actionable_ai).*

### Sign up for the newsletter

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

To stay up-to-date with the latest content in terms of what I am reading and thinking about, please subscribe to the [Actionable AI Ethics newsletter](https://actionableaiethics.substack.com)

### Sign up for the AI Ethics Brief by the [Montreal AI Ethics Institute](https://montrealethics.ai)

<iframe src="https://brief.montrealethics.ai/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

### Support me with a coffee

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>