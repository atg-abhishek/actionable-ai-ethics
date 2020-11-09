# Fairness Definitions Explained

**Authors: Sahil Verma and Julia Rubin**  

[Paper link](https://dl.acm.org/citation.cfm?id=3194776)

## Summary

### One-line summary

The basic premise of the paper is that it will attempt to explain how because of different definitions of fairness, we can have scenarios that are fair according to one and not fair according to another. 

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>

### Data and techniques used

* As an example it uses the [German Credit Dataset](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)) and checks if there are any biases based on gender. Given prior work that has shown how some definitions are necessarily incompatible with each other, the findings from this paper bear the same in terms of the final results. 
* Given that there was so case of a single female applicant, the authors don’t take that into consideration and in making cross-gender comparisons, they just look at married and divorced males and females.
* They used a logistic regression model with 10-fold cross-validation using 90% of the dataset as training data and 10% as test data. The numerical and categorical variables were used directly and the categorical variables were converted to binary attributed giving a total of 48 attributes.

### Definitions

*There are many, many definitions in this paper, and this is my attempt at making the most sense of them and keeping them all organized for easy reference for the rest of the summary*

I'll try and steer away from using mathematical notation because there will be a lot of symbols and I feel that it will be easier to get a sense for each of these definitions when expressed in natural language.

#### Statistical Definitions

##### Basics

* **True Positive (TP)** : when the predicted outcome and the actual outcome are both in the positive class
* **True Negative (TN)** : when the predicted outcome and the actual outcome are both in the negative class

*So, both of the above are the cases when you are spot on!*

* **False Positive (FP)** : when the predicted outcome is positive **but** the actual outcome is negative.
* **False Negative (FN)** : when the predicted outcome is negative **but** the actual outcome is positive.

*These are both cases where a mismatch has occurred.*

**My recommendation for these first 4 definitions if you're encountering these for the first time is to stick to keeping in mind one from each bucket (and remembering that well), the other one in that bucket is just the opposite of that.**

*Make sure that you really get these before we move on to the other definitions since they will use these as building blocks!*

##### Intermediate

* **Positive Predictive Value (PPV)** : Divide the correct positive predictions that you made by *all* the cases where you predicted positive outcomes. **This is also called precision** (a term that you will encounter frequently in the field)
* **Negative Predictive Value (NPV)** : Similar to the one above, divide the correct negative predictions that you made by *all* the cases where you predicted negative outcomes. *You can choose to just remember the previous definition and you'll know that this is just the case for the negative classes.*

* **False Discovery Rate (FDR)** : This is the probability of false (or wrong) acceptance.
* **False Omission Rate (FOR)** : This is the probability of wrongly rejecting someone. *Again, here you can choose to just remember the previous one and know that this is the opposite case.*

*So, these were all definitions where we were only looking at the predicted outcomes, the difference in the following definitions is that we will also look at the actual outcomes.*

* **True Positive Rate (TPR)** : This is the probability of identifying a truly positive subject as such. **This is also called as sensitivity or recall.** (common references for this term in the literature)
* **True Negative Rate (TNR)** : This is the probability of identifying a truly negative subject as such. *Again, here you can choose to just remember the previous one and know that this is the opposite case.*

*The above two definitions are the cases of correct identification amongst all the actual cases belonging to that class.*

* **False Positive Rate (FPR)** : This is the probability of false alarms, that is falsely accepting a negative case.
* **False Negative Rate (FNR)** : This is the probability of getting a negative result for actually positive cases.

#### Definitions based on predicted outcomes

Let's give a quick definition for **protected attributes** : these are attributes which are *sensitive*, which are the subject of potential discrimination. Someone belong to the protected group then is the one who has a positive value for this attribute and the unprotected group is the one that has negative values for this attribute.

* **Group Fairness** : Members from both the protected and unprotected group have the same probability of being assigned to the positive predicted class. In the case of the credit example, this means that regardless of gender, you have an equal probability of being assigned a good credit score.

*Note that the above is also called equal acceptance rate, benchmarking, and statistical parity (not to be confused with the following definition)*

* **Conditional Statistical Parity** : Extending the previous definitions, this definition allows for the inclusion of a group of legitimate factors that won't be considered discriminatory when included in the decision making process. So, controlling for these factors, the groups should have equal probabilities of landing with positive predicted values.

#### Definitions based on predicted and actual outcomes 

* **Predictive Parity** : The fraction of correctly predicted positive cases should be the same across the protected and the unprotected group.

*This is also called outcome test*

* **False positive error rate balance** : Getting similar results for both groups when they actually belong to the negative class.

*This is also called predictive equality*

* **False negative error rate balance** : The probability of a subject in a positive class to have a negative predictive value should be the same across the groups. A thing to note here is that 

*This is also called equal opportunity*

* **Equalized odds** : Combining the previous two definitions, this definition tells us that, across the two groups, we should get a similar classification for those with actual positive outcomes and actual negative outcomes.

*This is also called disparate mistreatment and conditional procedure accuracy equality*

* **Conditional use accuracy equality** : This definition gives equivalent accuracy, across both groups, for both positive and negative predicted classes.  

* **Overall accuracy equality** : Across both groups, this definition gives equal prediction accuracy for those who are in the positive and negative classes to be correctly assigned to those classes. **A thing to note here is that we are assuming that we value equally true positives and true negatives which might not always be the case.**

* **Treatment equality** : Across both groups, this definition looks that the ratio of errors made is the same (i.e. the ratio of false positives to false negatives).

#### Definitions based on predicted probabilities and actual outcomes

* **Test fairness** : Given the probability score from the classifier, across both groups, this definition checks if the subjects have equal probability of truly belonging to the positive class. 

