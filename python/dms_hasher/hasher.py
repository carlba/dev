import md5

with open ("clean_imsis.txt") as f:
    for line in f:
        print md5.new(line.encode("utf-16-le")).hexdigest()


