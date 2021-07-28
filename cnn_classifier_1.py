import tensorflow as tf
import tensorflow_datasets as tfdf

dataset, info = tfds.load("imdb_reviews/subwords8k", with_info=True, as_supervised=True)

train_dataset, test_dataset, dataset["train"], dataset["test"]
