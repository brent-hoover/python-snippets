"""ClusterMetrics: a metric cluster**** of cluster metrics!"""
from __future__ import division
from math import sqrt
from Probably import variation_of_information as vi, \
    mutual_information as mi, log2, conditional_entropy_X_Given_Y, \
    conditional_entropy_Y_Given_X, entropy_of_multinomial
from waterworks.Tools import ondemand
from PrecRec import precision_recall_f, fscore

# TODO switch to waterworks.Dictionaries.TwoLevelCounterDict
from AIMA import DefaultDict

class ConfusionMatrix(object):
    def __init__(self):
        """Creates an empty confusion matrix.  You'll need to call the add()
        method to populate it."""
        # test : { gold : count }
        self.by_test = DefaultDict(DefaultDict(0))
        self._all_gold = None

    def __repr__(self):
        return "<ConfusionMatrix (%s test tags, %s gold tags)>" % \
            (len(self.all_test), len(self.all_gold))

    def all_gold():
        doc = "Set of all gold tags.  Calculated on demand."
        def fget(self):
            if self._all_gold is None:
                self._all_gold = set()
                for gold_dict in self.by_test.values():
                    self._all_gold.update(gold_dict.keys())
            return self._all_gold
        return locals()
    all_gold = property(**all_gold())

    def all_test():
        doc = "Set of all test tags."
        def fget(self):
            return self.by_test.keys()
        return locals()
    all_test = property(**all_test())

    def gold_sizes():
        doc = "Mapping from gold cluster label to size. Calculated on demand."
        def fget(self):
            if self._gold_sizes is None:
                self._gold_sizes = DefaultDict(0)
                for gold_dict in self.by_test.values():
                    for gold,size in gold_dict.items():
                        self._gold_sizes[gold] += size
            return self._gold_sizes
        return locals()
    gold_sizes = property(**gold_sizes())

    def add(self, gold, test, count=1):
        """Add count joint occurrences of gold and test."""
        self.by_test[test][gold] += count
        # invalidate cache
        self._all_gold = None
        self._gold_sizes = None
    def as_confusion_items(self):
        """Yields ((gold, test), count) items."""
        for test, gold_dict in self.by_test.items():
            for gold, count in gold_dict.items():
                yield (gold, test), count
    def as_confusion_matrix(self, mapping_method='one_to_one_optimal_mapping'):
        """Returns this as a confusion matrix (list of lists)."""
        all_test = set()
        all_gold = set()
        for (gold, test), count in self.as_confusion_items():
            all_test.add(test)
            all_gold.add(gold)
        all_gold = sorted(all_gold)

        mapping_method = getattr(self, mapping_method)
        mapping = mapping_method()
        def sorter(test):
            key = mapping.get(test)
            return (key, -self.by_test[test][key])

        all_test = sorted(all_test, key=sorter)
        
        rows = []
        for gold in all_gold:
            row = [self.by_test[test][gold] for test in all_test]
            rows.append(row)

        return rows, all_gold, all_test

    def as_latex_confusion_matrix(self, normalize='gold'):
        """Returns the table as a LaTeX formatted confusion matrix.
        You will need to include the LaTeX package colortbl:

            \usepackage{colortbl}
        """
        assert normalize == 'gold', "Only supports gold normalization for now."

        from TeXTable import make_tex_bitmap
        rows, gold_labels, test_labels = self.as_confusion_matrix()

        header = [''] + test_labels
        def escape_label(label):
            label = label.replace('$', r'\$')
            label = label.replace('#', r'\#')
            label = label.replace('%', r'\%')
            return label

        def process_row(row, label):
            total = sum(row)
            return [escape_label(label)] + [1 - (cell / total) for cell in row]
        rows = [header] + [process_row(row, gold_label)
            for gold_label, row in zip(gold_labels, rows)]
        return make_tex_bitmap(rows, has_header=True)

    def pylab_pcolor(self, mapping_method='one_to_one_greedy_mapping',
                     normalize='gold'):

        assert normalize in ('total', 'gold', 'test')

        import pylab, numpy
        rows, gold_labels, test_labels = \
            self.as_confusion_matrix(mapping_method=mapping_method)

        def normalize_row_by_total(row):
            total = self.total_points
            return [1 - (cell / total) for cell in row]

        def normalize_row_by_row(row):
            total = sum(row)
            return [1 - (cell / total) for cell in row]

        if normalize == 'total':
            normalize = normalize_row_by_total
        elif normalize == 'gold':
            normalize = normalize_row_by_row
        else: # test
            from AIMA import vector_add
            column_totals = reduce(vector_add, rows)
            def normalize(row):
                return [1 - (cell / total) 
                    for cell, total in zip(row, column_totals)]

        rows = [normalize(row)
            for gold_label, row in zip(gold_labels, rows)]
        rows = numpy.array(rows)
        pylab.pcolor(rows)

    def one_to_one_greedy_mapping(self):
        """Computes the one-to-one greedy mapping.  The mapping returned
        is a dictionary of {test : gold}"""
        one_to_one_mapping = {} # test : gold
        confusion_by_count = sorted((-count, (gold, test))
            for (gold, test), count in self.as_confusion_items())

        for count, (gold, test) in confusion_by_count:
            if test in one_to_one_mapping.keys() or \
               gold in one_to_one_mapping.values():
                continue
            else:
                one_to_one_mapping[test] = gold
        return one_to_one_mapping
    def one_to_one_greedy(self, verbose=True):
        """Computes and evaluates the one-to-one greedy mapping.
        Returns a score between 0.0 and 1.0 (higher is better)."""
        return self.eval_mapping(self.one_to_one_greedy_mapping(),
                                 verbose=verbose)
    def one_to_one_optimal_mapping(self):
        """Computes the one-to-one optimal mapping using the Hungarian 
        algorithm.  The mapping returned is a dictionary of {test : gold}"""
        from cookbook.hungarian_method import hungarian_method
        all_gold = set()
        for (gold, test), count in self.as_confusion_items():
            all_gold.add(gold)
        all_gold = sorted(list(all_gold))
        neg_confusion_array = []
        all_test = []
        for test, gold_counts in self.by_test.items():
            counts = [-gold_counts.get(gold, 0) for gold in all_gold]
            neg_confusion_array.append(counts)
            all_test.append(test)

        for x in range(len(all_gold) - len(all_test)):
            neg_confusion_array.append([0] * len(all_gold))

        mapping = hungarian_method(neg_confusion_array)
        mapping_dict = {}
        for test_index, gold_index in mapping:
            try:
                test = all_test[test_index]
            except IndexError:
                continue
            mapping_dict[test] = all_gold[gold_index]
        return mapping_dict
    def one_to_one_optimal(self, verbose=True):
        """Computes and evaluates the one-to-one optimal mapping.
        Returns a score between 0.0 and 1.0 (higher is better)."""
        return self.eval_mapping(self.one_to_one_optimal_mapping(),
                                 verbose=verbose)
    def many_to_one_mapping(self):
        """Computes the many-to-one mapping.  The mapping returned is
        a dictionary of {test : gold}"""
        many_to_one_mapping = {} # test tag : gold tag
        for test, gold_counts in self.by_test.items():
            by_count = ((v, k) for k, v in gold_counts.items())
            top_count, top = max(by_count)
            many_to_one_mapping[test] = top
        return many_to_one_mapping
    def many_to_one(self, verbose=True):
        """Computes and evaluates the many-to-one mapping.  Returns a
        score between 0.0 and 1.0 (higher is better)."""
        return self.eval_mapping(self.many_to_one_mapping(),
                                 verbose=verbose)

    def eval_mapping(self, mapping, verbose=True):
        """Evaluates a mapping (dictionary of assignments between test and
        gold).  Returns a score between 0.0 and 1.0 (higher is better).
        
        If verbose is true, the mapping will be printed before being
        evaluated."""
        if verbose:
            print "Mapping", mapping
        right = 0
        wrong = 0
        for (gold, test), count in self.as_confusion_items():
            if mapping.get(test) == gold:
                right += count
            else:
                wrong += count
        return right, wrong, right / (right + wrong)
    def variation_of_information(self):
        """Calculates the variation of information between the test and gold.  
        Lower is better, minimum is 0.0"""
        return vi(dict(self.as_confusion_items()))

    def variation_of_information_upper_bound(self):
        """Calculates the upper bound on variation of information between the 
        test and gold.  VI(C, C') <= log2(n) where n is the total number of
        data point."""
        return log2(self.total_points)

    def normalized_vi(self):
        """Calculates NVI (Reichart and Rappoport '09), which is
        VI/H(C), variation of information normalized by the entropy of
        the true clustering. This metric has value 0 for perfect
        clusterings and 1 for the single-cluster clustering;
        'reasonable' clusterings have scores in between."""
        hc = entropy_of_multinomial(self.gold_sizes.values())
        if hc == 0:
            return 0
        return self.variation_of_information() / hc

    def mutual_information(self):
        """Calculates the mutual information between the test and gold.  
        Higher is better, minimum is 0.0"""
        return mi(dict(self.as_confusion_items()))

    def normalized_mutual_information(self):
        """Normalized mutual information (Strehl and Ghosh JMLR '02
        "Cluster Ensembles"), eq 2: mutual information normalized by
        the square root of the product of entropies. The value is
        between 0 and 1, and is 1 for identical clusterings."""
        denom = (sqrt(
            entropy_of_multinomial(self.gold_sizes.values()) *
            entropy_of_multinomial([sum(table.values())
                                    for table in self.by_test.values()])))
        if denom == 0:
            if entropy_of_multinomial(self.gold_sizes.values()) == 0:
                #gold clustering is entirely uninformative
                #so anything we do is good
                return 1
            else:
                #induced clustering is entirely uninformative
                return 0

        return self.mutual_information() / denom

    def v_measure(self, beta=1):
        """Computes Rosenberg and Hirschberg's V-measure (EMNLP '07),
        which ranges between 0 and 1 (1 is best). The beta parameter
        can be used to weigh homogeneity or completeness; the default
        is balanced harmonic mean, beta > 1 favors homogeneity."""
        h_c = entropy_of_multinomial(self.gold_sizes.values())
        h_k = entropy_of_multinomial(
            [sum(table.values()) for table in self.by_test.values()])

        if h_c == 0:
            homo = 1
        else:
            h_c_given_k = self.conditional_entropy_gold_given_test()

            homo = 1 - h_c_given_k / h_c

        if h_k == 0:
            comp = 1
        else:
            h_k_given_c = conditional_entropy_Y_Given_X(
                dict(self.as_confusion_items()))

            comp = 1 - h_k_given_c / h_k

        return fscore(homo, comp, beta) #computes the harmonic mean

    def v_beta(self):
        """Computes the v-beta metric, a variant of V-measure, given
        in Vlachos, Korhonen and Ghahramani (EACL '09), section
        3. This is equal to the V-measure where beta is set to
        |K|/|C|, the ratio of number of predicted clusters to number
        of true clusters, and attempts to correct for V's reported
        bias in favor of solutions with many clusters."""
        #note that our harmonic mean is (1 + b**2) * h * c
        #while eq 3 in Vlachos et al gives (1 + b)... therefore
        #we take a square root here to get equivalent answers
        b = len(self.all_test) / len(self.all_gold)
        return self.v_measure(beta=sqrt(b))

    def conditional_entropy_gold_given_test(self):
        """Calculates the conditional entropy of the gold given the test.  
        lower is better, minimum is 0.0"""
        return conditional_entropy_X_Given_Y(dict(self.as_confusion_items()))

    def jaccard_index(self):
        """Calculates the Jaccard index between test and gold, as defined
        in Meila "Comparing Clusterings", eq 7.
        Value is between 0 and 1, and is 1 for identical clusterings."""
        N00,N11,N01,N10 = self.pairwise_statistics
        return N11/(N11 + N01 + N10)

    def mirkin_metric(self):
        """Calculates the Mirkin metric (a scaled form of the Rand index)
        as defined in Meila "Comparing Clusterings", eq. 9.
        Value is 0 for identical clusterings and positive otherwise."""
        N00,N11,N01,N10 = self.pairwise_statistics
        return 2 * (N01 + N10)

    def rand_index(self):
        """Calculates the (unadjusted) Rand index, which is the
        classification accuracy of the clustering over same/different edges,
        as defined in Meila "Comparing Clusterings", eq. 5.
        Value is 1 for identical clusterings and always greater than 0,
        tending to be close to 1 in practice."""
        N00,N11,N01,N10 = self.pairwise_statistics
        return (N11 + N00) / (N00 + N11 + N01 + N10)

    def prec_rec(self):
        """Calculates the classification precision, recall and F-score
        over edges, with respect to the same-cluster class."""
        N00,N11,N01,N10 = self.pairwise_statistics

        return precision_recall_f(N11, (N11 + N10), (N11 + N01))

    def micro_average_f(self):
        """Evaluates the micro-average f-score. Micro-averaging
        averages f-score for each cluster in the gold transcript,
        weighted by the cluster size."""
        res = 0
        total = sum(self.gold_sizes.values())

        for gold in self.all_gold:
            fs = [self.eval_cluster_f(gold, test)[0][2]
                  for test in self.all_test]
            maxF = max(fs)
            res += maxF * self.gold_sizes[gold] / total
        return res

    def macro_average_f(self):
        """Evaluates the macro-average f-score. Macro-averaging adds
        number matched and cluster sizes for each pair of clusters,
        then takes the f-score at the end. Clusters are matched to
        maximize overlap, though this does not necessarily maximize
        the metric itself."""
        match = 0
        prop = 0
        true = 0
        for gold in self.all_gold:
            counts = [self.eval_cluster_f(gold, test)[1]
                      for test in self.all_test]
            best = max(counts, key=lambda x: x[0]) #matched
            match += best[0]
            true += best[1]
            prop += best[2]
        (p,r,f) = precision_recall_f(match, true, prop)
        return f

    def eval_cluster_f(self, gold_cluster, test_cluster):
        """Computes the clustering f-score of the gold and test cluster,
        where prec = |overlap| / |test|, rec = |overlap| / |gold|.
        Returns two tuples of values: the first is (prec, rec, f)
        , and the second is (|overlap|, |gold|, |test|)."""
        matched = self.by_test[test_cluster][gold_cluster]
        proposed = sum(self.by_test[test_cluster].values())
        true = self.gold_sizes[gold_cluster]
        (p,r,f) = precision_recall_f(matched, true, proposed)
        return (p, r, f), (matched, true, proposed)

    def _total_points(self):
        total = sum(count for (gold, test), count in self.as_confusion_items())
        return total
    total_points = ondemand(_total_points)

    def _pairwise_statistics(self):
        items = []
        for (gold, test), count in self.as_confusion_items():
            items.extend((((gold, test),) * count))

        N00 = 0
        N01 = 0
        N10 = 0
        N11 = 0
        for index1, i1 in enumerate(items):
            for index2, i2 in enumerate(items):
                if index2 <= index1:
                    continue
                # print index1, index2, i1, i2
                if i1[0] != i2[0] and i1[1] != i2[1]:
                    N00 += 1
                if i1 == i2:
                    N11 += 1
                if i1[0] == i2[0] and i1[1] != i2[1]:
                    N10 += 1
                if i1[0] != i2[0] and i1[1] == i2[1]:
                    N01 += 1

        return N00, N11, N01, N10
    pairwise_statistics = ondemand(_pairwise_statistics)

