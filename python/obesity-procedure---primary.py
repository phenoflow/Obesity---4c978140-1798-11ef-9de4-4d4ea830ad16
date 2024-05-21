# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"56107.0","system":"readv2"},{"code":"56926.0","system":"readv2"},{"code":"64123.0","system":"readv2"},{"code":"34119.0","system":"readv2"},{"code":"93378.0","system":"readv2"},{"code":"18863.0","system":"readv2"},{"code":"60421.0","system":"readv2"},{"code":"90600.0","system":"readv2"},{"code":"97691.0","system":"readv2"},{"code":"39797.0","system":"readv2"},{"code":"39123.0","system":"readv2"},{"code":"88474.0","system":"readv2"},{"code":"90517.0","system":"readv2"},{"code":"48417.0","system":"readv2"},{"code":"40977.0","system":"readv2"},{"code":"89259.0","system":"readv2"},{"code":"59622.0","system":"readv2"},{"code":"92957.0","system":"readv2"},{"code":"7082.0","system":"readv2"},{"code":"90454.0","system":"readv2"},{"code":"19929.0","system":"readv2"},{"code":"89148.0","system":"readv2"},{"code":"62848.0","system":"readv2"},{"code":"95929.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('obesity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["obesity-procedure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["obesity-procedure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["obesity-procedure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
