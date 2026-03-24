%% Normalized scores to 0-1
function normalize_scores = Normalize_scores(scores)

[m,n] = size(scores);
normalize_scores = zeros(m,n);
u = mean(scores);
sd = std(scores);
for i = 1:m
    normalize_scores(i) = (scores(i)-u)/sd;
end