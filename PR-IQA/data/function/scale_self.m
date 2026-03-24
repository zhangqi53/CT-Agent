%% scale the score to min_scores-max_scores
function scale_scores = scale_self(scores,max_scores,min_scores)
[m,n] = size(scores);

scale_scores = (max_scores-min_scores) * (scores-min(scores)) / (max(scores)-min(scores));