def blast_by_NCBIWWW(output_file_path: str):
    result_status = False
    with open(output_file_path, "r") as result_text:
        print(result_text.readline())
        if len(result_text.readline()) > 0:
            result_status = True
    return result_status

load_file_dir_r1 = "C:/Users/kwz50/IdeaProjects/PowerBarcoder/data/result/202307071741/trnLF_result/denoiseResult/r1/Abrodictyum_cumingii_ZXC002739_KTHU1461_.fas"
print(blast_by_NCBIWWW(load_file_dir_r1))