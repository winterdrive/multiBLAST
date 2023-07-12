import os

from Bio.Blast import NCBIWWW, NCBIXML

"""
需要篩選hit的長度，不然會拉到chromosome
"""


def parsing_the_best_blast_xml_result(input_file_path: str):
    with open(input_file_path, "r") as blast_result:
        E_VALUE_THRESH = 1e-3
        count = 0
        best_hit = None
        best_hit_score = 0
        for record in NCBIXML.parse(blast_result):
            for alignment in record.alignments:
                for hsp in alignment.hsps:
                    count += 1
                    if hsp.expect < E_VALUE_THRESH and hsp.score > best_hit_score:
                        if alignment.length < 1000:
                            best_hit = alignment
                            best_hit_score = hsp.score
        # print(f"There are {count} similar sequences in Blast output")
        # print("The best hit is:" + best_hit.title)
    return best_hit.title

def parsing_all_blast_xml_result(input_file_path: str):
    result_set = set()
    with open(input_file_path, "r") as blast_result:
        count = 0
        for record in NCBIXML.parse(blast_result):
            for alignment in record.alignments:
                for hsp in alignment.hsps:
                    count += 1
                    if alignment.length < 1000:
                        result_set.add(alignment.title.split("|")[3])
        # print(f"There are {count} similar sequences in Blast output")
    return result_set

load_file_dir_r1 = "/multiBLAST/data/output/r1/"

rawFilesR1 = os.listdir(load_file_dir_r1)

result_set = set()

for blast_xml_file in rawFilesR1:

    # best hit collection
    try:
        temp_seq_title = parsing_the_best_blast_xml_result(load_file_dir_r1 + blast_xml_file)
        result_set.add(temp_seq_title.split("|")[3])
    except:
        print("Error in parsing blast xml file:", blast_xml_file)

    # # all hit collection
    # try:
    #     temp_seq_title = parsing_all_blast_xml_result(load_file_dir_r1 + blast_xml_file)
    #     result_set.update(temp_seq_title)
    # except:
    #     print("Error in parsing blast xml file:", blast_xml_file)

print(result_set)
print(len(result_set))


# gi|1662973096|gb|MK052490.1| Dennstaedtia scabra voucher YYH12150 tRNA-Leu (trnL) gene and trnL-trnF intergenic spacer, partial sequence; chloroplast


# 整理好序列，太大量的話丟這裡搜尋
# https://zhuanlan.zhihu.com/p/370078654