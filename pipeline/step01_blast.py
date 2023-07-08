# 關閉driver視窗的三種方法
# https://stackoverflow.com/questions/15067107/difference-between-webdriver-dispose-close-and-quit

# -*- coding: utf-8 -*-
import os
import queue
import time

from Bio.Blast import NCBIWWW, NCBIXML


def fasta_seq_reader(fasta_file_path):
    with open(fasta_file_path, "r") as file:
        seq = ""
        for line in file:
            if line[0] == ">":
                if seq != "":
                    # yield seq
                    return seq
                seq = ""
            else:
                seq += line.strip()
        # yield seq
        return seq


def blast_by_NCBIWWW(input_file_path: str, output_file_path: str):
    result_status = False
    start_time = time.localtime()
    blast_result = NCBIWWW.qblast("blastn", "nt", fasta_seq_reader(input_file_path))
    with open(output_file_path, "w") as out_handle:
        out_handle.write(blast_result.read())
    # print(blast_result.read()) # 這個是讀取結果的原始碼，用xml紀錄
    with open(output_file_path, "r") as result_text:
        print(result_text.readline())
        if len(result_text.readline()) > 0: # 檢查第一行要有東西
            result_status = True
    end_time = time.localtime()
    print("total blast time:", time.mktime(end_time) - time.mktime(start_time))
    return result_status


def execute_the_queue(message_queue: queue.Queue, load_file_dir: str, save_file_dir: str):
    # Process elements in the queue
    while not message_queue.empty():
        print("Queue size:", message_queue.qsize())
        element = message_queue.get()

        # Process the element
        success = blast_by_NCBIWWW(load_file_dir + element, save_file_dir + element)

        if not success:
            print("Adding element back to the queue:", element)
            message_queue.put(element)

    print("All elements processed")


def parsing_the_best_blast_xml_result(input_file_path: str):
    # parsing blast result from xml file by biopython NCBIXML
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
                        best_hit = alignment
                        best_hit_score = hsp.score
                        # print("****Alignment****")
                        # print("sequence:", alignment.title)
                        # print("length:", alignment.length)
                        # print("e value:", hsp.expect)
                        # print(hsp.query[0:75] + "...")
                        # print(hsp.match[0:75] + "...")
                        # print(hsp.sbjct[0:75] + "...")
        print(f"There are {count} similar sequences in Blast output")
        print("The best hit is:" + best_hit.title)
    return best_hit.title


load_file_dir_r1 = "/PowerBarcoder/data/result/202307071741/trnLF_result/denoiseResult/r1/"  # load_file_dir+"/"+rawFilesR1[0]
load_file_dir_r2 = "/PowerBarcoder/data/result/202307071741/trnLF_result/denoiseResult/r2/"  # load_file_dir+"/"+rawFilesR2[0]
save_file_dir_r1 = "/multiBLAST/data/output/r1/"  # save_file_dir+"/"+rawFilesR1[0]
save_file_dir_r2 = "/multiBLAST/data/output/r2/"  # save_file_dir+"/"+rawFilesR2[0]

# 取得所有檔案與子目錄名稱
rawFilesR1 = os.listdir(load_file_dir_r1)
rawFilesR2 = os.listdir(load_file_dir_r2)

# Create a queue to hold the elements
message_queue_r1 = queue.Queue()
message_queue_r2 = queue.Queue()

# Add elements to the queue
for i in rawFilesR1:
    message_queue_r1.put(i)
for i in rawFilesR1:
    message_queue_r2.put(i)

# Function to process an element
# Here is "blast_by_NCBIWWW()"

execute_the_queue(message_queue_r1, load_file_dir_r1, save_file_dir_r1)
execute_the_queue(message_queue_r2, load_file_dir_r2, save_file_dir_r2)

# TODO: parsing the best result in each XML file