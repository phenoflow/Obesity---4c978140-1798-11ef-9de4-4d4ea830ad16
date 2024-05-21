# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"55586.0","system":"readv2"},{"code":"67516.0","system":"readv2"},{"code":"52034.0","system":"readv2"},{"code":"32843.0","system":"readv2"},{"code":"67517.0","system":"readv2"},{"code":"40153.0","system":"readv2"},{"code":"52735.0","system":"readv2"},{"code":"29538.0","system":"readv2"},{"code":"47439.0","system":"readv2"},{"code":"70950.0","system":"readv2"},{"code":"11461.0","system":"readv2"},{"code":"21744.0","system":"readv2"},{"code":"52703.0","system":"readv2"},{"code":"97014.0","system":"readv2"},{"code":"16196.0","system":"readv2"},{"code":"49409.0","system":"readv2"},{"code":"55585.0","system":"readv2"},{"code":"52036.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('obesity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["obesity-history---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["obesity-history---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["obesity-history---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
