# Workflows
V1.0: The goal of this assignment is to learn the basics of Snakemake workflows.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The following packages were used during the development of this code. Other versions may be supported, but cannot be guaranteed.

- python (version 3.7.0)
- pycodestyle (version 2.5.0)
- matplotlib (version 3.1.1)
- numpy (verstion 1.17.3)

### Installation

The following steps will help you set up the proper environment on your machine. All example commands are entered directly into terminal.

**Installing conda:**

```
cd $HOME
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
. $HOME/miniconda3/etc/profile.d/conda.sh
conda update --yes conda
conda config --add channels bioconda
echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
```

**Creating conda environment:**

```
conda create --yes -n <your_environment>
conda install --yes python=3.7
```

**Activating conda environment:**

```
conda activate <your_environment>
```

**Installing pycodestyle:**

pycodestyle is used to ensure that all .py files adhere to the PEP8 style guidelines.

```
conda install -y pycodestyle
```

**Installing matplotlib:**

matplotlib is used to generate the boxplots of the data.

```
conda install -y pycodestyle
```

**Installing numpy:**

numpy is used during unit testing.

```
conda install -y pycodestyle
```

### Examples

get_gene_counts creates a .txt file of sample ID's and counts for a given gene of interest.

```
python get_gene_counts.py GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz <gene> <gene>_counts.txt
```

get_tissue_samples.py extracts the samples of a particular tissue group and places into a .txt file.

```
python get_tissue_samples.py GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt <tissue> <tissue>_samples.txt
```

box.py makes a series of boxplots for gene expression distribution across a set of genes for a set of tissue groups
```
python box.py --tissues <tissue_list> --genes <gene_list> --output_file <file>.png
```

snakeman runs the workflow stored in Snakefile. See Snakefile for the specific details of the workflow
```
snakemake
```
## Authors

**Michael W. Chifala** - University of Colorado, Boulder, CSCI 7000: Software Engineering for Scientists

## Acknowledgments

* Ryan Layer's CSCI 7000 "Development Environment" document
* Ryan Layer's CSCI 7000 "Continuous Integration with Travis CI" document
* Ryan Layer's CSCI 7000 "Test-Driven Development" document
* Ryan Layer's CSCI 7000 "Using libraries: Matplotlib" document
* Ryan Layer's CSCI 7000 "Workflows" document
* PEP8 Style Guidelines: https://www.python.org/dev/peps/pep-0008/
* ssshtest: https://github.com/ryanlayer/ssshtest
* Github: PurpleBooth/README-Template.md
* Data Files:
    * https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
    * https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