*This is also called matching conditional frequencies and callibration*

* **Well-callibration** : This extends the previous definition by saying that not only should the probability of truly belonging to the positive class is the same across the groups but that it is also equal to the predicted probability score. The reason to do so is that we are trying to *callibrate* the classifier by checking if it indeed meets the base rate prevalence for truly belonging to the positive class as it predicts.

* **Balance for positive class** : The subjects constituting the positive class from both groups have equal average predicted probability scores. 

* **Balance for negative class** : This is the flipped version of the previous definition.

#### Similarity based measures

* **Causal discrimination** : Satisfying this definition means that if all the attributes except the *protected attribute* are the same, then we should get the same predicted outcomes across both groups.

* **Fairness through unawareness** : This definition is essentially the same as the previous one, **except** that we don't include the *protected attributes* in making the decisions.

* **Fairness through awareness** : Expanding the previous two definitions, similar subjects should have similar classification. 

#### Causal Reasoning

**What are causal graphs?**

They are basically a way to map causal (cause-effect) reasoning and expressing them as nodes and edges helps to understand how one thing influences another.

**What is a proxy attribute?**

Alright, so this is a big one, we often talk about this in the discussions about fairness and bias. 
In the context of a causal graph, it is an attribute that can be used to derive the values in another attribute. *C'est tout!* (Translation: That's all!)

* **Counterfactual fairness** : If the predicted outcome in the graph is not dependent on any of the descendants of the protected attribute.

**What is a resolving attribute?**

An attribute that is influenced by the protected attribute but in a non-discriminatory way.

* **No unresolved discrimination** : If the only paths from the protected attributes to the predicted outcome in the causal graph are through a resolving attribute, then we satisfy this definition.

* **No proxy discrimination** : We satisfy this definition if there is no path from the protected attribute to the predicted outcome that is blocked by a proxy attribute.

* **Fair inference** : We classify the different paths from the protected attribute to the predicted outcome as legitimiate or illegitimate. Some attributes even if they are proxies might be considered legitimate in making a prediction and hence the path could be classified as legitimate. We satisfy this definition then if there are no illegitimate paths in the causal graph.

*For the above 3 definitions, I strongly recommend looking at the graphic in the paper and then working through the definition description in the paper as they are slightly complicated and require a couple of pass-throughs to make sense of them.*

### Conclusion

* One of the things to keep in mind about the statistical definition is that even though they are easy to measure, we need to have verified, measured outcomes, if those are not available there is a bit of a problem. That is, even though we have a certain distribution for the training data, there is **no guarantee** that it holds for the real-world data on which the system will operate.
* The causal definitions and similarity based metrics require expert input and are hence subject to expert bias. 
* For some definitions like *fairness through unawareness* it requires that we are able to find individuals who differ in some attributes but are identical in others. This is not always (in fact quite rarely!) possible in the real-world and hence limit the viability of these approaches. 

## What does this mean for Actionable AI Ethics?

* I believe that just having a basic awareness of the various definitions of fairness is a great starting point. 
* From a practical standpoint, it is important to know when a certain product or service is deemed to be fair and what can be done in the case that are competing definitions that might be applicable.
* My takeaway from this paper is that the involvement of domain experts is crucial in selecting the right definition of fairness.
* It is also important to be transparent with the users of the system on which definitions of fairness you are utilizing and what the shortcomings of that are.

## Questions I am exploring

**If you have answers to any of these questions, please [tweet](https://twitter.com/actionable_ai/status/1321332124490911744?s=20) and let me know!**

1. Why is it that there are no single females in the dataset? 
2. What are some other datasets that are similar to this that can be used for comparing fairness Definitions? 
3. Is the binary good or bad credit decision sufficient or should there be more graduations for involving a human in the loop? 
4. What are some classes of basic definitions that the policy makers are familiar with? Does the plethora of definitions make it hard for them to make comparisons? 
5. What would be required to get to a more standardized taxonomy?
6. Is there a simple way to communicate the confusion matrix to non-technical audiences? 
7. What constitutes a minor difference to assign a fair outcome? Example of the difference between the male and female case is 0.03 in conditional statistical parity and that's assigned as the same for practical purposes 
8. Given the differences across various definitions, should we require the computation of all for the classification work so that people can make decisions for themselves?
9. What about intersectionality and people who are non-binary or genderfluid? Since that data isn't captured here, there might be over- or underestimation in the results. 

## Potential further reading

A list of papers that I think might be interesting related to this paper. 

* [The Measure and Mismeasure of Fairness: A Critical Review of Fair Machine Learning](https://arxiv.org/abs/1808.00023)
* [Measuring the Biases that Matter: The Ethical and Casual Foundations for Measures of Fairness in Algorithms](https://dl.acm.org/doi/abs/10.1145/3287560.3287573)
* [Fairness Metrics: A Comparative Analysis](https://arxiv.org/abs/2001.07864)

*Please note that this is a wish list of sorts and I haven't read through the papers listed here unless specified otherwise (if I have read them, there will be a link from the entry to the page for that.)*

## Twitter discussion

I'll write back here with interesting points that surface from the Twitter discussion. 

*If you have comments and would like to discuss more, please leave a [tweet here](https://twitter.com/actionable_ai/status/1321332124490911744?s=20).*

### Sign up for the newsletter

<iframe src="https://actionableaiethics.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

To stay up-to-date with the latest content in terms of what I am reading and thinking about, please subscribe to the [Actionable AI Ethics newsletter](https://actionableaiethics.substack.com)

### Support me with a coffee

If you enjoy the content on this page, you can support my work by [buying me a coffee](https://buymeacoffee.com/abhishekgupta)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abhishekgupta" data-color="#FF5F5F" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>