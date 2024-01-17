import datasets
from datasets import load_dataset
from datasets.tasks import TextClassification

DESCRIPTION = """
Text classification is a widespread task and a foundational step in numerous information extraction pipelines. However, a notable challenge in current NLP research lies in the oversimplification of benchmarking datasets, which predominantly focus on rudimentary tasks such as topic classification or sentiment analysis. 

This dataset is specifically curated to address the limitations of existing benchmarks by incorporating rich and complex content derived from the biotech domain. It encompasses diverse biotech news articles and events, offering a more nuanced perspective on information extraction challenges. Unlike conventional datasets, our collection goes beyond basic categorization, delving into the realm of multi-label classification.

A distinctive feature of this dataset is its emphasis on not only identifying the overarching theme but also extracting information about the target companies associated with the news. This dual-layered approach enhances the dataset's utility for applications that require a deeper understanding of the relationships between events, companies, and the biotech industry as a whole.
"""

labels = ['event organization',
 'executive statement',
 'regulatory approval',
 'hiring',
 'foundation',
 'closing',
 'partnerships & alliances',
 'expanding industry',
 'new initiatives or programs',
 'm&a',
 None,
 'service & product providing',
 'event organisation',
 'new initiatives & programs',
 'subsidiary establishment',
 'product launching & presentation',
 'product updates',
 'executive appointment',
 'alliance & partnership',
 'ipo exit',
 'article publication',
 'clinical trial sponsorship',
 'company description',
 'investment in public company',
 'other',
 'expanding geography',
 'participation in an event',
 'support & philanthropy',
 'department establishment',
 'funding round',
 'patent publication']

TRAIN_DOWNLOAD_URL = "https://huggingface.co/datasets/knowledgator/events_classification_biotech/raw/main/train.csv"
TEST_DOWNLOAD_URL = "https://huggingface.co/datasets/knowledgator/events_classification_biotech/raw/main/test.csv"

class BiotechNews(datasets.GeneratorBasedBuilder):
    """Biotech news events classification dataset."""

    def _info(self):
        return datasets.DatasetInfo(
            description=DESCRIPTION,
            features=datasets.Features(
                {
                    "title": datasets.Value("string"),
                    "content": datasets.Value("string"),
                    "target organization": datasets.Value("string"),
                    "all_labels": datasets.Sequence(datasets.Value("string")),
                    "all_labels_concat": datasets.Value("string"),
                    "label 1": datasets.features.ClassLabel(names=labels),
                    "label 2": datasets.features.ClassLabel(names=labels),
                    "label 3": datasets.features.ClassLabel(names=labels),
                    "label 4": datasets.features.ClassLabel(names=labels),
                    "label 5": datasets.features.ClassLabel(names=labels),

                }
            ),
        )

    def _split_generators(self, dl_manager):
        train_path = dl_manager.download_and_extract(TRAIN_DOWNLOAD_URL)
        test_path = dl_manager.download_and_extract(TEST_DOWNLOAD_URL)
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": train_path}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": test_path}),
        ]

    def get_all_labels(self, curr_labels):
         curr_labels = [lbl for lbl in curr_labels if lbl]
         if not len(curr_labels):
              curr_labels = ['other']
         curr_labels_cat = ', '.join(curr_labels)
         return curr_labels, curr_labels_cat
    
    def _generate_examples(self, filepath):
            csv_reader = load_dataset('csv', data_files=filepath, split='train')
            for example in csv_reader:
                id_, title, content, organization, label1, label2, label3, label4, label5 = example.values()

                curr_labels = (label1, label2, label3, label4, label5)
                curr_labels, curr_labels_cat = self.get_all_labels(curr_labels)

                yield id_, {"title": title, "content": content, "target organization": organization,
                             "all_labels": curr_labels,
                             "all_labels_concat": curr_labels_cat,
                                "label 1": label1, "label 2": label2, "label 3": label3, "label 4": label4,
                                    "label 5": label5}
