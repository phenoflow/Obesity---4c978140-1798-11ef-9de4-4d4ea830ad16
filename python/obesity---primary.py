# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"C38z000","system":"readv2"},{"code":"C380000","system":"readv2"},{"code":"C380400","system":"readv2"},{"code":"C380600","system":"readv2"},{"code":"66CE.00","system":"readv2"},{"code":"ZV65319","system":"readv2"},{"code":"C380500","system":"readv2"},{"code":"C380100","system":"readv2"},{"code":"1444.00","system":"readv2"},{"code":"66C4.00","system":"readv2"},{"code":"212Q.00","system":"readv2"},{"code":"ZC2CM00","system":"readv2"},{"code":"9OK..11","system":"readv2"},{"code":"C380.00","system":"readv2"},{"code":"C380300","system":"readv2"},{"code":"C380700","system":"readv2"},{"code":"104421.0","system":"readv2"},{"code":"25968.0","system":"readv2"},{"code":"24755.0","system":"readv2"},{"code":"22556.0","system":"readv2"},{"code":"64712.0","system":"readv2"},{"code":"10728.0","system":"readv2"},{"code":"38799.0","system":"readv2"},{"code":"49250.0","system":"readv2"},{"code":"38658.0","system":"readv2"},{"code":"11401.0","system":"readv2"},{"code":"8854.0","system":"readv2"},{"code":"38059.0","system":"readv2"},{"code":"7984.0","system":"readv2"},{"code":"52782.0","system":"readv2"},{"code":"38632.0","system":"readv2"},{"code":"22695.0","system":"readv2"},{"code":"17477.0","system":"readv2"},{"code":"70898.0","system":"readv2"},{"code":"3176.0","system":"readv2"},{"code":"69757.0","system":"readv2"},{"code":"430.0","system":"readv2"},{"code":"104129.0","system":"readv2"},{"code":"13278.0","system":"readv2"},{"code":"59780.0","system":"readv2"},{"code":"38294.0","system":"readv2"},{"code":"103574.0","system":"readv2"},{"code":"17444.0","system":"readv2"},{"code":"66406.0","system":"readv2"},{"code":"E66","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('obesity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["obesity---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["obesity---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["obesity---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
