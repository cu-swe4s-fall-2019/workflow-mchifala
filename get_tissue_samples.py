def main(file, tissue_group, output_file):
    """
    This main function extracts the samples of a particular
    tissue group and places into a .txt file

    Parameters:
    - file(str): The file path to the sample attribute file
    - tissue_group(str): The tissue group of interest. Ex. Blood
    - output_file(str): The .txt file of the results

    """
    out = open(output_file, 'w')

    header = None
    sampid_col = -1
    smts_col = -1

    file = open(file, 'rt')

    for line in file:
        line = line.rstrip().split('\t')
        if header is None:
            header = line
            sampid_col = line.index('SAMPID')
            smts_col = line.index('SMTS')
            continue

        if line[smts_col] == tissue_group:
            out.write(line[sampid_col] + '\n')

    file.close()
    out.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get tissue samples")

    parser.add_argument('file',
                        type=str,
                        help="Sample attribute file")

    parser.add_argument('tissue_group',
                        type=str,
                        help="Tissue group (SMTS)")

    parser.add_argument("output_file",
                        type=str,
                        help="File with sample ids for tissue group")

    args = parser.parse_args()

    main(args.file, args.tissue_group, args.output_file)
