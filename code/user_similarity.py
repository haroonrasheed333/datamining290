from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from itertools import combinations

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    ###
    # TODO: write the functions needed to
    # 1) find potential matches,
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##/

    def user_business(self, _, record):
        if record['type'] == 'review':
            yield [record['user_id'], record['business_id']]

    def user_businesses(self, userid, businessid):
        business_id = set(businessid)  # set() uniques an iterator
        yield ["Comb", [userid, list(business_id)]]

    def similarity(self, stat, usbslist):
        k = list(usbslist)
        j = combinations(k, 2)
        for line in list(j):
            num = len(set(line[0][1]) & set(line[1][1]))
            den = len(set(line[0][1]) | set(line[1][1]))
            sim = num / (float(den))
            if sim>=0.5:
                yield[[line[0][0],line[1][0]],sim]

    def steps(self):
        return [self.mr(self.user_business, self.user_businesses),
                self.mr(reducer=self.similarity)]


if __name__ == '__main__':
    UserSimilarity.run()
