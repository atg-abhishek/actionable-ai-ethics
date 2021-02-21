# Algorithmic content moderation: Technical and political challenges in the automation of platform governance

**Authors**: Robert Gorwa, Reuben Binns, and Christian Katzenbach

[Paper link](https://journals.sagepub.com/doi/full/10.1177/2053951719897945)

## Summary 

### One-line summary

The paper provides a comprehensive overview of the existing content moderation practices

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>

<br>

The Global Internet Forum for Counter-Terrorism is a cross-company group that helps to share information across some of the major tech providers to combat illegal online hate speech. They regularly share information with each other to help increase the efficacy of their content moderation efforts. 

> As the amount of user-generated content (UGC) goes up in volume, the ability to effectively utilize community and human moderation is diminished and we have to rely on automated and commercial content moderation. 


````{panels}

Relying on the members of the community in a distributed manner to self-moderate the content that is created and distributed on a platform.

{badge}`Community moderation,badge-primary`


----

This involves hiring dedicated staff who are responsible for moderating the content by reviewing those that are either flagged by users or put in their review queue by some other mechanism.

{badge}`Human moderation,badge-primary`



````

### What are the key challenges in commercial content moderation? 

* the human cost: subjecting the reviewers to traumatic content on a frequent cadence leads to long-term psychological harm
* what constitutes "valid" content is determined by a homogenous set of people in Silicon Valley that affects people all around the world 
* a potential lack of transparency and accountability, especially when things go wrong. 

### What are some of the reasons precipitating the need to utilize AI for content moderation? 

* very large amount of UGC 
* short response times dictated by legislations, for example the NetzDG or the EU Code of Conduct on Hate Speech, that necessitate the use of AI to meet those requirements. 

### What is algorithmic moderation? 

An important point made in the paper pointing to prior work by Grimmelmann talks about how moderation is not just the act of administrators and others involved in the moderation process to remove content, but it also includes the design decisions that are made for the platform that dictate how users interact with each other. 

_In this paper when the term algorithmic moderation is used, it refers to algorithmic commercial content moderation._

This refers to the act of either doing _prediction_ or _matching_ that leads to a decision or governance outcomes related to the piece of content and the parties involved. 
As an example, it could be taking down the content, geoblocking, suspension of accounts, among other actions. 

Again, in this paper, the focus is on **hard moderation** which refers to actions like taking down content and blocking accounts vs. **soft moderation** which refers to design decisions, recommendation algorithms, and other approaches that are used to govern the interactions between content and users on a platform. 

### Some basic terminology 

````{panels}

A technique that transforms a large piece of data into a smaller piece of data, trying to uniquely identify it despite the change. They are frequently used in cryptography to check the integrity of content. 

{badge}`Hashing,badge-primary`


----

Since hashes are supposed to be unique and two dissimilar pieces of content should give different hashes, if content is altered for example through rotation or watermarking, we might miss previously flagged content in this modified form.
Homologies are a way to counter that problem through hashing techniques that are insensitive to those changes allowing for matching of "similar" content.

{badge}`Homology,badge-primary`


----

Since the cryptographic definition of hashing requires exact matching which is orthogonal to what we want to achieve with hashing in content moderation, there are non-cryptographic approaches to hashing like perceptual hashing which focus only on the perceptually relevant features in a piece of content. 
This means that it doesn't change if minor features in the content are altered that would still lead them to be perceived the same way by humans. 
This allows us to match similar content and leverage previously flagged content to prevent it from spreading again.

{badge}`Perceptual Hashing,badge-primary`


----

Matching refers to the use of any of the hashing techniques to identify whether there exists the same content (modified or otherwise) in the previously flagged content repository so that it can automatically be removed.

{badge}`Matching,badge-primary`


----

Classification refers to the approach of using the previous bank of flagged content and bucket new incoming content into a category that is most appropriate given the other content in that repository. 

{badge}`Classification,badge-primary`


````

### So, what are some of the problems?

For starters, maintaining a blacklist of this content that is shared and accessible across the major platforms is a very challenging task.
Content, especially multi-modal content, constantly changes in meaning over time. 
Words take on new meanings based on the societal context in which they are used, and there are also limitations in the kind of examples that are available in the flagged content repository.
Relying on domain-specific ontologies, for example a list of words that are deemed to be offensive to the LGBTQ communities based on consultations with domain experts is one way to address this challenge but that requires us to be able to go out and do that for a lot of different communities and coordinate that effort across all the platforms that might need to use such an ontology.

#### What is the problem with matching?

* It requires a manually curated list of flagged content that needs to constantly be kept up to date. 
* It needs to be robust to variations introduced by malicious actors who are trying to evade moderation efforts.

#### What is the problem with classification? 

* It requires inducing generalizations from existing content bases which might not be culturally or contextually relevant beyond the home base of the content that is used to generate these generalizations. 
* New categories may emerge which will again need manual effort before they are effective as a content moderation tool.

### What happens when content is matched or classified?

The content can either be flagged or deleted. 

````{panels}

The content is identified for further processing at which point it enters the queue of content to be reviewed by human moderators, or pushed into a high-priority queue to be reviewed faster or by an expert moderator.

{badge}`Flagging,badge-primary`


----

The content is deleted without further review.
This is reserved as an action for more serious violations of the terms and conditions of the platform.

{badge}`Deletion,badge-primary`



````

### What does the future hold? 

* When considering text content, given the complexity of language, it is incredibly hard to encode cultural and contextual factors into an automated system, so the presence of human moderators won't be fully eliminated.
* Human moderator's efforts will be augmented through the use of automated content moderation systems.
* Companies using shared hash databases, and different policies of flagging and deleting need to become more transparent to earn the trust of their community of users.
* The above point is important because there is an uneven application of community standards and the severity of content moderation based on the commercial motivations of different platforms. 
* Opening up the shared databases and more access to the policies as they are actually applied to content moderation will be helpful to 3rd party auditors and researchers to make the systems more just and help them work in the interest of users rather than **only** serving commercial interests.

### Conclusion 

Content moderation is an incredibly complicated field in the application of AI and it more than other endeavors perhaps requires the inclusion of domain experts and communities in the formulation of community standards and moderation approaches. 

Additionally, higher levels of transparency in how the content moderation is applied in practice will also help to elicit higher levels of trust from the user community on the platforms. 
### What does this mean for [Actionable AI Ethics](https://atg-abhishek.github.io/actionable-ai-ethics)?

* The design of content moderation systems should be flexible to include the input of external stakeholders, including domain experts and community members.
* The flexibility of such systems should also be such that one can easily integrate emerging uses of language and other media, for example memes as a form of multi-modal content diffusion. 

### Questions that I am exploring

**If you have answers to any of these questions, please [tweet](https://twitter.com/actionable_ai/status/1324943418712334336?s=20) and let me know!**

1. What is an effective way to include emergent language uses into content moderation systems in an unsupervised manner?
2. What is the extent to which external community stakeholders are invited to contribute to the content moderation practices of different platforms today? 

### Potential further reading

A list of papers that I think might be interesting related to this paper.

* [Notice and Takedown: Online Service Provider and Rightsholder Accounts of Everyday Practice](https://doi.org/10.31235/osf.io/hp9fz)
* [Publicity and Transparency: The Itinerary of a Subtle Distinction](https://doi.org/10.1007/978-3-319-77161-8_10)
* [What Can I Do? How to Use Social Media to Improve Democratic Society](https://doi.org/10.1080/10584609.2019.1610620)

*Please note that this is a wish list of sorts and I haven't read through the papers listed here unless specified otherwise (if I have read them, there will be a link from the entry to the page for that.)*

### Twitter discussion

I'll write back here with interesting points that surface from the Twitter discussion. 

*If you have comments and would like to discuss more, please leave a [tweet here](https://twitter.com/actionable_ai/status/1324943418712334336?s=20).*

### Sign up for the newsletter

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

To stay up-to-date with the latest content in terms of what I am reading and thinking about, please subscribe to the [Actionable AI Ethics newsletter](https://actionableaiethics.substack.com)

### Sign up for the AI Ethics Brief by the [Montreal AI Ethics Institute](https://montrealethics.ai)

<iframe src="https://brief.montrealethics.ai/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe
### Support me with a coffee

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>