if __name__ == "__main__":
    cm = ConfusionMatrix()
    cm.add('B', 1, 0)
    cm.add('A', 1, 9)
    cm.add('B', 2, 9)
    cm.add('A', 2, 10)
    print "gold tags", cm.all_gold
    print "test tags", cm.all_test
    print list(cm.as_confusion_items())
    print "121g", cm.one_to_one_greedy()
    print "m21", cm.eval_mapping(cm.many_to_one_mapping())
    print "vi", cm.variation_of_information()
    print "mi", cm.mutual_information()
    print "nvi", cm.normalized_vi()
    print "121o", cm.one_to_one_optimal_mapping()
    print "121o", cm.one_to_one_optimal()
    print "edge-f", cm.prec_rec()
    print "micro-f", cm.micro_average_f()
    print "macro-f", cm.macro_average_f()
    print "nmi", cm.normalized_mutual_information()
    print "vm", cm.v_measure()
    print "beta vm", cm.v_beta()

    #verify nvi gets 1 for single-cluster
    cm = ConfusionMatrix()
    cm.add('A', 1, 10)
    cm.add('B', 1, 10)
    vv = cm.normalized_vi()
    assert(vv == 1)

    #verify perfection
    cm = ConfusionMatrix()
    cm.add('A', 1, 10)
    cm.add('B', 2, 10)
    print "121o", cm.one_to_one_optimal()
    print "vi", cm.variation_of_information()
    print "nvi", cm.normalized_vi()
    print "edge-f", cm.prec_rec()
    print "micro-f", cm.micro_average_f()
    print "macro-f", cm.macro_average_f()
    print "nmi", cm.normalized_mutual_information()
    print "vm", cm.v_measure()
    print "beta vm", cm.v_beta()

