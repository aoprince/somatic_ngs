#parse files

import pandas as pd
def parse(file):
    df = pd.read_csv(file, sep="\t")
    return df

dups = parse("multiqc_picard_dups.txt")
HsMetrics = parse("multiqc_picard_HsMetrics.txt")
flagstat = parse("multiqc_samtools_flagstat.txt")
fastQC = parse("multiqc_fastqc.txt")



import matplotlib as mpl
import matplotlib.pyplot as plt

#plots graphs from input of parsed dataframes

def plot(dataframe, a, b, filename):
    dataframe.plot(x = a, y = b, kind ="scatter")
    return plt.savefig("./" + filename + "_plot.png")
#df.plot(x="Sample", y="PERCENT_DUPLICATION", kind="scatter")

plot(dataframe = dups, a = "Sample", b = "PERCENT_DUPLICATION", filename= "multiqc_picard_dups" )

plot(dataframe= flagstat, a = "Sample", b = "total_failed", filename= "multiqc_samtools_flagstat")

plot(dataframe= fastQC, a= "Sample", b = "Sequences flagged as poor quality", filename= "multiqc_fastqc")

plot(dataframe= HsMetrics, a="Sample", b = "ON_TARGET_BASES", filename= "multiqc_picard_HsMetrics" )

#plt.show()

#plt.savefig('./test_plot.png')