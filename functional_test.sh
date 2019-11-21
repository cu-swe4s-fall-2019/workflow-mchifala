test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_gene_counts python get_gene_counts.py GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz MEN1 MEN1_counts.txt
assert_no_stderr
assert_exit_code 0

run test_tissue_samples python get_tissue_samples.py GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt Blood Blood_samples.txt
assert_no_stderr
assert_exit_code 0

run test_tissue_samples python box.py --tissues Blood --genes MEN1 --output_file Blood_MEN1.png
assert_no_stderr
assert_exit_code 0