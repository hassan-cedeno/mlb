
def clean_reference_files(data):
    h_row = data[0]
    return [dict(zip(h_row, r)) for r in data[1:-1]]
    