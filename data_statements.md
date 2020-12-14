# Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science

**Authors**: Emily M. Bender and Batya Friedman

[Paper link](https://www.aclweb.org/anthology/Q18-1041/)

## Summary 

### One-line summary

The paper provides a new methodological instrument to give people using a dataset a better idea about the generalizability of a dataset, assumptions behind it, what biases it might have, and implications from its use in deployment. It also details some of the accompanying changes required in the field writ large to enable this to function effectively.

### What is a data statement?

> A data statement is a characterization of a dataset that provides context to allow developers and users to better understand how experimental results might generalize, how software might be appropriately deployed, and what biases might be reflected in systems built on the software.

* A benefit that we might get from the use of data statements is that it will help with generalizability and reproducibility in the field, something that has been pointed out as a concern at many workshops like NeurIPS, ICML, and ICLR.
* A clarification that authors provide is the difference between ethical practice and sound science where having one doesn't mean we necessarily get the other. You might get accurate results based on some metric giving you sound science but it doesn't make the use of that technology ethical.

### Key terms 

* While some of the common terms are fairly well-known in the NLP community, the paper sheds an important light on nuances to some of them for better understanding. 
* For example, it talks about **curators** who are the people who make decisions, for example, on which search terms to use for gathering data, selecting where to look, who to interview, and other meta-level choices that have downstream implications. 
* An interesting distinction made in the stakeholders is around those who are **indirect stakeholders**, for example, those whose data might be rendered invisible due to how search terms are processed and utilized in an NLP system. 

#### Bias

* Providing a very clear summary of what bias means in this context, they refer to how bias (in the social sense) occurs only when it is done _systematically_ and leads to _unfair outcomes_.
* It also talks about **pre-existing biases** which have roots in social institutions, practices, and attitudes. 
* **Technical biases** stem from technical constraints and decisions.
* **Emergent biases** are those that arise when a system is developed for one situation and is supplanted into another.

An example that clarifies why we might need data statements in NLP is from research cited in this paper that points to how Mexican restaurants with similar star ratings got lower ratings on their reviews because of pre-existing biases against the word Mexican in the wider use of that term.

### What will data statements look like?

The paper provides a schema with a minimum set of items that must be included but also goes on to talk about how there will need to be some best practices that emerge from the field as they start to become more widely used. 

Here are the elements: 

* **Curation Rationale**: What were the decisions and assumptions that led to a certain data source being selected, both in the original and the sub-selection that might be made in the case of reuse?
* **Language Variety**: Given that languages have different structures and might thus interact differently with the NLP algorithms, taking a tag from [BCP-47](https://tools.ietf.org/rfc/bcp/bcp47.txt), a standardized way to identify languages along with a prose description of that tagging will help in understanding the language captured in the dataset. In addition, paying attention to the dialect used will also help downstream researchers make appropriate decisions. 
* **Speaker demographic**: Here speaker is used to the generator of the text artifact. Having information on the demographics will also help to make determinations about language artifacts to expect in the dataset since people use language in differing fashion to project their identity. This should include:
    * Age
    * Gender
    * Race/ethnicity
    * Native language
    * Socioeconomic status
    * Number of different speakers represented
    * Presence of disordered speech
* **Annotator demographics**: The same points as above are also essential for better understanding artifacts in the dataset because the _social address_ of the annotators will determine how they interact with the data. Some attributes to capture here include: 
    * Age
    * Gender
    * Race/ethnicity
    * Native language
    * Socioeconomic status
    * Training in linguistics/other relevant discipline
* **Speech situation**: We all realize that we speak quite differently in different contexts, depending on the situation we are in, who we are speaking to, etc. Capturing this information is also essential which should include:
    * Time and place
    * Modality (spoken/signed, written)
    * Scripted/edited vs. spontaneous
    * Synchronous vs. asynchronous interaction
    * Intended audience
* **Text characteristics**: The genre and the topic will influence the text that shows up in the data.
* **Recording quality**: Any particulars about how the recording was done and any limitations of the equipment will also help to understand any shortcomings that might show up in the dataset.
* **Other**: This is the placeholder where best practices can be integrated as they evolve over time.
* **Provenance Index**: In the case of reuse of the dataset, we can include information linking it to the origin to help people understand how the dataset has changed over time and if there are things that they should watch out for.

An important point to note is that while it might seem onerous to repeat the information again and again for datasets that are commonplace in the NLP community, considering the data in new light every single instance will help people better understand the capabilities and limitations from that data in the new task at hand.

* Having a short form of the data statement between 60-100 words will also help direct inclusion in papers that are published which will be useful to have persistent reminders of the specificities of the data that is being used.
* The paper also provides two sample case studies which can be used to understand how the data statements might be used in practice.
* Even retroactive application of data statements has value, though they won't be as good as making them right when the dataset is being created because of the loss of information over time unless there are strict records. 

### Potential barriers to implementation and mitigation strategies

* If the ACL implements this as a requirement, those who are not yet members of ACL and are not aware of how to craft good data statements might face desk-rejection for their work.
* Having mentorship programs, training modules, and how-to guides will help to bridge this gap.
* These require time to craft (2-3 hours based on the experience of the authors) but the potential payoff is high and thus we must incentivize researchers to do so.
* They take up space in the paper if they are included and hence the authors ask that conferences exclude these from page and word limits. 
* While excluding demographic information can obviate the need for ethics reviews in some instances, collection of this information might add that as a burden for projects that didn't previously engage in that.

### Differences from related work

* Some of the elements from data statements might ring familiar to those who are interested in this kind of things, I've linked some of those pieces of work at the bottom of this post. But, data statements do stand out in some regards in the sense that data sheets for datasets, as an example, for broader and thus left a lot of elements with too much flexibility which can make their application inconsistent. 
* Similarly, algorithmic impact assessments also provide very high-level guidance but data statements provide more granularity making them more _actionable_!

### Implications for tech policy

* Without the presence of clear information about the origins of the data and the limitations that are posed by their use in different systems, we might end up in situations where we limit the ability of citizens adversely affected by these systems to mount effective challenges because of the lack of sufficient evidence to back their claims.
* Having some sort of requirements in certification processes can also normalize and standardize the use of such instruments. 
* The authors also advocate that we ensure that people using software give preference to those that come with such data statements over those that don't to mount pressure on the rest of the community to adopt the practice.

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>

### Conclusion 

Data statements will provide many benefits to the field including better generalizability and reproducibility. It will empower stakeholders to be better informed about the capabilities and limitations of the system. For people in the industry it can be a forward-looking initiative that helps prevent PR nightmares because of overlooked areas.

### What does this mean for [Actionable AI Ethics](https://atg-abhishek.github.io/actionable-ai-ethics)?

* Having such documentation more well-integrated into the MLOps workflow will be crucial for the success of adoption and utilization. You can see my thoughts on that [here](https://actionableaiethics.substack.com/p/actionable-ai-ethics-1-adopting-an).
* Having domain-specific formats that are agreed upon by practitioners will be the way forward, and I encourage us as _Actionable AI Ethics_ practitioners to share best practices and lessons that we learn in the use of such instruments in our work.

### Questions that I am exploring

**If you have answers to any of these questions, please [tweet](https://twitter.com/actionable_ai/status/1324581030825807872?s=20) and let me know!**

1. What has been the progress so far in implementing such requirements in the field?
2. What are some lessons that we can learn from things like the broader impact statements at different conference? What has worked and what hasn't that can be applied here?

### Potential further reading

A list of papers that I think might be interesting related to this paper.

* [A Nutrition Label for Rankings](https://dl.acm.org/doi/10.1145/3183713.3193568)
* [Datasheets for Datasets](https://arxiv.org/abs/1803.09010)
* [Model Cards for Model Reporting](https://dl.acm.org/doi/10.1145/3287560.3287596)

*Please note that this is a wish list of sorts and I haven't read through the papers listed here unless specified otherwise (if I have read them, there will be a link from the entry to the page for that.)*

### Twitter discussion

I'll write back here with interesting points that surface from the Twitter discussion. 

*If you have comments and would like to discuss more, please leave a [tweet here](https://twitter.com/actionable_ai/status/1324581030825807872?s=20).*

### Sign up for the newsletter

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

To stay up-to-date with the latest content in terms of what I am reading and thinking about, please subscribe to the [Actionable AI Ethics newsletter](https://actionableaiethics.substack.com)

### Support me with a coffee

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>