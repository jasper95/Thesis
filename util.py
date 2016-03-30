from collections import Counter


def fScore(pred, truth):
    counts = Counter(zip(pred, truth))
    true_pos = float(counts[1.0, 1.0])
    false_pos = float(counts[0.0, 1.0])
    true_neg = float(counts[1.0, 0.0])
    false_neg = float(counts[0.0, 0.0])
    print('true_pos', true_pos, 'false_pos', false_pos, 'true_neg', true_neg,
          'false_neg', false_neg)
    recall = float(true_pos)/float(true_pos+true_neg)
    precision = true_pos/float(true_pos+false_pos)
    print ('precision: ', precision, 'recall:', recall)
    return 2.0/((1.0/recall) + (1.0/precision))