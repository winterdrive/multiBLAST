import os
import queue
import time
import asyncio
import concurrent.futures
from Bio.Blast import NCBIWWW, NCBIXML


def fasta_seq_reader(fasta_file_path):
    with open(fasta_file_path, "r") as file:
        seq = ""
        for line in file:
            if line[0] == ">":
                if seq != "":
                    return seq
                seq = ""
            else:
                seq += line.strip()
        return seq


async def blast_by_NCBIWWW(input_file_path: str, output_file_path: str):
    result_status = False
    start_time = time.localtime()
    loop = asyncio.get_running_loop()
    print("start blast:", input_file_path)
    blast_result = await loop.run_in_executor(None, NCBIWWW.qblast, "blastn", "nt", fasta_seq_reader(input_file_path))
    with open(output_file_path, "w") as out_handle:
        out_handle.write(blast_result.read())
    with open(output_file_path, "r") as result_text:
        print(result_text.readline())
        if len(result_text.readline()) > 0:
            result_status = True
    end_time = time.localtime()
    print("total blast time:", time.mktime(end_time) - time.mktime(start_time))
    return result_status


def execute_the_queue(message_queue: queue.Queue, load_file_dir: str, save_file_dir: str):
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        async def process_element(element):
            return await blast_by_NCBIWWW(load_file_dir + element, save_file_dir + element)

        async def process_queue():
            while not message_queue.empty():
                print("Queue size:", message_queue.qsize())
                element = message_queue.get()
                success = await process_element(element)

                if not success:
                    print("Adding element back to the queue:", element)
                    message_queue.put(element)

        loop.run_until_complete(process_queue())
    print("All elements processed")


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
                        best_hit = alignment
                        best_hit_score = hsp.score
        print(f"There are {count} similar sequences in Blast output")
        print("The best hit is:" + best_hit.title)
    return best_hit.title

def main(load_file_dir, save_file_dir):
    message_queue = queue.Queue()
    rawFiles = os.listdir(load_file_dir)
    xmlFiles = os.listdir(save_file_dir)
    # print("rawFiles:", rawFiles[0])
    # print("xmlFiles:", xmlFiles[0])
    for i in rawFiles:
        # we skip the xml files already been processed by the previous batch
        if i in xmlFiles:
            # print("skip:", i)
            continue
        message_queue.put(i)
    execute_the_queue(message_queue, load_file_dir, save_file_dir)

load_file_dir_r1 = "/PowerBarcoder/data/result/202307071741/trnLF_result/denoiseResult/r1/"
load_file_dir_r2 = "/PowerBarcoder/data/result/202307071741/trnLF_result/denoiseResult/r2/"
load_file_dir_dada2_merged = "/PowerBarcoder/data/result/202307071741/trnLF_result/mergeResult/dada2/merged/"
save_file_dir_r1 = "/multiBLAST/data/output/r1/"
save_file_dir_r2 = "/multiBLAST/data/output/r2/"
save_file_dir_dada2_merged = "/multiBLAST/data/output/dada2_merged/"

main(load_file_dir_r1, save_file_dir_r1)
main(load_file_dir_r2, save_file_dir_r2)
main(load_file_dir_dada2_merged, save_file_dir_dada2_merged)

