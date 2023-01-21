import barcode
barcode.PROVIDED_BARCODES
['code128', 'code39', 'ean', 'ean13', 'ean14', 'ean8', 'gs1', 'gs1_128', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'itf', 'jan', 'pzn', 'upc', 'upca']
number_barcode = input()
if len(number_barcode) == 13:
    EAN = barcode.get_barcode_class('ean13')
    my_ean = EAN(number_barcode)
    save_name = my_ean.save('ean_barcode')
    'ean_barcode.svg'
if len(number_barcode) == 14:
    EAN = barcode.get_barcode_class('ean14')
    my_ean = EAN(number_barcode)
    save_name = my_ean.save('ean_barcode')
    'ean_barcode.svg'