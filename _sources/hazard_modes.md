# Hazard Contribution Modes of Machine Learning Components

**Authors**: Colin Smith, Ewen Denney, and Ganesh Pai

[Paper link](https://ntrs.nasa.gov/citations/20200001851)

## Summary 

### One-line summary

This paper provides a categorization framework for assessing the safety posture of a system that consists of embedded machine learning components. It additionally ties that in with a safety assurance reasoning scheme that helps to provide justifiable and demonstrable mechanisms for proving the safety of the system.

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>

### Definitions

* **Safety assurance arguments** : Structured reasoning that links the safety claims made about a system with verifiable and auditable pieces of evidence. Specifically, it provides defensible and comprehensive justification for the safety of a system in a given environment. 
* **Failure modes and effects analysis (FMEA)** : A bottom-up hazard analysis approach for a system with a focus on the level of components of the system.
* **Learning-enabled components (LEC)** : Software systems that consist of knowledge acquisition and machine learning components to provide a function or a service. 
* **Hazard Contribution Mode (HCM)** : A categorization of the ways in which LEC outputs can lead to hazardous system states. It does so by linking the potentially unobservable outputs of the LEC with the observable outputs of the wider system.
* **LEC accuracy** : The property of the LEC such that its outputs are globally optimal which could mean accurate classification, near-perfect regression, or selection of reward-maximization actions in reinforcement learning.
* **LEC error** : The divergence between the LEC outputs and the reference values.

### Why is this a problem in LECs?

* The problems where machine learning is utilized is often hard to specify, if it was easy to specify, it might not have warranted the use of machine learning.
* ML algorithms are often unintelligible to humans which makes their oversight hard.

### How are HCMs different from failure modes?

They are broader than just failure modes in the sense that they also encapsulate the cases where there isn't a failure but it can still lead to a hazardous state.

**Figure 2 provided in the paper is a really good reference for someone who wants to get a quick understanding of the spectrum of HCMs**

![HCM](./hcm.png)

One of the things that is important regarding this figure is that we assume that we have the ability to define the safety thresholds and states for the system as a whole. 

Keeping this in mind, violating the safety thresholds can thus lead to the transition of the system from a safe to a hazardous state.

### How does LEC error arise?

#### Supervised learning

Error can emerge from a combination of *bias* from the model assumptions and from *variance* from the type and quantity of data used and *noise*.

#### Unsupervised learning

There are several sources for errors in this context: inadequately specified optimization objective leading to *approximation errors*, an *identifiability error* from the model parameter choices that complicate the differentiation of different inputs, inadequate data a.k.a. *estimation error*, and algorithmic insufficiencies a.k.a. *optimization errors*. 

### What is expected performance? 

One of the important notions that is utilized in this paper is *expected performance*: this is basically the idea that an LEC performs as expected, be that giving an accurate output or an erroneous one. What it essentially means is that you will see outputs from the system, whether accurate or erroneous, as was exhibited during the training, validation, and calibration phases of the LEC.

#### Expected and Accurate (EA) HCM 

The system gives outputs that are accurate (as per the specification of the system) yet they induce hazardous system states.

**An example** : Say you have an autonomous vehicle (AV) that relies on lane markings to localize itself, in this case, if some of those lane markings are removed for some reason, the sensors might *latch on* to other lane markings and thus correctly align themselves with that and maintain appropriate distance except that they are **not** in the right lane and can lead to an accident. 

**When can this arise?** : This can happen in the case of sensor malfunctions or *different-from-normal* environmental conditions within which the system is operating. This might happen because of inadequate representation in the data that is used to train the system or in the optimization algorithm that is used.    

#### Expected with Error (EE) HCM

The system gives outputs that are erroneous with such a large magnitude of error that they violate the safety thresholds of the system. 

**An example** : Building on the previous example, if the lane-keeping function has some deviation in the outputs whereby the errors are so large that, for example in estimating the distance to keep in the lane, instead of keeping the lane, it leads to lane departure and hence a hazardous state. 

*A special note here that adversarial perturbations *

**When can this arise?** : In the cases where there is inadequate representation in the training data, assumptions made in the building on the ML model, especially as it relates to the relationship required between the inputs, outputs, and the safety thresholds, and an inadequate coverage of the environmental conditions within which the system will be deployed.

### What is unexpected performance? 

This refers to any behaviour from the system that is not observed during the validation of the LEC and is not expected to be seen in the *normal operating conditions* of the system. A thing to note here is that the definition of *normal* is something that probably emerges from the system specifications during the design phase but it requires more refinement if we're to correctly utilize this taxonomy.
This can happen because of unexpected feature interactions, and other emergent behaviour from the system that can cause problems when deployed in an environment where the conditions are different from the ones that the system was expected to run on.

#### How do we avoid this unexpected performance?

Compared to the case of expected performance, this requires runtime detection, recovery, and architecture-level safeguards to prevent hazardous states from emerging.

#### Unexpected and accurate (UA) HCM

This can occur in a situation where there is no notion of the ground truth. 
An example given in the paper that illustrates the other condition under which UA HCM can emerge is when there rules are learned that might be completely appropriate under many circumstances but those that fail to capture established conventions that are known through implicit knowledge.

The example goes as follows: in uncontrolled airspace, if there are two planes that suddenly find themselves on a head-on collision course, the convention dictates that both of them bank to their respective rights to avoid collision. 
But, if an automated aviation system is to learn the rules on its own, it might figure out that in many cases banking to the left saves it from collision with approaching objects and in this case would learn something that would clearly cause a collision when the human follows the convention and the automated system doesn't know about that convention.

**What is covariate shift?**

It is a change in the dataset distribution, specifically on the inputs to a system that have a different distribution from the one that it was trained on. 

**What is prior shift?**

Another kind of change in the dataset distribution when during operation the distribution of the outputs is different from the ones that it produced during training.

**What is concept shift?**

Combining both of the above in a sense, this is a shift in the joint distribution of inputs and outputs during operation compared to what the LEC had during training.

### So how do we manage HCMs?

#### Under accurate and hazardous output

We can take the following actions to mitigate the effects under this condition:
* if you have information on potential precursors to hazardous conditions, reflect them in the training and validation data.
* penalize these hazardous precursors appropriately during the training phase. 
* comprehensive testing of the model and verification-based coverage of the precursors as identified above.

#### Under hazardous output with error

* have valid safety thresholds associated with the outputs of the LEC. 
* reflect these thresholds in the training and validation data. 
* reflect these approximately in the cost or loss functions during training. 
* comprehensive model testing and verification that considers errors in relation to the overall performance of the system.

#### Potential approaches

**Prevention and Recovery**

* comprehensive definition of the operating environment making it as rich as possible.
* sufficiency of the training and validation data such that they are balanced, accurate, and complete.
* contextually-relevant model validation techniques 

**Layered Mitigation**

*The nice thing with a nod to this approach in the paper is that it borrows from the best practices in cybersecurity as well where we don't rely on a single layer of controls to protect the system*

* monitor your system during runtime to find instances where it violates the safety thresholds that you have put in place.
* have ways to disengage the system in case something goes wrong, akin to a circuit breaker. **I am currently working on a paper for this, [shoot me an email](mailto:abhishek@montrealethics.ai) if you'd like to collaborate on that!**
* have redundant functions deployed in the LEC so that there is a way to reach consensus in case there is a potential to violate the safety thresholds and then look for consensus to reinforce the above two mechanisms.

### Safety Assurance Arguments 

The following figure does a good job of showcasing what a safety assurance argumentation can look like: 

![Safety Assurance Argumentation Pattern](./safety_arguments.png)

Basically, this provides an assurance mechanism that the identified HCMs are acceptably mitigated in a demonstrable manner for stakeholders who need to be assured that the system will behave within acceptable bounds in operation. *I encourage you to refer to the paper for all the details on what each of the symbols mean and how to build such diagrams for your systems.*

### Conclusion 

Ultimately, this paper provides a neat framework for thinking about the safety implications of a system in operation and provides not only a taxonomy for thinking about the potential hazards, but also provides a framework for demonstrating the acceptability of different mitigation techniques. 

The gap filled from previous work is that it provides a holistic approach towards linking the assurances during the lifecycle of an LEC with the evidence using HCMs.

### What does this mean for Actionable AI Ethics?

* This is a great way to build more robustness into machine learning systems, especially from the perspective of having demonstrable and verifiable claims about the system.
* Given that the techniques mentioned here are system-agnostic, both from the perspective of the type of system within which the machine learning components are embedded and the type of machine learning itself, it serves as a great framework to complement other safety protocols within the organization.
* The assurance argumentation graphs also help to unearth potential blindspots when trying to ensure the safety of such systems and are a great supplement to reports that might need to be filed for auditing or regulatory purposes.

### Questions that I am exploring

**If you have answers to any of these questions, please [tweet](https://twitter.com/actionable_ai/status/1322406706073227264?s=20) and let me know!**

1. To what extent are these being practised in the industry today?
2. What is the degree of awareness on the part of the practitioners and how rigorously do they adhere to these considerations?
3. I really liked the **layered mitigation** approach and wonder if there are exemplars of this in practice?

### Potential further reading

A list of papers that I think might be interesting related to this paper.

* [ABOUT ML: Annotation and Benchmarking on Understanding and Transparency of Machine Learning Lifecycles](https://arxiv.org/abs/1912.06166)
* [Survey of Attacks and Defenses on Edge-Deployed Neural Networks](https://arxiv.org/abs/1911.11932)
* [Disruptive Innovations and Disruptive Assurance: Assuring Machine Learning and Autonomy](https://ieeexplore.ieee.org/document/8812789)

*Please note that this is a wish list of sorts and I haven't read through the papers listed here unless specified otherwise (if I have read them, there will be a link from the entry to the page for that.)*

### Twitter discussion

I'll write back here with interesting points that surface from the Twitter discussion. 

*If you have comments and would like to discuss more, please leave a [tweet here](https://twitter.com/actionable_ai/status/1322406706073227264?s=20).*

### Sign up for the newsletter

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

To stay up-to-date with the latest content in terms of what I am reading and thinking about, please subscribe to the [Actionable AI Ethics newsletter](https://actionableaiethics.substack.com)

### Support me with a coffee

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>