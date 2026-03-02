---
title: Interpretability

view: masonry
---

We are interested in developing interpretable models. An interpretable model exposes means for identifying the process that leads from an input to a prediction. We are mainly focused on interpretability by design in text classification.

Current topics of interest:

**Selective Rationalization:**\
The process of learning by providing highlights as explanations is denoted as selective rationalization. 
Highlights are a subset of input texts meant to be interpretable by a user and faithfully describe the inference process of a classification model. 
A popular architecture for selective rationalization is the Select-then-Predict Pipeline (SPP): a generator selects the rationale to be fed to a predictor. 
It has been shown that SPP suffers from local minima derived by suboptimal interplay between the generator and predictor, a phenomenon known as interlocking.

**Knowledge Extraction:**\
The process of extracting interpretable knowledge from data-driven processes. 
Our aim is to distill common knowledge from several examples when addressing a downstream task.

<br/>