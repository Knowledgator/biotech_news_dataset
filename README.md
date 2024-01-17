**📚 Multi-label events-focused biotech news classification dataset**

### Key aspects
* Event extraction;
* [Multi-label classification](https://en.wikipedia.org/wiki/Multi-label_classification);
* Biotech news domain;
* 31 classes;
* 3140 total number of examples;

### Motivation

Text classification is a widespread task and a foundational step in numerous information extraction pipelines. However, a notable challenge in current NLP research lies in the oversimplification of benchmarking datasets, which predominantly focus on rudimentary tasks such as topic classification or sentiment analysis. 

This dataset is specifically curated to address the limitations of existing benchmarks by incorporating rich and complex content derived from the biotech news domain. It encompasses diverse biotech news articles consisting of various events, offering a more nuanced perspective on information extraction challenges. 

A distinctive feature of this dataset is its emphasis on not only identifying the overarching theme but also extracting information about the target companies associated with the news. This dual-layered approach enhances the dataset's utility for applications that require a deeper understanding of the relationships between events, companies, and the biotech industry as a whole.

### Classes

The dataset consists of **31** classes, including None values.

* event organization - organizing or participating in an event like a conference, exhibition, etc.
* executive statement - a statement or quote from an executive of a company.
* regulatory approval - getting approval from regulatory bodies for products, services, trials, etc.
* hiring - announcing new hires or appointments at the company.
* foundation - establishing a new charitable foundation.
* closing - shutting down a facility/office/division or ceasing an initiative.
* partnerships & alliances - forming partnerships or strategic alliances with other companies.
* expanding industry - expanding into new industries or markets.
* new initiatives or programs - announcing new initiatives, programs, or campaigns.
* m&a - mergers, acquisitions, or divestitures.
* None - no label.
* service & product providing - launching or expanding products or services.
* event organisation - organizing or participating in an event.
* new initiatives & programs - announcing new initiatives or programs.
* subsidiary establishment - establishing a new subsidiary company.
* product launching & presentation - launching or unveiling a new product.
* product updates - announcing updates or new versions of existing products.
* executive appointment - appointing a new executive.
* alliance & partnership - forming an alliance or partnership.
* ipo exit - having an initial public offering or acquisition exit.
* article publication - publishing an article.
* clinical trial sponsorship - Sponsoring or participating in a clinical trial.
* company description - describing or profiling the company.
* investment in public company - making an investment in a public company.
* other - other events that don't fit into defined categories.
* expanding geography - expanding into new geographical areas.
* participation in an event - participating in an industry event, conference, etc.
* support & philanthropy - philanthropic activities or donations.
* department establishment - establishing a new department or division.
* funding round - raising a new round of funding.
* patent publication - publication of a new patent filing.

### Benchmark
We trained various models with binary-cross entropy loss and evaluated them on the test set.

| Model           | Accuracy | F1    | Precision | Recall |
|-----------------|----------|-------|-----------|--------|
| DeBERTa-small   | 96.58    | 67.69 | 74.18     | 62.19  |
| DeBERTa-base    | 96.60    | 67.55 | 74.81     | 61.58  |
| DeBERTa-large   | 96.99    | 74.07 | 73.46     | 74.69  |
| SciBERT-uncased | 96.57    | 68.07 | 73.07     | 63.71  |
| Flan-T5-base    | 96.85    | 71.10 | 75.71     | 67.07  |

### Recommended reading:
- Check the general overview of the dataset on Medium - [Finally, a decent multi-label classification benchmark is created: a prominent zero-shot dataset.](https://medium.com/p/4d90c9e1c718)

- Try to train your own model on the datset - [ Multi-Label Classification Model From Scratch: Step-by-Step Tutorial ](https://huggingface.co/blog/Valerii-Knowledgator/multi-label-classification)

### Feedback
We value your input! Share your feedback and suggestions to help us improve our models and datasets.
Fill out the feedback [form](https://forms.gle/5CPFFuLzNWznjcpL7)

### Join Our Discord
Connect with our community on Discord for news, support, and discussion about our models and datasets.
Join [Discord](https://discord.gg/mfZfwjpB)
