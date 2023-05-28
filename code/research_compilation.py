import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from misc import update_rc


def main():
	# load data
	df = pd.read_excel(os.path.join('data', 'paper_count.ods'))

	# visualize
	update_rc()
	cs = sns.color_palette('rocket', 4)
	fig, ax = plt.subplots()
	ax.plot(df['year'], df['epidemiological'], 'o-',
			markevery=10, c=cs[0], lw=3,
			label='epidemiological')
	ax.plot(df['year'], df['review'], '^--',
			markevery=10, c=cs[1], lw=3,
			label='review')
	ax.plot(df['year'], df['experimental'], 's-.',
			markevery=10, c=cs[2], lw=3,
			label='experimental')
	ax.plot(df['year'], df['dosimetric'], 'd:',
			markevery=10, c=cs[3], lw=3,
			label='dosimetric')
	ax.set(xlabel='year',
			ylabel='number of studies',
			xticks=[1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020],
			xticklabels=[1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020],
			yticks=[0, 125, 250, 375],
			yticklabels=[0, 125, 250, 375],)
	ax.legend(loc='best', title='studies', frameon=False)
	sns.despine()
	plt.show()
	# fig.savefig(os.path.join('figures', 'research_compilation.pdf'),
	#             bbox_inches='tight')
	

if __name__ == '__main__':
        main()
