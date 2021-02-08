# Understanding the Capabilities, Limitations, and Societal Impacts of Large Language Models

**Authors**: Alex Tamkin, Miles Brundage, Jack Clark, and Deep Ganguli

[Paper link](https://arxiv.org/abs/2102.02503)

## Summary 

### One-line summary

The paper provides insights and different lines of inquiry on the capabilities, limtations and the societal impacts of large-scale language models, specifically in the context of the GPT-3 and other such models that might be released in the coming months and years. 
It also dives into issues of what constitutes intelligence and how such models can be better aligned with human needs and values. 
All of these are based on a workshop that was convened by the authors inviting participation from a wide variety of backgrounds.

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>

### Technical Capabilities and Limitations

One of the points that immediately caught my eye when reading this paper which often goes unsaid in many conversations is the lack of transparency around how many other such large-scale models (like the GPT-3) are being used by corporations that haven't been disclosed. 
In particular, based on the challenges that have been encountered in terms of biases in the GPT-3 model, because of the corpora of data that it is trained on, what might be the datasets that such undisclosed models are trained on and what are some of the protective measures that are adopted by them. 

#### Scale leading to interesting results 

The paper points to how the simple idea of scaling the number of parameters and the amount of data ingested by the system led to a lot of interesting properties in the system which is functionally similar to the smaller GPT-2 model. 
The participants in the workshop pointed to similarities with the laws in physics and thermodynamics. 

> We talk a lot about interdisciplinarity between domains if we're to build responsible AI systems, but something that jumped from the discussion as presented in the paper was the requirement to have many different technical subdomains also working together so that the system can be fielded responsibly including those who manage the infrastructure that helps to run such large-scale models in the first place. 

#### What do we mean by intelligence and understanding? 

The current methodology for judging the performance of a system stems from various accuracy and performance metrics that seek to allocate a score based on how frequently the system is right. 
An important distinction that participants pointed out was when you have systems that are going to be used in important domains like healthcare, etc. we might need to reconsider if being "mostly right" is going to be adequate. 
Specifically, we would need to consider if there are important examples that the system is getting wrong and have higher penalties in those situations to align the system more with what matters to humans. 

Another interesting point of discussion was whether this obsession with understanding is even important for exhibiting intelligence as they pointed to how a recent Scrabble champion in French knew very little French in the first place as trained himself solely for the competition. 

> Acquiring more from less data might require multimodal training datasets that could accelerate the learning acquired by the system, something that a lot of researchers are working on. 

#### Alignment with human values

While what constitute human values itself has a lot of variance across different cultures and regions, there was a strong emphasis on at least involving people from many different domains to gain a more holistic sense for this. 
In addition, working towards techniques that are explicitly tasked with ensuring the alignment in the first place was another requirement that participants emphasized as we venture into ever-larger models that have the potential to start exhibiting what some might call general intelligence.

### Societal impacts 

As GPT-3 has exhibited many different capabilities, taking basic task descriptions like the natural language description of a website and then generating the boilerplate code for that or in parsing legal documents and sharing summaries of them, the questions about the societal impacts of such models loom large. 

#### Controlled access

A point made by the participants was that given that OpenAI has constrained access to the model behind an API, there is a higher degree of control in preventing misuses of the model. 
But, a related concern is that there is a lack of transparency when it comes to how such requests for access are processed in the first place and who is and who isn't denied access in the first place. 

#### Deploying such models 

Arguments for th societal benefits and harms can be made in many different fora, but if we are to adopt a more scientifically rigorous approach, we need to come up with more defined metrics against which we can benchmark such systems. 
While no organization can maintain a lasting advantage when it comes to such models, there is also a responsibility that such organizations should undertake in setting responsible norms that others can follow, especially when they are large organizations and they can dedicate efforts towards doing so.

#### Potential for accelerating disinformation

This has been one of the most cited harms when it comes to large language models that can produce coherent and persuasive text. 
To that end, investments in being able to discern between the two and helping people recognize them in the wild is also going to be an important skill that needs to be built up over time. 
Cryptographic methods that can ascertain the authenticity of content and verify its provenance might prove to be effective ways to ensure a healthy information ecosystem. 

#### Bias 

This has been demonstrated through many ad-hoc and rigorous studies that GPT-3 exhibits bias, some of which is a function of the text corpora that it is trained on. 

> A very important distinction that was made by the participants here was the emphasis that we must place in carefully defining what is biased and what isn't for large language models such as GPT-3 that might be used in wildly differing contexts and being inherently multi-use. 

Red-teaming and combatting bias through the use of expansive and publicly shared bias test suites were the two measures that caught my eye in the paper in addition to some of the other well-known approaches to detecting and mitigating biases. 

#### Economic impacts 

Expanding the access to the model through the API can become a way to gather signals in terms of how the use of the model is impacting people from an economic standpoint as it would help to surface new ways that people employ the model for automation.

### Future Research Directions

For anyone that wants to keep an eye out for where the field might be headed, the research directions section of the paper provides some good jumping off points. 
The one that caught my eye here was creating a more thorough understanding of the threat landscape in a way that emphasizes more rigorous research in making these models more robust.

### Conclusion 

The paper provides a comprehensive but abbreviated overview of the current capabilities and limitations of large language models. More importantly, it provides potential areas of investigation to improve the stature of how we conduct research into the societal impacts of these models and how we might do better. 

### What does this mean for [Actionable AI Ethics](https://atg-abhishek.github.io/actionable-ai-ethics)?

* Staying abreast of how large-scale models are built, the challenges they face, and what we can do to perform better on that front is going to be an important consideration when thinking about which ethical measures to put in place.
* In particular, being cognizant of the areas where such systems can fail will also be essential if you're to build more robust systems. 

### Questions that I am exploring

**If you have answers to any of these questions, please [tweet](https://twitter.com/actionable_ai) and let me know!**

1. How do we gain better insights into the potential development and fielding of large-scale models like GPT-3 that are undisclosed to the public?
2. How do we move towards an ecosystem that democratizes the access to such models without requiring access to large-scale compute and data infrastructure?

### Potential further reading

A list of papers that I think might be interesting related to this paper.

* [On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](http://faculty.washington.edu/ebender/papers/Stochastic_Parrots.pdf) 

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