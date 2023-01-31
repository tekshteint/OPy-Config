import csv

def csvRead() -> None:
    with open("opconfig_ncmx5_obd_pids_master.csv","r") as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0]=="x":
                linesToUse.append(row)
                
def textParse(memAddr: str) -> None:
    with open("logcfg.txt", "w") as output:
        if memAddr != "":
            output.writelines([";-----[ channel setup   ]-----\n",
                        "\n",
                        "type = obd\nprotocolid = 6 ; ISO15765\n",
                        "\n",
                        "calcsampinterval = 500		; timing parameter\n",
                        "\n",
                        "mode23txaddrwidth = 4\nmode23txlenwidth = 2\nmode23rxaddrwidth = 0\n\n",
                        ";-----[ logable parameters ]-----\n",
                        "\nparamname = LOAD_UNCORR\n",
                        "mode = 0x23\n",
                        "paramid = " + memAddr + "\n",
                        "isfloat = 1\n\n"])
        else:
            output.writelines([";-----[ channel setup   ]-----\n",
                        "\n",
                        "type = obd\nprotocolid = 6 ; ISO15765\n",
                        "\n",
                        "calcsampinterval = 500		; timing parameter\n",
                        "\n",
                        "mode23txaddrwidth = 4\nmode23txlenwidth = 2\nmode23rxaddrwidth = 0\n\n",
                        ";-----[ logable parameters ]-----\n\n"])
        
        for col in linesToUse:
            output.writelines([f"paramname = {col[1]}\n",
                               f";description = {col[2]}\n",
                               f"mode = {col[3]}\n",
                               f"paramid = {col[4]}\n",
                               f"databits = {col[6]}\n",
                               f"offsetbits = {col[7]}\n",
                               f"scalingrpn = {col[8]}\n\n"
            ])

def getMemAddr() -> str:
    memAddr = input("Input memory address for logging uncorrected load.\nIf you wish to not log uncorrect load just press enter.\n")
    if memAddr == "":
        return ""
    else:
        return memAddr
    

if __name__ == "__main__":
    linesToUse=[]
    memAddr = getMemAddr()
    csvRead()
    textParse(memAddr)
