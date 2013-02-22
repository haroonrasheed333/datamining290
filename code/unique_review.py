from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

import re

WORD_RE = re.compile(r"[\w']+")

class UniqueReview(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def extract_words(self, _, record):
        if record['type'] == 'review':
            for word in WORD_RE.findall(record['text']):
                yield [word.lower(), record['review_id']]

    def count_reviews(self, word, review_ids):
        unique_reviews = set(review_ids)  # set() uniques an iterator
        if len(unique_reviews) == 1:
            for rev in unique_reviews:
                yield [rev,1]

    def count_unique_words(self, review_id, unique_word_counts):
        yield [review_id, sum(unique_word_counts)]

    def aggregate_max(self, review_id, unique_word_count):
        yield ["MAX",[unique_word_count,review_id]]

    def select_max(self, stat, count_review_ids):
        yield["RESULT",max(count_review_ids)]

    def steps(self):
        return [self.mr(self.extract_words, self.count_reviews),
                self.mr(reducer=self.count_unique_words),
                self.mr(self.aggregate_max, self.select_max)]

if __name__ == '__main__':
    UniqueReview.run()