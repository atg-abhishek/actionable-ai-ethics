# Examining the Black Box: Tools for Assessing Algorithmic Systems

**Authors**: Ada Lovelace Institute and Data Kind UK

[Paper link](https://adalovelaceinstitute.org/report/examining-the-black-box-tools-for-assessing-algorithmic-systems/)

## Summary 

### One-line summary

The paper provides some much needed clarity on what assessment in algorithmic systems can look like taking it apart on the axes of when the assessment activities are carried out, who needs to be involved, the pieces being evaluated, and the maturity of the techniques.
It also provides an understanding of some key terms used in the field and identifies the gaps in the current crop of methods as they relate to the axes mentioned above.  

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>

### What is the difference between an algorithmic audit and an algorithmic impact assessment? 

#### Algorithmic audit 

The paper talks about two kinds of audits:

````{panels}

A targeted approach that is just focused on evaluating the system for bias.

{badge}`Bias Audit,badge-primary`


----

This concerns itself with evaluating the system for compliance with regulations and norms within the place that the system is operating in; it is typically performed by regulators and auditors.

{badge}`Regulatory Inspection,badge-primary`


````

#### Algorithmic impact assessment

The paper also talks about two kinds of impact assessments: 

````{panels}

This is an evaluation of the potential harms that might arise from the use of the system _before_ it is launched into the world.

{badge}`Algorithmic Risk Assessment,badge-primary`


----

This is an evaluation of the system and its effects on its subjects _after_ it has been launched into the world. 

{badge}`Algorithmic Impact Evaluation,badge-primary`



````

So, the key difference between the two is just the temporal element. 

> The goal of clarifying these terms is to move past confusion, create shared understanding and focus on the important work of developing and evaluating different approaches to algorithmic assessment.

### What do we mean by audits? 

* In the computer science community, the term is mostly used to describe an evaluative suite of tests and other methods designed to ascertain whether the system behaves as intended by looking at its inputs and outputs. 
* In the non-technical community, audits include a more comprehensive evaluation of the system to see its level of adherence to professed norms and regulations. 

```{note}
In that sense, the former is more so aligned with the _bias audit_ while the latter is much more so aligned with the _regulatory inspection_.
```

### What might a bias audit look like? 

* This essentially takes the form of testing by researchers in the form of evaluating the system by running counterfactuals (differences on one aspect with the rest of the attributes being identical) to suss out if there are any discriminatory behaviours from the system. 
* These are typically done in a _black-box_ fashion since the researchers usually only have access to being able to send in inputs to the system and then observe the outputs from it. 

```{dropdown} What is a Black Box?
This is the idea that we are unable to examine the contents and workings of a system (intentionally or unintentionally) and that limits our analysis to taking a look at the inputs of the system and the corresponding outputs. 

This is then used to make inferences about what might be going on inside the system and how it might be working.
```

#### What are some tools and methodological approaches that can be used in this context?

Bias audits can be carried out by following one of the following three approaches as an example:

````{panels}

This is done by querying the system in question to figure out where there might be biased outcomes, but this risks running afoul of laws like the CFAA. 

There are rulings recently that give leeway to researchers to engage in this but I caution checking first that you are in the clear before embarking on this method since it is quite easy to violate the ToS of the platform.

{badge}`Scraping Audits,badge-primary`

----

This involves the creation of fake accounts, CVs, etc. to ascertain how the system might respond to the varying inputs.

{badge}`Sock Puppet Audits,badge-primary`


----

This is done when there is a mass of people who participate in evaluating the behaviour of the system by, for example, installing a browser extension. 

[The Markup](https://themarkup.org) has done some fantastic work with this approach to figure out privacy leakages in various platforms.

{badge}`Crowdsourced/Collaborative Audits,badge-primary`

````

The uniting feature of all of these audits is that they have a targeted attribute that they are looking to evaluate the impact on. 

Often these are based on some scientific and technical definitions (which in themselves might be flawed!) but the goal is to arrive at an understanding on how the system might be discriminating on that particular attribute or set of attributes. 

```{note}
The most famous example of this is the **Gender Shades** project undertaken by Dr. Timnit Gebru and Dr. Joy Buolamwini that unearthed how facial recognition systems are biased against those with darker skin and those who are not male. 
```

#### What is the benefit of engaging in bias audits? 

* It leads to more awareness that can move platforms to change their working so that we have more just outcomes from the system. 
* A multi-platform comparison also mounts peer pressure for the firms to do better so that they can retain their customer base and provide users with more information on which to choose to protect their rights. 

#### What are some future research and practice priorities? 

This is my favorite part of the paper since it lends itself more to the **Actionable AI Ethics** mindset which is what we really want to be getting at! 

The key things to be looking out for are:

1. Making sure that we have more **meta-literature*** on how impactful bias audits have been.
2. Conducting **bias audits over time** and tracking their results to see if changes arise from doing them.
3. **Looking at audits in more than just the online context**, especially in back-end systems that are used in the public sector as an example. 
4. **Examining the role of different funding instruments** and the agenda that researchers have because of that when they conduct such audits. 

### What is regulatory inspection? 

As mentioned before, this is supposed to be a more comprehensive evaluation of the system to see if there is adherence to the norms and regulations where the system is being deployed. 

```{note}
Given that this is more _invasive_ and requires more access, we need cooperation from the firms that are being evaluated and hence this falls better under the purview of regulators and auditors who have legal mandates to be able to compel the firms to such scrutiny. 
```

The UK Government's ICO Auditing framework provides a good sample of this approach and is one that can be used as a starting point for those who are looking to prepare themselves for such regulatory scrutiny. 

While this framework takes a more risk-based approach to align with the EU, in other regimes where that is not the case, you might also encounter cases with a rules-based approach. 

#### What are the future research and practice priorities? 

* Thinking about what the current skills gaps are for regulators and auditors to effectively carry out the above roles is going to be important.
* In addition, there should be a forum where successes and failures can be shared with others to accelerate the knowledge building process. 

```{tip}
The robustness of such an evaluation relies not just on the examination of the code, inputs, outputs, and the other _tangibles_ but also the **social context** within which the system is going to be deployed because that leads to differential impacts and requires due consideration. 
```

### What are algorithmic risk assessments? 

As alluded to in the tip above, these go beyond just the mandated requirements, and take a more holistic view of the system, especially the social context within which the system is deployed. 

An effort from the Canadian Federal Government has created an online questionnaire that gathers some basic data about your use case and then provides you with a list of requirements to build a _responsible AI_ system after establishing a level of risk from it.

Another approach called _stakeholder impact assessment_ seeks to bring in people who will be directly and indirectly impacted by the system into making determinations about how to build a more responsible AI application and help to uncover blindspots in the expertise that is on board the internal development team.

#### What are the future research and practice priorities? 

Quite similar to the points raised in the other instruments, what we need here are: 

* Ways to share the findings easily, building up a case-study bank that others can look into to take away valuable lessons.
* Sharing findings from other fields where such risk assessments have been conducted to make the approach in our field more robust.

### What are algorithmic impact evaluations? 

These are quite similar to the algorithmic risk assessments except that these are conducted after the system has already been deployed. 

The key thing to watch out for here is the degree to which the organizations to whom the recommendations are made actually implement the actions and whether they have the willingness to do so. 

Numerous cases in the past have demonstrated that there isn't as much of an incentive to change behaviour, especially when there is the potential to lose business. 

```{warning}
In the case of the Allegheny Family Screening Tool, after an evaluation done by researchers from Stanford that found there to not be too many problems with putting it into place, it gave the impression that it is ok to use algorithmic systems in practice. 

There have also been conflicting reports on the efficacy of the tool and we need to be careful when advocating for the deployment of more such automated tools through the legitimization of their use by such evaluation reports. There are a host of professional and ethical concerns which should be highlighted prior to even engaging in the practice of such an evaluation because post-hoc, they can provide the ammunition needed to continue their use without necessarily questioning if they should be used in the first place.
```

#### What are some future practice and research priorities?

Similar to the previous cases, having a more fleshed out set of use-cases where this has been tried along with some documented best practices for doing so effectively will be essential. 

### Conclusion 

The paper provided some much needed clarity on how different terms that are sometimes used interchangeably mean different things, have different audiences and also imply different requirements from a technical. organizational, and legal standpoint. 

Following some of the recommendations, especially in the _future research and practice priorities_ will help the field move forward faster in a deliberate fashion. 

### What does this mean for [Actionable AI Ethics](https://atg-abhishek.github.io/actionable-ai-ethics)?

* Preparing your team and organization to better meet these different needs is something that you can start to do by determining which of the mentioned instruments are more applicable to your case.
* Working actively with peers in your industry to create and augment best practices will not only help you shine as a practitioner but also push the entire field forward in terms of building more ethical, safe, and inclusive AI systems. 

### Questions that I am exploring

**If you have answers to any of these questions, please [tweet](https://twitter.com/actionable_ai/status/1325305807605559297?s=20) and let me know!**

1. Most of the places where these techniques fall flat is a lack of reporting back of the results from the deployment of these techniques. I am wondering what might be the best ways to share results so that they are discoverable. 
2. How do we incentivize people and organizations to engage in this work, especially that it seems to place additional burden (at least from their perspective) when it comes to deploying AI systems? 

### Potential further reading

A list of papers that I think might be interesting related to this paper.

* [Counterfactual Explanations Without Opening the Black Box: Automated Decisions and the GDPR](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3063289)
* [Explanation in artificial intelligence: Insights from the social sciences](https://www.sciencedirect.com/science/article/abs/pii/S0004370218305988?via%3Dihub)

*Please note that this is a wish list of sorts and I haven't read through the papers listed here unless specified otherwise (if I have read them, there will be a link from the entry to the page for that.)*

### Twitter discussion

I'll write back here with interesting points that surface from the Twitter discussion. 

*If you have comments and would like to discuss more, please leave a [tweet here](https://twitter.com/actionable_ai/status/1325305807605559297?s=20).*

### Sign up for the newsletter

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

To stay up-to-date with the latest content in terms of what I am reading and thinking about, please subscribe to the [Actionable AI Ethics newsletter](https://actionableaiethics.substack.com)

### Support me with a coffee

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>