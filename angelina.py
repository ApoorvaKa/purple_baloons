import pandas as pd

def highlight_first(x):
    '''
    highlight the last row in a Series BOLD.
    '''
    return ['font-weight: bold' if v == 0 and v == x.iloc[0] else '' for v in x]

fold_changes = [.3, .6, .9, .1, .4]
print(fold_changes)
avg_fold_changes = sum(fold_changes)/len(fold_changes)
fold_changes.append(avg_fold_changes)

std_dev = [.1, .2, .3, .4, .5]
std_dev.append("--")

df = { 'Trial': ["Trial 1", "Trial 2", "Trial 3", "Trial 4", "Trial 5", "Average"],
       'Fold Change': fold_changes,
       'Standard Deviation': std_dev
    }
df = pd.DataFrame(df)


df.style.apply(highlight_first)

html = df.to_html(index=False, justify="left")

# write html to file
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()